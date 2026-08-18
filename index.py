from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        print("جاري فتح الموقع واستخراج الجدول مباشرة...")
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # الانتقال للموقع والانتظار حتى تحميل البيانات
        page.goto("https://www.sdc.com.jo/ar", wait_until="networkidle")
        
        # استهداف العنصر الذي يحتوي على جدول الإحصائيات مباشرة عبر CSS Selector
        # يحدد أي جدول أو حاوية تضم كلمتي 'الجنسية' و 'القيمة السوقية'
        target_element = page.locator("table, div, section").filter(has_text="الجنسية").filter(has_text="القيمة السوقية").first
        
        if target_element.count() > 0:
            print("\n" + "=" * 45)
            print("📊 البيانات المستخرجة بدقة من الحاوية:")
            print("=" * 45)
            print(target_element.inner_text())
            print("=" * 45 + "\n")
        else:
            print("لم يتم العثور على العنصر المحدد داخل الصفحة.")
            
        browser.close()

if __name__ == "__main__":
    main()