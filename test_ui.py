import re
from playwright.sync_api import Page, expect

def test_example_website(page: Page):
    # 1. 前往目標網站
    page.goto("https://example.com")

    # 2. 驗證 Title (不管哪個語言 Title 都是 Example Domain)
    expect(page).to_have_title(re.compile("Example Domain"))

    # 3. 驗證第一個段落元素存在且可見 (不綁定特定語言文字)
    paragraph = page.locator("p").first
    expect(paragraph).to_be_visible()

    # 4. 定位包含 target url 的超連結 (不依賴按鈕顯示的是 "Learn more" 還是 "了解更多")
    learn_more_link = page.locator("a[href*='iana.org']")
    expect(learn_more_link).to_be_visible()
    
    # 5. 點擊連結並驗證跳轉
    learn_more_link.click()
    expect(page).to_have_url(re.compile("iana.org"))