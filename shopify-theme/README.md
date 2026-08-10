# Glowfye - Shopify Theme
Converted from Webflow template https://glowfye.webflow.io/home-v1

## What's Included

**Shopify OS 2.0 Theme - Ready to Upload**

### Structure:
- `layout/theme.liquid` - Main layout with CSS/JS, header, footer
- `templates/` - index.json, product.json, collection.json, page.json, cart.json, blog.json, etc.
- `sections/` - 13 sections:
  - header.liquid (navbar with Home, Shop, Categories, Blog, Contact, Pages dropdown)
  - hero.liquid (main hero with botanicals)
  - features.liquid (Purely Botanical, Safe & Clean, Dermatologist, Sustainable)
  - featured-products.liquid (Shopify collection loop + fallback static)
  - featured-in.liquid (logos: Glamour Awards, Cosmetic Awards)
  - our-values.liquid (Discover Difference)
  - shop-by-category.liquid (Beauty Tools, Makeover, Fragrance, Nail, Hair, Skin)
  - latest-blogs.liquid (Shopify blog loop)
  - follow-us.liquid (Instagram, Facebook, LinkedIn, YouTube ticker)
  - footer.liquid
  - main-product, main-collection, main-page, main-cart, main-blog, main-article, main-404, main-search
- `assets/` - 189 files (19MB):
  - CSS: glowfye.webflow.shared.025b3c252.css
  - JS: jquery, webflow chunks, webfont
  - Images: 145+ images (hero, products, categories, blogs, icons, logos) - safe names without spaces
  - Fonts: GeneralSans, Fraunces, Outfit, Inter
  - Videos: Skincare beauty mp4/webm
- `config/` - settings_schema.json, settings_data.json
- `locales/` - en.default.json

### Features Converted:
- ✅ No more sales-cta_wrap (Buy/Customize It/Figba buttons removed)
- ✅ No Made in Webflow badge
- ✅ Navbar: Home Pages dropdown replaced with single Home link
- ✅ Pages dropdown cleaned: Home V1/V2/V3 removed, only Home
- ✅ All images local, no CDN dependency
- ✅ Shopify Liquid for products, collections, cart, blogs
- ✅ Responsive, Webflow animations kept

### Installation on Shopify:

1. Go to Shopify Admin > Online Store > Themes
2. Click "Add theme" > "Upload zip"
3. Select `glowfye-shopify-theme.zip` (or `shopify-glowfye.zip`)
4. Wait for upload, then click "Publish" or "Customize"

### Customization:

- In Shopify Theme Editor, you can edit sections: Hero text, Featured Products collection, etc.
- Replace placeholder images with your own products via Shopify Admin
- Collections: Create collections named Beauty Tools, Makeover, Fragrance, etc. to match categories
- Blogs: Create blog named "news" for Latest Blogs section

### Notes:

- This is a conversion from Webflow to Shopify. Some Webflow interactions may need adjustment.
- Original template by Flowfye: https://webflow.com/templates/html/glowfye-website-template
- Converted for educational/personal use

### Live Demo (Vercel version before Shopify conversion):
https://glowfye-site.vercel.app

---
Made with Arena AI Agent
