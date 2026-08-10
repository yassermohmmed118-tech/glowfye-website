# Glowfye - Skincare Ecommerce Template

Converted from Webflow template [Glowfye](https://glowfye.webflow.io/home-v1) to static site, Vercel, Shopify & GitHub.

**Live Demos:**
- Vercel (Fixed Version): https://glowfye-site.vercel.app
- Original Webflow: https://glowfye.webflow.io/home-v1
- Shopify Store (Demo): https://yt6jmn-n7.myshopify.com/ (password protected)

## 📁 Repository Structure

```
glowfye-github/
├── index.html                 # Main homepage (fixed, no badges, Home instead of Home Pages)
├── css/                       # Stylesheets (Webflow shared CSS)
├── js/                        # jQuery + Webflow JS chunks
├── images/                    # 145+ images (AVIF, WEBP, SVG, PNG) - safe names
├── fonts/                     # 9 fonts (GeneralSans, Fraunces, Inter, Outfit)
├── videos/                    # Background videos MP4/WEBM
├── pages/                     # 27 pages (home-v2, home-v3, shop, categories, etc.)
├── shopify-theme/             # Complete Shopify OS 2.0 theme (ready to upload)
│   ├── layout/theme.liquid
│   ├── templates/index.json
│   ├── sections/ (13 sections)
│   ├── assets/ (189 files)
│   ├── config/
│   └── locales/
├── original-backup/           # Original pages & README
├── vercel.json                # Vercel config
└── README.md
```

## 🚀 Features Fixed

- ✅ Removed `sales-cta_wrap` (Buy, Customize It, Figma buttons) bottom-right/left rectangles
- ✅ Removed `Made in Webflow` badge via CSS
- ✅ Replaced `Home Pages` dropdown with single `Home` link
- ✅ Cleaned `Pages` dropdown: Removed Home V1/V2/V3, added Home
- ✅ Fixed image names (removed spaces & parentheses): `blog image (1).avif` → `blog_image_1.avif`
- ✅ Removed integrity attributes that blocked CSS on Vercel/Shopify
- ✅ All images local, no CDN dependency
- ✅ Shopify theme ready (189 assets, 14MB zip)

## 🌐 Deployment

### Vercel
```bash
vercel --prod
```
Live: https://glowfye-site.vercel.app

### Shopify
1. Zip the `shopify-theme` folder contents (not the folder itself)
2. Go to Shopify Admin > Themes > Add theme > Upload zip
3. Select `glowfye-shopify-direct.zip`

### GitHub Pages
1. Enable GitHub Pages in repo settings
2. Source: main branch / root
3. Your site will be live at `https://username.github.io/repo-name/`

## 🛠️ Tech Stack

- Webflow Ecommerce Template by Flowfye
- jQuery 3.5.1
- Webflow.js
- Shopify OS 2.0 Liquid
- Fonts: GeneralSans, Fraunces 72pt, Inter, Outfit, Open Sans

## 📄 License
Original template: https://webflow.com/templates/html/glowfye-website-template
Converted for educational/personal use.

---
Created with Arena AI Agent
