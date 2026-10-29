import re
from playwright.sync_api import Page, expect

def test_example_website(page: Page):
    # 1. 強制設定瀏覽器請求標頭為英文
    page.set_extra_http_headers({"Accept-Language": "en-US,en;q=0.9"})

    # 2. 前往目標網站
    page.goto("https://example.com")

    # 3. 驗證 Title
    expect(page).to_have_title(re.compile("Example Domain"))

    # 4. 驗證內文段落
    paragraph = page.locator("p").first
    expect(paragraph).to_contain_text("documentation examples")

    # 5. 點擊 Learn more 連結
    learn_more_link = page.get_by_role("link", name=re.compile("Learn more|了解更多|詳細資訊", re.I))
    learn_more_link.click()

    # 6. 驗證網址
    expect(page).to_have_url(re.compile("iana.org"))