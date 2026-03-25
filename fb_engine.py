import os, json, time, random, argparse
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv

load_dotenv()
BASE_DIR = r"f:\DangTy - Automation\Profiles"

class FBEngine:
    def __init__(self, p_name):
        self.p_dir = os.path.join(BASE_DIR, p_name)
        os.makedirs(self.p_dir, exist_ok=True)

    def _d(self, m=3, x=7): time.sleep(random.uniform(m, x))
    def _ty(self, l, t):
        for c in t: l.type(c, delay=random.uniform(50, 150))

    def login(self):
        print(f"[LOGIN] {self.p_dir}")
        with sync_playwright() as p:
            ctx = p.chromium.launch_persistent_context(user_data_dir=self.p_dir, channel="chrome", headless=False, no_viewport=True)
            page = ctx.new_page(); page.goto("https://www.facebook.com/")
            print(">>> HÃY ĐĂNG NHẬP. SAU KHI XONG, HÃY ĐÓNG TRÌNH DUYỆT ĐỂ LƯU.")
            try: page.wait_for_timeout(300000)
            except: pass # Bỏ qua lỗi khi người dùng đóng trình duyệt thủ công
            finally: ctx.close()

    def post_f(self, msg, pr=False):
        print(f"[FEED] Profile: {self.p_dir} (Private: {pr})")
        with sync_playwright() as p:
            ctx = p.chromium.launch_persistent_context(user_data_dir=self.p_dir, channel="chrome", headless=False, viewport={'width':1280,'height':720})
            page = ctx.new_page()
            try:
                page.goto("https://www.facebook.com/"); self._d(5, 8); page.keyboard.press("Escape")
                
                # Mở hộp thoại đăng bài
                print(">>> Đang mở hộp thoại...")
                page.locator('div[role="button"]:has-text("on your mind"), div[role="button"]:has-text("đang nghĩ gì")').first.click()
                self._d(4, 6)

                # Chế độ riêng tư
                if pr:
                    try:
                        aud = page.locator('div[role="button"] >> text=/Công khai|Public|Bạn bè|Friends|Đối tượng|Audience/').first
                        aud.click(); self._d(3, 5)
                        page.locator('text=/Only me|Chỉ mình tôi/').first.click(); self._d(2, 4)
                        dn = page.locator('text=/Xong|Done|Lưu|Save/').first
                        if dn.is_visible(): dn.click()
                    except: pass

                # Nhập nội dung
                print(">>> Đang nhập nội dung...")
                tb = page.locator('div[role="textbox"][contenteditable="true"]').nth(-1)
                tb.wait_for(state="visible", timeout=15000)
                tb.focus(); self._ty(tb, msg); self._d(3, 5)

                # Bấm Tiếp (Nếu có)
                nxt = page.locator('div[role="button"]:has-text("Tiếp"), div[role="button"]:has-text("Next")').first
                if nxt.is_visible():
                    nxt.click(); self._d(4, 6)

                # Bấm Đăng
                print(">>> Đang hoàn tất đăng bài...")
                btn = page.locator('div[role="button"]:has-text("Đăng"), div[role="button"]:has-text("Post"), [aria-label="Đăng"], [aria-label="Post"]').last
                btn.click()
                
                # Chờ xác nhận phụ (Confirmation)
                self._d(8, 12)
                confirm = page.locator('text=/Xác nhận|Confirm|OK|Đăng/').last
                if confirm.is_visible(): confirm.click(); self._d(5, 8)
                
                print("--- ĐĂNG BÀI THÀNH CÔNG ---")
            except Exception as e: print(f"LỖI: {e}")
            finally: ctx.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["login", "post_feed"])
    parser.add_argument("--profile", required=True); parser.add_argument("--content"); parser.add_argument("--private", action="store_true")
    args = parser.parse_args(); e = FBEngine(args.profile)
    if args.action == "login": e.login()
    elif args.action == "post_feed": e.post_f(args.content, args.private)
