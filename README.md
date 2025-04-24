# Tự Động Sao Lưu Cơ Sở Dữ Liệu

Script này giúp tự động sao lưu hàng ngày các file cơ sở dữ liệu SQL và gửi thông báo qua email về trạng thái sao lưu.

## Tính Năng
- Kiểm tra các file SQL trong thư mục chỉ định  
- Tạo bản sao lưu trong thư mục backup được cấu hình  
- Gửi email thông báo về trạng thái sao lưu  
- Được thiết lập để chạy tự động hàng ngày vào lúc nửa đêm

## Hướng Dẫn Cài Đặt

1. Cài đặt các thư viện cần thiết:
   ```
   pip install -r requirements.txt
   ```

2. Cấu hình biến môi trường trong file `.env`:
   - `SENDER_EMAIL`: Địa chỉ Gmail của bạn  
   - `PASSWORD`: Mật khẩu ứng dụng Gmail  
   - `RECIEVER_EMAIL`: Email nhận thông báo  

3. Tạo các thư mục cần thiết:
   ```
   mkdir sql backup
   ```

4. Đặt các file SQL của bạn vào thư mục `sql`

5. Chạy script:
   ```
   python main.py
   ```

## Lưu Ý
- Đối với Gmail, bạn cần tạo **mật khẩu ứng dụng** thay vì dùng mật khẩu thông thường  
- Script được cấu hình để kiểm tra file có tên `a.sql` trong thư mục `sql`