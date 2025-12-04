# إعداد OAuth 2.0 للـ DME Equipment Docs

## المشكلة السابقة 🔴

عند استخدام **Service Account**، كانت المشكلة:
- Service Account عندها **0 GB storage quota**
- Google Docs كانت بتحسب على الـ quota بتاعتها
- Error: "storage quota exceeded" ❌

## الحل الجديد ✅

استخدام **حسابك الشخصي** (OAuth 2.0) بدل Service Account:
- عندك **15 GB مجانية**
- Google Docs **مالهاش حد**
- هتشتغل زي ما كانت بتشتغل locally! 🎉

---

## خطوات التفعيل

### 1️⃣ إنشاء OAuth Credentials في Google Cloud

1. افتح: https://console.cloud.google.com/apis/credentials
2. اختار مشروعك: **dme-equipment-docs**
3. اضغط **+ CREATE CREDENTIALS**
4. اختار **OAuth client ID**
5. Application type: **Desktop app**
6. Name: أي اسم (مثلاً: "DME Desktop Client")
7. اضغط **CREATE**
8. اضغط **DOWNLOAD JSON**
9. احفظ الملف باسم **credentials.json**

---

### 2️⃣ تشغيل السكريبت على جهازك

1. حط ملف `credentials.json` في مجلد المشروع
2. افتح Terminal وشغل:

```bash
python generate_oauth_token.py
```

3. هيفتح متصفح تلقائياً
4. سجل دخول بـ **حسابك** (heshamelhoseni25@gmail.com)
5. اضغط **Allow**
6. السكريبت هيطبع لك الـ OAuth credentials

---

### 3️⃣ تحديث Streamlit Secrets

1. روح على: https://share.streamlit.io
2. افتح app settings
3. افتح **Secrets**
4. **امسح** القسم القديم `[gcp_service_account]` كله
5. **الصق** القسم الجديد اللي طبعه السكريبت:

```toml
[google_oauth]
token = "ya29.a0..."
refresh_token = "1//0..."
token_uri = "https://oauth2.googleapis.com/token"
client_id = "xxx.apps.googleusercontent.com"
client_secret = "GOCSPX-xxx"
```

6. **خلي** باقي الـ secrets زي ما هي:
   - `GEMINI_API_KEY`
   - `FOLDER_ID`

7. اضغط **Save**

---

### 4️⃣ إعادة نشر التطبيق

1. اضغط **Reboot app** أو
2. عمل push جديد للـ repo

---

## التأكد من نجاح العملية ✅

بعد ما الـ app يشتغل:
- جرب ترفع صور
- اتأكد إن Google Docs بتتعمل على Drive بتاعك
- مش هيطلع error "storage quota exceeded" تاني! 🎉

---

## ملاحظات مهمة

### الأمان 🔒
- الـ `credentials.json` **لا ترفعها على GitHub** (في .gitignore)
- الـ `token.json` **لا ترفعها على GitHub** (في .gitignore)
- الـ OAuth tokens في Streamlit Secrets **آمنة ومش ظاهرة لحد**

### الصلاحيات
- متأكد إن الـ folder على Drive **مشارك مع حسابك** (وهو أصلاً بتاعك!)
- لو غيرت الـ FOLDER_ID، اتأكد إن الحساب عنده صلاحية

---

## مشاكل محتملة

### ❌ "credentials.json not found"
**الحل:** حط ملف credentials.json في مجلد المشروع

### ❌ "Invalid grant" error
**الحل:** امسح `token.json` وشغل `generate_oauth_token.py` تاني

### ❌ "Access blocked: This app's request is invalid"
**الحل:** اتأكد إنك ضفت الـ Scopes الصحيحة في Google Cloud Console:
- `https://www.googleapis.com/auth/documents`
- `https://www.googleapis.com/auth/drive`

---

## هل نجحت؟ 🎉

لو اتبعت الخطوات دي، التطبيق هيشتغل بـ **حسابك الشخصي** وهيقدر ينشئ Google Docs براحته!

---

**أي مشاكل؟ راجع الخطوات أو اسأل!**
