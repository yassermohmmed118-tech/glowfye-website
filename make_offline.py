import pathlib, re, os, json, urllib.parse

# Build mapping from downloaded files
# We have assets.txt and we know download logic, but let's build from existing files folder scans

# Read existing index.html original
orig_html = pathlib.Path("index.html").read_text(encoding='utf-8', errors='ignore')

# Build mapping of URL -> local relative path
mapping = {}

# From js, css
css_file = pathlib.Path("css/glowfye.webflow.shared.025b3c252.css")
if css_file.exists():
    mapping["https://cdn.prod.website-files.com/67c6b5d07ed6d0236f35b3ea/css/glowfye.webflow.shared.025b3c252.css"] = "css/glowfye.webflow.shared.025b3c252.css"

# js mappings
js_files = {
 "https://d3e54v103j8qbb.cloudfront.net/js/jquery-3.5.1.min.dc5e7f18c8.js?site=67c6b5d07ed6d0236f35b3ea": "js/jquery-3.5.1.min.dc5e7f18c8.js",
 "https://cdn.prod.website-files.com/67c6b5d07ed6d0236f35b3ea/js/webflow.schunk.26493d4beaa9dff2.js": "js/webflow.schunk.26493d4beaa9dff2.js",
 "https://cdn.prod.website-files.com/67c6b5d07ed6d0236f35b3ea/js/webflow.schunk.2b34912ad28f070d.js": "js/webflow.schunk.2b34912ad28f070d.js",
 "https://cdn.prod.website-files.com/67c6b5d07ed6d0236f35b3ea/js/webflow.6d825c9e.c500fdcc315afc5b.js": "js/webflow.6d825c9e.c500fdcc315afc5b.js",
 "https://ajax.googleapis.com/ajax/libs/webfont/1.6.26/webfont.js": "js/webfont.js",
}

for k,v in js_files.items():
    mapping[k]=v

# Image mappings: scan images folder and try to map by original filename endings
# We will replace any occurrence of https://cdn.prod.website-files.com/.../filename with images/filename local
# For that we need list of image files
images_dir = pathlib.Path("images")
image_files = list(images_dir.iterdir())
# create lookup by decoded tail
lookup={}
for img_path in image_files:
    name=img_path.name
    lookup[name]=f"images/{name}"
    # also lookup without spaces encoding?
    # For avif with spaces, encoded version will have %20
    # We'll handle via replacement later

# videos
videos_dir = pathlib.Path("videos")
if videos_dir.exists():
    for v in videos_dir.iterdir():
        lookup[v.name]=f"videos/{v.name}"

# Build generic replacement function
def offline_replace(html):
    # replace known exact mappings first
    for url, local in mapping.items():
        html = html.replace(url, local)
    # replace any cdn url that contains a known local filename
    # Find all cdn urls in html
    pattern = r'https://cdn\.prod\.website-files\.com[^\s"\'\)]+'
    def repl_match(m):
        url=m.group(0)
        # decode filename
        parsed = urllib.parse.urlparse(url)
        fname = urllib.parse.unquote(os.path.basename(parsed.path)).split("?")[0].split('"')[0].split(",")[0]
        fname = fname.strip()
        # try to find this file in lookup
        # Also try unquote and stripped
        if fname in lookup:
            return lookup[fname]
        # try finding by partial
        for key in lookup:
            if fname in key or key in fname:
                return lookup[key]
        # if poster jpg encoded %2F case
        if "%2F" in url:
            # video poster
            if "poster-00001.jpg" in url:
                # look for poster jpg
                for k in lookup:
                    if "poster" in k and k.endswith(".jpg"):
                        return lookup[k]
            if "transcode.mp4" in url:
                for k in lookup:
                    if k.endswith(".mp4") and "Skincare" in k:
                        return lookup[k]
            if "transcode.webm" in url:
                for k in lookup:
                    if k.endswith(".webm") and "Skincare" in k:
                        return lookup[k]
        # fallback keep original? but for offline we keep remote? We'll return local if possible else keep
        return url
    html = re.sub(pattern, repl_match, html)
    # replace cloudfront jquery
    html = re.sub(r'https://d3e54v103j8qbb\.cloudfront\.net/js/jquery[^\s"\'\)]+', 'js/jquery-3.5.1.min.dc5e7f18c8.js', html)
    # also fix srcset with p-500 etc which we already map via filename lookup should work
    return html

offline_html = offline_replace(orig_html)

# Write offline file
pathlib.Path("index_offline.html").write_text(offline_html, encoding='utf-8')
print("Created index_offline.html", len(offline_html))

# Also create a combined html with inline css? Maybe not needed

# Create css offline patch - replace font urls with local
css_path = pathlib.Path("css/glowfye.webflow.shared.025b3c252.css")
if css_path.exists():
    css_text = css_path.read_text(errors='ignore')
    # mapping fonts
    fonts_dir = pathlib.Path("fonts")
    font_lookup={}
    for f in fonts_dir.iterdir():
        font_lookup[f.name]=f"../fonts/{f.name}"  # from css to fonts is ../fonts
        # also encoded variants
        # map by bare name
    # replace https://.../font.ttf with ../fonts/...
    def css_repl(m):
        url=m.group(0)
        # extract fname
        parsed = urllib.parse.urlparse(url)
        fname = urllib.parse.unquote(os.path.basename(parsed.path)).split("?")[0]
        fname_clean = fname.split('"')[0].split("'")[0]
        for local_name, local_path in font_lookup.items():
            if fname_clean in local_name or local_name in fname_clean:
                return local_path
        # images in css
        for img_name, img_local in lookup.items():
            if fname_clean in img_name:
                # from css folder: ../images/...
                return img_local.replace("images/","../images/")
        return url
    # find urls
    pattern_css = r'https://[^\s"\'\)]+\.(?:ttf|woff|woff2|otf|svg|png|webp|avif|jpg|jpeg)'
    css_text_new = re.sub(pattern_css, css_repl, css_text)
    pathlib.Path("css/glowfye.webflow.shared.025b3c252.offline.css").write_text(css_text_new, encoding='utf-8')
    print("Created offline css")
    # also update offline html to use offline css
    offline_html2 = offline_html.replace("css/glowfye.webflow.shared.025b3c252.css","css/glowfye.webflow.shared.025b3c252.offline.css")
    pathlib.Path("index_offline.html").write_text(offline_html2, encoding='utf-8')

# Write mapping json
with open("url_mapping.json","w",encoding='utf-8') as f:
    json.dump({"exact":mapping,"lookup":lookup}, f, ensure_ascii=False, indent=2)

print("Done")
