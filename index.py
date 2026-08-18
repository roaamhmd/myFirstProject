import pandas as pd
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
            rows = target_element.locator("tr").all()
            table_data = []

            for row in rows:
                cells = [col.inner_text().strip() for col in row.locator("th, td").all()]
                filtered_cells = [c for c in cells if c != ""]
                
                if filtered_cells:
                    table_data.append(filtered_cells)

            if len(table_data) > 1:
                df = pd.DataFrame(table_data[1:], columns=table_data[0])
                df.to_excel("top_5_nationalities.xlsx", index=False)
                print("✅ تم استخراج البيانات وحفظها بنجاح في ملف top_5_nationalities.xlsx")
            else:
                print("⚠️ الجدول فارغ أو لا يحتوي على عناصر كافية")

        browser.close()

if __name__ == "__main__":
    main()