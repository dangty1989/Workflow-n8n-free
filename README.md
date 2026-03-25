# 🚀 Kho Workflow n8n Miễn Phí & Facebook Auto Post Bot

Chào mừng bạn đến với kho lưu trữ workflow n8n và các công cụ tự động hóa miễn phí của **Đặng Tỵ!** Đây là nơi chia sẻ những giải pháp thực chiến, giúp bạn giải phóng sức lao động và tối ưu hóa vận hành doanh nghiệp.

---

## 🌟 Giải pháp tiêu điểm: Facebook Auto Post Engine (Playwright + Python)

Đây là bộ engine "Vàng" giúp bạn tự động hóa việc đăng bài lên Facebook cá nhân với độ an toàn cực cao, hỗ trợ nhiều tài khoản cùng lúc.

### ✨ Tính năng nổi bật (Key Features):
*   **🔐 Đa tài khoản (Multi-profile):** Mỗi nick Facebook có một Chrome Profile riêng, không lo lẫn lộn Cookie.
*   **🛡️ Chống Checkpoint (Stealth Mode):** Mô phỏng hành vi người thật (gõ phím ngẫu nhiên, trễ tự nhiên) — Facebook không thể phát hiện bot.
*   **🔒 Hỗ trợ Public/Private:** Tự động chọn đối tượng bài viết (Công khai hoặc Chỉ mình tôi).
*   **⚡ n8n Ready:** Tích hợp cực kỳ đơn giản vào n8n qua node `Execute Command`.
*   **🏠 100% Local:** Mọi dữ liệu đăng nhập nằm trên máy của bạn, bảo mật tuyệt đối.

---

## 🛠️ Hướng dẫn cài đặt (Quick Start)

### 1. Cài đặt môi trường
Đảm bảo bạn đã cài Python, sau đó chạy lệnh:
```bash
pip install playwright python-dotenv
playwright install chromium
```

### 2. Đăng nhập tài khoản (Chỉ cần 1 lần duy nhất)
```bash
python fb_engine.py login --profile ten_nick_cua_ban
```
*Trình duyệt sẽ mở ra -> Bạn đăng nhập FB -> Đóng trình duyệt. Xong!*

### 3. Đăng bài tự động
```bash
# Đăng công khai
python fb_engine.py post_feed --profile ten_nick_cua_ban --content "Nội dung bài viết"

# Đăng riêng tư (Chỉ mình tôi)
python fb_engine.py post_feed --profile ten_nick_cua_ban --content "Nội dung" --private
```

---

## 🔗 Tích hợp n8n (n8n Integration)

Sử dụng node **Execute Command** trong n8n để gọi script:
```bash
python C:\duong\dan\fb_engine.py post_feed --profile {{ $json.profile }} --content "{{ $json.content }}"
```

---

## 📦 Các Workflow n8n đi kèm:
Ngoài bộ Post Facebook, kho này còn chứa các template n8n miễn phí:
*   `minh_triet_caption_per_scene`: Mẫu thiết kế caption cho video.
*   `n8n_zapier_buffer_tiktok`: Quy trình đồng bộ video lên TikTok.

---

## 🤝 Kết nối với tôi (Connect with Me)

Nếu bạn cần hỗ trợ cài đặt hoặc muốn tùy chỉnh giải pháp cho doanh nghiệp:
*   **Zalo:** 0943 798 542 (Đặng Tỵ)
*   **Notion:** [Tài liệu Vận hành & Hướng dẫn](https://www.notion.so/32ebde87a17481968b04de07c714cec5)
*   **Email:** dangducty@gmail.com

---
*Cảm ơn bạn đã quan tâm! Nếu thấy hữu ích, hãy tặng tôi 1 ⭐ cho Repo này nhé!*
