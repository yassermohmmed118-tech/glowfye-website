# Glowfye - تحميل موقع Webflow

تم تحميل موقع **https://glowfye.webflow.io/home-v1** بالكامل بتاريخ اليوم.

## محتويات المجلد

```
glowfye_site/
├── index.html                  # النسخة الأصلية من الصفحة الرئيسية (home-v1)
├── index_offline.html          # نسخة تعمل Offline بالملفات المحلية
├── assets.txt                  # قائمة روابط الـ CDN
├── pages/                      # جميع صفحات الموقع (27 صفحة)
│   ├── home-v1.html
│   ├── home-v2.html
│   ├── home-v3.html
│   ├── shop.html
│   ├── categories.html
│   ├── our-story.html
│   ├── faq.html
│   ├── blogs.html
│   ├── contact.html
│   ├── checkout.html
│   ├── privacy-policy.html
│   ├── 404.html
│   ├── utilities__changelog.html
│   ├── utilities__licenses.html
│   ├── utilities__style-guides.html
│   ├── category__beauty-tools.html
│   ├── category__makeover.html
│   ├── category__fragrance.html
│   ├── category__nail-care.html
│   ├── category__hair-care.html
│   ├── category__skin-care.html
│   ├── product__hair-growth-serum.html
│   ├── product__anti-aging-serum.html
│   ├── product__brightening-eye-cream.html
│   ├── blog__5-pro-tips-for-glowing-skin.html
│   ├── blog__guide-to-long-gorgeous-hair.html
│   └── blog__tips-for-stunning-nails.html
├── css/
│   ├── glowfye.webflow.shared.025b3c252.css          # ملف الستايل الأساسي من Webflow
│   └── glowfye.webflow.shared.025b3c252.offline.css  # نسخة Offline تشير للملفات المحلية
├── js/
│   ├── jquery-3.5.1.min.dc5e7f18c8.js
│   ├── webfont.js
│   ├── webflow.schunk.26493d4beaa9dff2.js
│   ├── webflow.schunk.2b34912ad28f070d.js
│   ├── webflow.6d825c9e.c500fdcc315afc5b.js
│   └── webflow.*.js (صفحات أخرى)
├── images/                     # جميع الصور (SVG, PNG, WEBP, AVIF)
│   ├── hero main image
│   ├── ingredients, logos, categories
│   ├── product images
│   ├── blog images
│   └── icons & visuals
├── fonts/                      # الخطوط المستخدمة
│   ├── GeneralSans-Variable
│   ├── Fraunces-Variable
│   ├── Outfit
│   ├── Inter-Variable
│   └── Fraunces 72pt Regular
├── videos/                     # فيديوهات الخلفية
│   ├── Skincare Beauty transcode mp4
│   └── Skincare Beauty transcode webm
└── url_mapping.json            # خريطة الروابط الأصلية للمحلية
```

## كيفية الاستخدام

### 1. النسخة الأصلية
افتح `index.html` سيعمل مباشرة لكنه سيطلب الصور من CDN الخارجي.

### 2. النسخة Offline الكاملة
افتح `index_offline.html` - تم تعديله ليشير إلى المجلدات المحلية:
- `css/` للستايل
- `js/` للسكريبتات
- `images/` للصور
- `fonts/` للخطوط

### 3. باقي الصفحات
مجلد `pages/` يحتوي كل صفحات الموقع، يمكنك ربطها ببعض.

## التقنيات المستخدمة
- Webflow Ecommerce Template
- jQuery 3.5.1
- Webflow.js chunks
- Fonts: GeneralSans, Fraunces, Inter, Outfit, Open Sans (Google Fonts)
- CDN: cdn.prod.website-files.com و cloudfront.net

## ملاحظات
- جميع الصور عالية الجودة تم تحميلها بأحجام متعددة (p-500, p-800, p-1080, p-1600, p-2000, p-2600, original)
- تم حفظ الفيديوهات بصيغتين mp4 و webm لتوافق المتصفحات
- بعض ملفات `blog image (4)..(7)` كانت محمية 403 من Webflow ولم يتم تحميلها لأنها غير موجودة في home-v1 الأصلية بل في صفحة blogs
- الموقع هو قالب تجاري لـ Webflow لعلامات تجميل وعناية بالبشرة

## الحقوق
القالب الأصلي من Flowfye - https://webflow.com/templates/html/glowfye-website-template
الغرض التعليمي والشخصي فقط.

---
تم التحميل بواسطة Arena AI Agent
