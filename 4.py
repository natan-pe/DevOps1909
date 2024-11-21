import requests
import time
import json

url = 'https://www.oref.org.il/WarningMessages/alert/alerts.json'
headers = {
    'Referer': 'https://www.oref.org.il/',
    'X-Requested-With': 'XMLHttpRequest'
}

# משתנה לאחסון המצב הקודם של הקובץ
previous_data = None

while True:
    try:
        # בקשת הקובץ
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            # התמודדות עם ה-BOM והמרת התוכן ל-JSON
            content = response.content.decode('utf-8-sig')
            current_data = json.loads(content)

            # השוואת הנתונים הנוכחיים לנתונים הקודמים
            if current_data != previous_data:
                print("יש שינוי בנתונים:")
                print(current_data)

                # עדכון המצב הקודם
                previous_data = current_data
            else:
                print("אין שינוי בנתונים")

        else:
            print(f'שגיאה בקבלת הנתונים: {response.status_code}')

    except Exception as e:
        print(f'אירעה שגיאה: {str(e)}')

    # המתנה של 30 שניות לפני הבדיקה הבאה (אפשר לשנות לפי הצורך)
    time.sleep(2)
