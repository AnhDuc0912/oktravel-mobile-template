# Oktravel Mobile — Booking Template

Prototype app booking bằng HTML/CSS/JavaScript thuần, độc lập với frontend/backend; không cần Next.js hay bước build.

**Demo công khai:** https://anhduc0912.github.io/oktravel-mobile-template/

**Repository:** https://github.com/AnhDuc0912/oktravel-mobile-template

## Mở bản thiết kế

Mở `index.html` bằng trình duyệt, hoặc chạy trong thư mục này:

```sh
python3 serve.py
```

Truy cập http://localhost:4173. Điện thoại hiển thị toàn màn hình; desktop hiển thị khung app ở giữa.

## Dịch vụ đối chiếu từ web

| Dịch vụ | Luồng mẫu |
|---|---|
| Khách sạn | Điểm đến → ngày nhận phòng, số đêm → đặt phòng |
| Resort | Tìm resort → phòng cho 2 người → đặt phòng |
| Villa | Tìm villa → villa cho tối đa 6 khách → đặt villa |
| Căn hộ | Tìm căn hộ → căn hộ cho tối đa 4 khách → đặt căn hộ |
| Tour du lịch | Điểm đến → ngày khởi hành, số khách → đặt tour |
| Vé vui chơi | Điểm đến → ngày sử dụng, số vé → đặt vé |
| Vé máy bay | Điểm đi/đến → ngày bay, số khách → thông tin từng hành khách → đặt vé mẫu |
| Thuê xe | Thành phố → điểm đón/trả → ngày, giờ đón → đặt xe có tài xế |
| Nhà hàng | Thành phố → ngày, giờ đến, số khách → đặt bàn theo thực đơn |
| Đặc sản vùng miền | Tìm sản phẩm → số lượng → địa chỉ nhận hàng, phí vận chuyển → đặt mua |
| Cẩm nang du lịch | Danh sách → bài viết → tìm dịch vụ tại điểm đến |

Các nhóm dịch vụ lấy từ các route của `ERAS.oktravel-web/src/app/[locale]`, gồm cả resort, villa và căn hộ. Trang chủ hiển thị một hàng Khách sạn, Tour, Vé máy bay và nút ba chấm “Thêm”. Nút này mở đầy đủ dịch vụ, cẩm nang và ưu đãi trong bảng chọn từ dưới lên.

Có danh sách kết quả, lọc dịch vụ, chi tiết, yêu thích và quản lý đơn mẫu. Yêu thích/đơn lưu trong localStorage. Thông tin liên hệ và tên hành khách chỉ dùng để duyệt biểu mẫu, không lưu trong đơn mẫu.

## Thiết kế và phạm vi

Màu lấy theo logo mặc định: nâu #654930, kem #F3EAD9, vàng đồng #BA8B59. Font Be Vietnam Pro từ Google Fonts, có font hệ thống dự phòng. Ảnh sẵn có trong dự án; các dịch vụ chưa có ảnh dùng hình minh họa bằng icon.

Đây là prototype duyệt giao diện, không kết nối API, xác thực, thanh toán hoặc giữ chỗ. Dữ liệu, giá, đánh giá và chính sách đều minh họa. Chuyến bay mẫu một chiều/phổ thông; lưu trú dùng sức chứa cố định ghi rõ trong form; tour/vé dùng giá người lớn. Tài khoản, ưu đãi và hỗ trợ là màn minh họa.

## Tệp chính

- `index.html`: khung app.
- `catalog.js`: tệp tương thích cho các trang HTML cũ đã lưu trong trình duyệt.
- `app.js`: danh mục dịch vụ, dữ liệu mẫu, màn hình, tìm kiếm, đặt dịch vụ và lưu trạng thái trong cùng một tệp khởi tạo.
- `styles.css`: giao diện responsive.
- `assets/`: logo và ảnh.
