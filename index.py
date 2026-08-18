from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        print("جاري فتح الموقع وانتظار تحميل بيانات الجافاسكريبت...")
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # فتح الصفحة والانتظار حتى انتهاء جميع طلبات الشبكة
        page.goto("https://www.sdc.com.jo/ar", wait_until="networkidle")
        
        # استخراج كافة النصوص الظاهرة في الصفحة
        page_text = page.inner_text("body")
        lines = [line.strip() for line in page_text.split("\n") if line.strip()]
        
        print("\n" + "=" * 45)
        print("📊 نتائج البحث داخل الصفحة:")
        print("=" * 45)
        
        found = False
        for i, line in enumerate(lines):
            if "تداول أعلى خمس جنسيات" in line or "القيمة السوقية" in line:
                found = True
                # طباعة السطر المحدد والأقسام المجاورة له (الجنسيات والأرقام)
                start_index = max(0, i - 1)
                end_index = min(len(lines), i + 20)
                
                for item in lines[start_index:end_index]:
                    print(item)
                break
                
        if not found:
            print("لم يتم العثور على المقطع المطلوبة.")
            
        print("=" * 45 + "\n")
        browser.close()

if __name__ == "__main__":
    main()