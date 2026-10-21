# LAB 9 — KIỂM THỬ TỰ ĐỘNG WEBSITE VỚI SELENIUM

**Sinh viên:** Trần Văn Nhật · **MSSV:** 23010625  
**Bài thực hành:** Selenium WebDriver — kiểm thử chức năng tự động

> **Trạng thái:** Đã xây dựng website Demo Shop và **07 test case tự động** sử dụng Selenium + Python. **Chưa ghi nhận kết quả PASS/FAIL thực nghiệm**; cần chạy test trên Chrome rồi tải ảnh chụp thực tế lên repository.

## 1. Mục tiêu

- Tìm hiểu Selenium WebDriver và phương pháp kiểm thử tự động website.
- Thực hiện **ít nhất 05 test case**: đăng nhập, tìm kiếm, giỏ hàng, đăng xuất.
- Sử dụng Selenium locators (ID, CSS selector), assertion và explicit wait.
- Thu thập ảnh chụp màn hình, tổng hợp kết quả và trình bày báo cáo trong GitHub README.

## 2. Kiến thức và công cụ

**Selenium WebDriver** là công cụ điều khiển trình duyệt để tự động thao tác và xác minh giao diện. Mỗi test case có bước chuẩn bị (Arrange), thực hiện (Act) và đối chiếu kết quả mong đợi (Assert).

| Công cụ | Mục đích |
|---|---|
| Python 3.10+ | Viết mã kiểm thử |
| Selenium 4 | Điều khiển trình duyệt Chrome |
| unittest | Quản lý, chạy và báo cáo test case |
| Chrome | Trình duyệt cần kiểm thử |
| Selenium Manager | Hỗ trợ quản lý driver trên môi trường tương thích |
| Python http.server | Chạy website demo trên localhost |

Tài liệu học: [Selenium Documentation](https://www.selenium.dev/documentation/) · [WebDriver Getting Started](https://www.selenium.dev/documentation/webdriver/getting_started/) · [Python unittest](https://docs.python.org/3/library/unittest.html).

## 3. Website được kiểm thử

Website **Demo Shop** là trang mô phỏng thương mại điện tử được xây dựng riêng cho bài Lab, chạy tại **http://127.0.0.1:8000**. Chức năng gồm đăng nhập, tìm kiếm 3 sản phẩm (Laptop, Mouse, Keyboard), thêm/xóa giỏ hàng và đăng xuất.

- **Tài khoản demo:** `student`
- **Mật khẩu:** `123456`

**Phạm vi:** Website HTML/JavaScript chạy trong trình duyệt, không có backend, dữ liệu thật hay thanh toán. Đây là bài kiểm thử chức năng giao diện cho mục đích học tập.

## 4. Cấu trúc repository

```text
23010625_Selenium_Lab9/
├── README.md
├── requirements.txt
├── .gitignore
├── site/
│   └── index.html                # Website Demo Shop
├── tests/
│   └── test_shop.py              # 07 test case Selenium
└── screenshots/                  # Ảnh thật được tạo sau khi chạy test
```

## 5. Hướng dẫn cài đặt và chạy trên Windows

**Yêu cầu:** Python 3.10+, Google Chrome và kết nối Internet khi Selenium Manager cần tải driver.

Mở **VS Code Terminal / PowerShell**:

```powershell
git clone https://github.com/nhat965/23010625_Selenium_Lab9.git
cd 23010625_Selenium_Lab9
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Nếu PowerShell chặn activation script, có thể không kích hoạt môi trường mà gọi trực tiếp `.venv\Scripts\python.exe` cho các lệnh Python sau.

### Terminal 1 — Khởi động website

Tại thư mục gốc repo, chạy:

```powershell
cd site
python -m http.server 8000 --bind 127.0.0.1
```

Giữ terminal mở, kiểm tra website bằng Chrome: **http://127.0.0.1:8000**.

### Terminal 2 — Chạy 7 test case

Mở terminal mới tại **thư mục gốc** repo:

```powershell
python -m unittest discover -s tests -p "test_*.py" -v
```

Selenium mở Chrome tự động, thực hiện thao tác và đóng browser sau từng bài. Mỗi test được chạy trong một Chrome session mới. File ảnh được lưu vào thư mục `screenshots/` kể cả khi assertions thất bại (nếu driver và trình duyệt đã khởi tạo thành công).

**Tùy chọn chạy ẩn (headless):**

```powershell
$env:HEADLESS="1"
python -m unittest discover -s tests -p "test_*.py" -v
```

Để nhìn thấy Chrome thao tác trực tiếp, dùng chế độ mặc định (không đặt HEADLESS).

## 6. Danh sách 07 test case

| ID | Tên test / chức năng | Các bước thực hiện | Kết quả mong đợi |
|---|---|---|---|
| TC01 | `test_01_login_success` | Nhập student / 123456, bấm Đăng nhập | Hiển thị cửa hàng và lời chào student |
| TC02 | `test_02_login_invalid` | Nhập sai mật khẩu, bấm Đăng nhập | Báo lỗi, không hiển thị cửa hàng |
| TC03 | `test_03_search_product` | Đăng nhập, tìm từ khóa mouse | Hiển thị đúng 1 sản phẩm Mouse |
| TC04 | `test_04_search_missing` | Đăng nhập, tìm not-exist | Hiện “Không tìm thấy sản phẩm” |
| TC05 | `test_05_add_to_cart` | Đăng nhập, thêm Laptop | Số lượng giỏ hàng = 1, có Laptop |
| TC06 | `test_06_clear_cart` | Đăng nhập, thêm Mouse, xóa giỏ | Số lượng giỏ = 0, hiện “Giỏ hàng trống” |
| TC07 | `test_07_logout` | Đăng nhập, bấm Đăng xuất | Quay lại trang đăng nhập, ẩn cửa hàng |

**Cách xác minh:** `assertEqual`, `assertIn`, `assertTrue`, `assertFalse` cùng `WebDriverWait` trong mã Python.

## 7. Báo cáo kết quả thực nghiệm

### 7.1. Kết quả chạy

> **Chưa có bằng chứng chạy Selenium thực tế trong môi trường của sinh viên.** Không coi số lượng test đã viết là số test đã PASS.

| Chỉ số | Giá trị hiện tại |
|---|---|
| Test case đã xây dựng | 07 |
| Test case đã chạy trên máy | Chưa xác nhận |
| PASS | Chưa xác nhận |
| FAIL / ERROR | Chưa xác nhận |
| Phiên bản Python / Chrome / Selenium | Bổ sung sau khi thực hiện |
| Thời gian thực hiện | Bổ sung từ kết quả terminal |

Sau khi chạy, ghi kết quả cuối terminal (ví dụ `Ran 7 tests in ...`, `OK` hoặc chi tiết FAILED), cập nhật bảng này theo số liệu thật.

### 7.2. Ảnh minh họa

Bộ test được cấu hình để **tự động lưu 7 ảnh sau khi chạy**, theo tên từng test case. Các đường dẫn ảnh dưới đây sẽ hiển thị sau khi bạn đẩy ảnh thật vào `screenshots/`.

**Hình 1 — TC01: Đăng nhập thành công**

![TC01 Login success](screenshots/test_01_login_success.png)

**Hình 2 — TC02: Sai mật khẩu**

![TC02 Invalid login](screenshots/test_02_login_invalid.png)

**Hình 3 — TC03: Tìm kiếm Mouse**

![TC03 Product search](screenshots/test_03_search_product.png)

**Hình 4 — TC04: Không tìm thấy sản phẩm**

![TC04 No results](screenshots/test_04_search_missing.png)

**Hình 5 — TC05: Thêm Laptop vào giỏ**

![TC05 Add to cart](screenshots/test_05_add_to_cart.png)

**Hình 6 — TC06: Xóa giỏ hàng**

![TC06 Clear cart](screenshots/test_06_clear_cart.png)

**Hình 7 — TC07: Đăng xuất**

![TC07 Logout](screenshots/test_07_logout.png)

**Ảnh nên bổ sung:** Chụp cửa sổ terminal chứa kết quả tổng hợp `Ran 7 tests`, số PASS / FAIL và thời gian thực hiện; lưu ở `screenshots/08-terminal-results.png`.

### 7.3. Các bước nộp ảnh và kết quả

```powershell
git add README.md screenshots/
git commit -m "Add Selenium Lab 9 actual test results and screenshots"
git push origin main
```

Chỉ ghi PASS khi có kết quả chạy thực tế xác nhận.

## 8. Nhận xét và kết luận

Bộ kiểm thử gồm **7 kịch bản** bao phủ các thao tác chính của website: xác thực người dùng, tìm kiếm dữ liệu, cập nhật giỏ hàng và đăng xuất. Kiểm thử cả trường hợp hợp lệ và không hợp lệ, sử dụng Selenium để thao tác trên Chrome và assertion để kiểm tra trạng thái ứng dụng.

**Giới hạn:** Website mô phỏng chỉ chạy trong trình duyệt trên localhost, chưa kiểm thử backend, lưu trữ dữ liệu, thanh toán, bảo mật hay khả năng chịu tải. Cần chạy bộ test thực tế và đối chiếu PASS/FAIL trước khi kết luận website đạt yêu cầu.

---

**Trần Văn Nhật — 23010625 | Selenium Lab 9**
