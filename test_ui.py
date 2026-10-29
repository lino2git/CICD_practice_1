import re
from playwright.sync_api import Page, expect

def test_example_website(page: Page):
    page.goto("https://example.com")
    expect(page).to_have_title(re.compile("Example Domain"))
    
    h1_element = page.locator("h1")
    expect(h1_element).to_contain_text("Example Domain")