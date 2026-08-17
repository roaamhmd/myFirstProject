import requests
from bs4 import BeautifulSoup

# 1. رابط الصفحة الرئيسية للموقع
url = "https://www.sdc.com.jo/ar"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# 2. جلب محتوى الصفحة
response = requests.get(url, headers=headers)
response.encoding = 'utf-8'

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 3. البحث عن جميع الجداول في الصفحة
    tables = soup.find_all('table')
    target_table = None
    
    # البحث عن الجدول الذي يحتوي على البيانات المطلوبة
    for table in tables:
        if "تداول أعلى خمس جنسيات" in table.text or "القيمة السوقية" in table.text:
            target_table = table
            break

    # 4. استخراج البيانات وطباعتها
    if target_table:
        print("\n" + "=" * 45)
        print("📊 تداول أعلى خمس جنسيات - القيمة السوقية")
        print("=" * 45)
        
        rows = target_table.find_all('tr')
        for row in rows:
            # جلب محتوى الخلايا (العناوين والبيانات)
            cols = [cell.text.strip() for cell in row.find_all(['th', 'td']) if cell.text.strip()]
            if cols:
                # تنسيق العرض على الشاشة
                print(f"{cols[0]:<20} | {cols[1]:<15} | {cols[2] if len(cols) > 2 else '':<8}")
        
        print("=" * 45 + "\n")
    else:
        print("لم يتم العثور على الجدول داخل الصفحة.")
else:
    print(f"تعذر الاتصال بالموقع، كود الحالة: {response.status_code}")