import requests, pathlib, re, time, os
base = "https://glowfye.webflow.io"
pages = ['home-v1','home-v2','home-v3','shop','categories','our-story','faq','blogs','contact','checkout','privacy-policy','404','utilities/style-guides','utilities/licenses','utilities/changelog','category/beauty-tools','category/makeover','category/fragrance','category/nail-care','category/hair-care','category/skin-care','product/hair-growth-serum','product/anti-aging-serum','product/brightening-eye-cream','blog/5-pro-tips-for-glowing-skin','blog/guide-to-long-gorgeous-hair','blog/tips-for-stunning-nails']

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

for p in pages:
    url = f"{base}/{p}"
    safe_name = p.replace("/","__") + ".html"
    path = pathlib.Path("pages") / safe_name
    if path.exists() and path.stat().st_size>1000:
        print(f"skip {p} exists")
        continue
    try:
        print(f"Downloading {url}...")
        r=requests.get(url, headers=headers, timeout=15)
        print(f"  -> {r.status_code} {len(r.text)}")
        if r.status_code==200:
            path.write_text(r.text, encoding='utf-8')
        else:
            print(f"  failed {p}")
        time.sleep(0.5)
    except Exception as e:
        print(f"Error {p}: {e}")

print("Done pages")

# Also try to create offline version of index.html
# Build mapping from CDN urls to local files for offline use
