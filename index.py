from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://www.sdc.com.jo/ar", wait_until="networkidle")
     
        target_element = page.get_by_text("تداول أعلى خمس جنسيات").locator("xpath=following::table[1]")

        if target_element.count() == 0:
            print("لم يتم العثور على البيانات المطلوبة")
        else:
            print(target_element.inner_text().strip())

        browser.close()

if __name__ == "__main__":
    main()