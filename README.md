# we use guest user, so there was no need to do login function/page
# range does not really works
# make sure to skip outofstock in dropdown
# check subtotal
DRAFTDRAFTDRAFTDRAFTDRAFTDRAFTDRAFTDRAFTDRAFTDRAFTDRAFTDRAFT
🛒 eBay Automation Project

פרויקט אוטומציה מקצה לקצה (E2E) עבור אתר eBay, המבוסס על Python + Playwright + pytest, עם ארכיטקטורת Page Object Model.

📋 דרישות מקדימות (Prerequisites)

יש לוודא שמותקנים במערכת:

Python 3.10+

pip

Git

מערכת הפעלה: Windows / macOS / Linux

דפדפן Chromium (מותקן אוטומטית ע"י Playwright)

בדיקה:

python --version
pip --version

🐍 יצירת Virtual Environment (venv)

יש להריץ פעם אחת בלבד, מתוך תיקיית הפרויקט:

python -m venv venv

▶️ הפעלת ה־venv
Windows
venv\Scripts\activate


לאחר ההפעלה אמור להופיע:

(venv)

macOS / Linux
source venv/bin/activate

📦 התקנת תלויות

לאחר הפעלת ה־venv:

pip install playwright pytest allure-pytest


התקנת דפדפנים של Playwright:

playwright install

▶️ איך מריצים את הטסטים

הרצה של כל הטסטים:

pytest -s


הרצת טסט ספציפי:

pytest tests/test_e2e_flow.py -s

🏗️ ארכיטקטורת הפרויקט (בקצרה)

הפרויקט בנוי לפי Page Object Model (POM):

automation-ebay/
│
├── pages/
│   ├── base_page.py      # פונקציונליות משותפת (open, wait, human_wait וכו')
│   ├── search_page.py    # לוגיקת חיפוש וסינון
│   ├── item_page.py      # עמוד מוצר (בחירת וריאנטים, Add to Cart)
│   └── cart_page.py      # עגלת קניות ובדיקות סכומים
│
├── tests/
│   └── test_e2e_flow.py  # תרחיש E2E מלא
│
├── utils/
│   └── price_parser.py  # פירוק מחירים מטקסט
│
├── data/
│   └── test_data.json   # נתוני בדיקה (שאילתות, מחירים, מגבלות)
│
├── screenshots/         # צילומי מסך בזמן הרצה
├── venv/                # סביבת Python וירטואלית
└── README.md

automation-ebay/
│
├── pages/
│   ├── base_page.py
│   ├── search_page.py
│   ├── item_page.py
│   ├── cart_page.py
│
├── selectors/
│   ├── cart_selectors.py
│   ├── item_selectors.py
│   ├── search_selectors.py
│   ├── common_selectors.py
│
├── tests/
│   └── test_e2e_flow.py
│
├── utils/



🔄 תרחיש הבדיקה (Flow)

פתיחת אתר eBay

חיפוש מוצר לפי שאילתה

סינון לפי מחיר מינימלי ומקסימלי

מעבר על תוצאות החיפוש

כניסה לעמודי מוצר

בחירת וריאנטים (Size / Color וכו') אם קיימים

הוספה לעגלה

מעבר לעגלה

בדיקת סכום כולל מול מגבלת מחיר

⚠️ מגבלות והנחות

❌ אין התחברות (LOGIN)
הבדיקה מתבצעת כ־Guest User בלבד

🤖 CAPTCHA

אין ניסיון לעקוף CAPTCHA

אם מופיע CAPTCHA – ההרצה ממתינה לפתרון ידני

🌍 מטבע

המטבע נקבע לפי אזור (למשל ILS / USD)

הפענוח מתבסס על חילוץ מספרים בלבד מהטקסט

🧪 Stub / Mock

אין שימוש ב־Mocks או Stubs ל־Backend

הבדיקה רצה על אתר אמיתי (Live Environment)

⚡ יציבות סלקטורים

הסלקטורים מבוססים על DOM של eBay

שינוי באתר עלול לשבור בדיקות

🧠 הערות חשובות

מומלץ להריץ עם headless=False לצורך דיבוג

זמני המתנה מינימליים לשמירה על מהירות ויציבות

שימוש ב־human_wait להפחתת זיהוי אוטומציה

✅ סיום

הפרויקט מיועד ללמידה, ניסוי ואוטומציה אמיתית בקנה מידה קטן–בינוני.
ניתן להרחבה בקלות לטסטים נוספים, התחברות משתמש, או הרצה ב־CI.

בהצלחה 🚀