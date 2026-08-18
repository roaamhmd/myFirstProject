from playwrite.sync_api import sync_playwrite

def main():
    with sync_playwrite() as p:
        browser = p.chromiom.launch(headless=True)
        page = browser.new_page()

    page.goto("https://www.sdc.com.jo/ar",wait_until="networkidle")
     
    target_element = page.get_by_text("تداول اعلى خمس جنسيات").locator("xpath=following::table[1]")

    if target_element == 0:
        print("لم يتم العثور على البيانات المطلوبة")
    else:
        print(target_element.inner_text().strip())

if __name__ == "__main__":
    main()