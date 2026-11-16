# Hợp đồng mẫu kiểm bảng giá

Tác giả: PM - TKC

[CHỜ COO DUYỆT – D-04] Sheet Bang_Gia; hàng 1: STT, Sản phẩm, Giá thị trường, Giá hội viên, % nhà bán, % Affiliate, Cơ sở tính, Trạng thái, Ghi chú. Dòng sản phẩm có STT số nguyên; dòng KIỂM TRA là dòng tổng tỷ lệ của sản phẩm ngay trước, STT chứa chữ KIỂM TRA. Tỷ lệ dạng số thực 0–1. Cơ sở tính phải GIÁ HỘI VIÊN; nếu không có cột thì cần người đối chiếu công thức, không tự kết luận. Dữ liệu mẫu trong fixture là câu “DÒNG VÍ DỤ SIM”; mẫu thực phải cung cấp dấu hiệu đã xác nhận, không dùng tên thật.

Đọc data_only=True không tính công thức; cache thiếu là chưa xác minh. Cache có mặt vẫn có thể cũ: người cung cấp phải xác nhận tính lại trong Excel. Script chỉ kiểm kỹ thuật trên schema này, không nhận diện PII tự động.

Nguồn: skill vận hành nội bộ của nhóm (bản 11/2026), đã lược thông tin nội bộ
