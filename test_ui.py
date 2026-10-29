import re
from playwright.sync_api import Page, expect

def test_example_website(page: Page):
    # 1. 前往目標網站
    page.goto("https://example.com")

    # 2. 驗證網頁 Title 是否包含 "Example Domain"
    expect(page).to_have_title(re.compile("Example Domain"))

    # 3. 驗證內文段落是否包含關鍵字（適應新版 example.com 的結構）
    paragraph = page.locator("p").first
    expect(paragraph).to_contain_text("documentation examples")

    # 4. 驗證頁面上有 "Learn more" 連結並點擊
    learn_more_link = page.get_by_role("link", name="Learn more")
    expect(learn_more_link).to_be_visible()
    learn_more_link.click()

    # 5. 驗證跳轉後的網址是否為 iana.org
    expect(page).to_have_url(re.compile("iana.org"))