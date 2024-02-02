# import requests

# from bs4 import BeautifulSoup


# url = 'https://www.paixin.com/albums/pic/detail/1618/1'
# res = requests.get(url).text

# print(res)

# content = BeautifulSoup(res, "html.parser")


# 获取三个浏览器中百度
# from playwright.sync_api import sync_playwright
# with sync_playwright() as p:
#     for browser_type in [p.chromium, p.firefox, p.webkit]:
#         browser = browser_type.launch(headless=False)
#         page = browser.new_page()
#         page.goto('https://www.baidu.com')
#         page.screenshot(path=f'screenshot-{browser_type.name}.png')
#         print(page.title())
#         browser.close()



from playwright.sync_api import Playwright, sync_playwright, expect


def URIConcatHttp(uri):
    if uri.find('http') == -1:
        uri = 'https://sql.wang' + uri
    return uri




def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://sql.wang")
    page.evaluate("() => window.scrollTo(0,document.body.scrollHeight)")
    page.wait_for_timeout(5000)
    
    pic_src=page.query_selector_all('//img')
    for pic in pic_src:
        url = pic.get_attribute('src')
        new_url = URIConcatHttp(url)
        print(new_url)
    
    page.wait_for_timeout(20000)

    page.close()
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)