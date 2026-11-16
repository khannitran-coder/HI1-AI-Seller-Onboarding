"""Tác giả: PM - TKC. Kiểm schema SIM; không sửa workbook, không phản hồi nội dung tự do."""
import argparse,json,math
from numbers import Real
from openpyxl import load_workbook
HEADERS=['STT','Sản phẩm','Giá thị trường','Giá hội viên','% nhà bán','% Affiliate','Cơ sở tính','Trạng thái','Ghi chú']
def number(v):return isinstance(v,Real) and not isinstance(v,bool) and math.isfinite(v)
def review(path,sheet='Bang_Gia',sample_markers=('DÒNG VÍ DỤ SIM',)):
    w=load_workbook(path,data_only=True,read_only=True);f=load_workbook(path,data_only=False,read_only=True)
    errors=[];unknown=[];product_count=0
    def add(row,code,value):errors.append({'STT':row,'sản phẩm':f'dòng {row}','quy tắc vi phạm':code,'giá trị':value,'đề xuất người kiểm':'Đối chiếu nguồn; nhà bán xác nhận, không tự sửa'})
    try:
        data=list(w[sheet].values);forms=list(f[sheet].values)
        if not data or list(data[0][:9])!=HEADERS:raise ValueError('Schema cần ánh xạ')
        last=max((i for i,row in enumerate(data) if any(v is not None for v in row)),default=0)
        for idx,raw in enumerate(data[1:last+1],2):
            row=tuple(raw)+(None,)*max(0,9-len(raw))
            if not any(v is not None for v in row):add(idx,'PR-06','Dòng trống giữa bảng');continue
            missing=set()
            for col,expr in enumerate(forms[idx-1][:9]):
                if isinstance(expr,str) and expr.startswith('=') and row[col] is None:
                    missing.add(col);unknown.append({'dòng':idx,'cột':col+1,'lý do':'Thiếu cache công thức'})
            if row[0]=='KIỂM TRA':
                if missing.intersection({4,5}):continue
                a,b=row[4:6]
                if not number(a) or not number(b) or not math.isclose(a+b,1,abs_tol=1e-9):add(idx,'PR-02','Tổng tỷ lệ không đủ 100% hoặc không phải số')
                continue
            if not isinstance(row[0],int) or isinstance(row[0],bool):unknown.append({'dòng':idx,'lý do':'Không xác định dòng sản phẩm'});continue
            product_count+=1
            if 7 not in missing and row[7]!='ĐÚNG':add(idx,'PR-01','Trạng thái khác ĐÚNG')
            if 6 not in missing and row[6]!='GIÁ HỘI VIÊN':add(idx,'PR-03','Cơ sở tính không phải GIÁ HỘI VIÊN')
            if not missing.intersection({2,3}):
                if not all(number(v) for v in row[2:4]):add(idx,'PR-06','Ô giá không phải số')
                elif row[3]>=row[2]:add(idx,'PR-04','Giá hội viên không thấp hơn giá thị trường')
            if any(v.casefold() in str(row[8] or '').casefold() for v in sample_markers):add(idx,'PR-05','Còn câu/dòng ví dụ của mẫu')
        if product_count==0:unknown.append({'lý do':'Không có dòng sản phẩm đã xác định'})
        return {'tổng kết':'Không đạt' if errors else ('Chưa xác minh' if unknown else 'Đạt kiểm tra kỹ thuật'),'lỗi':errors,'chưa xác minh':unknown,'lưu ý':'[CHỜ COO DUYỆT – D-04]; xác nhận cache/quy tắc, không phải phê duyệt nghiệp vụ'}
    finally:w.close();f.close()
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('file');p.add_argument('--sheet',default='Bang_Gia');p.add_argument('--sample-marker',action='append');a=p.parse_args()
    try:
        result=review(a.file,a.sheet,a.sample_marker or ('DÒNG VÍ DỤ SIM',));print(json.dumps(result,ensure_ascii=False,indent=2));return 2 if result['lỗi'] else (3 if result['chưa xác minh'] else 0)
    except Exception as exc:p.exit(1,f'Chưa xác minh: {type(exc).__name__}; kiểm file/schema/quyền.\n')
if __name__=='__main__':raise SystemExit(main())
