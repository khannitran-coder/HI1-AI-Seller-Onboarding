"""Tác giả: PM - TKC. Kiểm/đóng gói skills/, không cài hoặc bật quyền."""
import argparse
import csv
import json
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCHEMA = ROOT/'skills/daily-operations-report/references/tracker-schema.json'


def scalar(value):
    value = value.strip()
    if value.startswith('"'):
        return json.loads(value)  # Frontmatter uses JSON-compatible YAML double quotes.
    if value.startswith("'"):
        if not value.endswith("'"):
            raise ValueError('Chuỗi YAML thiếu dấu đóng')
        return value[1:-1].replace("''", "'")
    if not value or any(c in value for c in '{}[]') or ': ' in value:
        raise ValueError('Cần scalar YAML đơn giản hoặc chuỗi có dấu nháy')
    return value


def metadata(text):
    if not text.startswith('---\n') or '\n---\n' not in text[4:]:
        raise ValueError('Thiếu frontmatter')
    front = text.split('---', 2)[1]
    result = {}
    for line in front.strip().splitlines():
        if not line.strip() or line.lstrip().startswith('#'):
            continue
        key, separator, value = line.partition(':')
        if not separator or key in result:
            raise ValueError('Frontmatter sai/khóa trùng')
        result[key] = scalar(value)
    return result


def check():
    issues = []
    folders = sorted(p for p in (ROOT/'skills').iterdir() if p.is_dir() and p.name != '__pycache__')
    for folder in folders:
        try:
            text = (folder/'SKILL.md').read_text(encoding='utf-8')
            data = metadata(text)
            if data.get('name') != folder.name or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', data['name']):
                raise ValueError('name không khớp folder/kebab-case')
            if not isinstance(data.get('description'), str) or not 1 <= len(data['description']) <= 1024:
                raise ValueError('description rỗng hoặc quá 1024 ký tự')
            if not re.search(r'^version: \d+\.\d+\.\d+\s*$', text, re.M):
                raise ValueError('Thiếu version')
            paths = set(re.findall(r'(?<![\w/.-])(?:[\w.-]+/)+[\w.-]+\.(?:md|json|py|ps1|csv|txt)', text))
            paths.update(re.findall(r'\]\(([^)#]+)(?:#[^)]*)?\)', text))
            if 'requirements.txt' in text:
                paths.add('requirements.txt')
            for target in paths:
                if re.match(r'https?://', target):
                    continue
                path = (folder/target).resolve()
                if not path.is_relative_to(folder.resolve()) or not path.is_file():
                    raise ValueError('Tham chiếu thiếu hoặc ngoài folder')
            for file in folder.rglob('*'):
                if file.is_symlink():
                    raise ValueError('Không đóng gói symlink')
        except (OSError, ValueError, KeyError, TypeError) as exc:
            issues.append(f'{folder.name}: {exc}')
    try:
        schema = json.loads(SCHEMA.read_text(encoding='utf-8'))
        with (ROOT/'templates/tracker-header.csv').open(encoding='utf-8-sig', newline='') as f:
            if next(csv.reader(f)) != schema['columns']:
                issues.append('Header tracker không khớp JSON')
    except (ValueError, OSError, KeyError, StopIteration):
        issues.append('Không đọc được schema/header')
    manifest_path = ROOT/'tests/fixtures/fixture-manifest.json'
    exemptions = set()
    if manifest_path.exists():
        try:
            manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
            for name in manifest['synthetic_red_fixtures']:
                path = (ROOT/name).resolve()
                if not path.is_relative_to((ROOT/'tests/fixtures').resolve()) or not path.is_file():
                    raise ValueError('Fixture ngoài phạm vi')
                exemptions.add(path)
        except (KeyError, OSError, ValueError):
            issues.append('Manifest fixture không hợp lệ')
    patterns = [re.compile(v, re.I) for v in [r'pass\s*:', r'\b[A-Z]:[\\/]', r'page=', r'docs\.google']]
    for file in ROOT.rglob('*'):
        if any(part in {'.git', 'dist', '__pycache__', '.venv'} for part in file.relative_to(ROOT).parts):
            continue
        if file.is_file() and file.suffix in {'.md', '.csv', '.json'}:
            try:
                text = file.read_text(encoding='utf-8')
                for line, value in enumerate(text.splitlines(), 1):
                    if any(p.search(value) for p in patterns) or (file.resolve() not in exemptions and re.search(r'\d{9,}', value)):
                        issues.append(f'{file.relative_to(ROOT)} dòng {line}: nghi chuỗi bí mật (không in giá trị)')
            except UnicodeError:
                issues.append(f'{file.relative_to(ROOT)}: không đọc được UTF-8')
    return folders, issues


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    folders, issues = check()
    if issues:
        print('\n'.join(issues), file=sys.stderr)
        return 2
    print(f'Đạt: {len(folders)} Skill; frontmatter, version, tham chiếu, schema/header và quét bí mật.')
    if not args.check:
        out = ROOT/'dist'
        out.mkdir(exist_ok=True)
        for folder in folders:
            with zipfile.ZipFile(out/(folder.name+'.zip'), 'w', zipfile.ZIP_DEFLATED) as archive:
                for file in sorted(folder.rglob('*')):
                    if file.is_file() and '__pycache__' not in file.parts and file.suffix != '.pyc':
                        archive.write(file, file.relative_to(folder))
            print(f'dist/{folder.name}.zip')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
