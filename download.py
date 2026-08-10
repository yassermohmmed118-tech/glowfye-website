import os, requests, pathlib, re, urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed

assets_file = "assets.txt"
urls = [line.strip() for line in open(assets_file) if line.strip()]

# function to get local filename
def get_local_path(url):
    # Remove query string for path determination
    parsed = urllib.parse.urlparse(url)
    # get filename
    path = parsed.path
    fname = os.path.basename(path)
    # decode
    fname = urllib.parse.unquote(fname)
    if not fname or len(fname) < 2:
        fname = "file_" + str(abs(hash(url)))[:8]
    # sanitize query char like ?site=
    if "?site=" in url:
        # keep base
        pass
    # Choose folder
    ext = fname.split('.')[-1].lower() if '.' in fname else ''
    if ext in ['css']:
        folder = "css"
    elif ext in ['js']:
        folder = "js"
    elif ext in ['avif','webp','png','jpg','jpeg','avif','svg','gif']:
        folder = "images"
    elif ext in ['mp4','webm']:
        folder = "videos"
    elif ext in ['woff','woff2','ttf','otf','eot']:
        folder = "fonts"
    else:
        # infer by url path
        if "/css/" in url:
            folder="css"
        elif "/js/" in url:
            folder="js"
        elif "image" in url.lower() or "thumbnail" in url.lower() or "logo" in url.lower() or "hero" in url.lower() or "fab" in url.lower() or "webclip" in url.lower() or "ellipse" in url.lower():
            folder="images"
        else:
            folder="images"
    # handle encoded slashes
    if "%2F" in url:
        # video case with poster
        if "poster" in url:
            folder="images"
            # extract last part after %2F
            try:
                encoded_part = url.split("%2F")[-1]
                encoded_part = encoded_part.split("-poster")[0] + "_poster.jpg" if "poster" in url else encoded_part
                fname = urllib.parse.unquote(encoded_part.split('"')[0].split(',')[0])
            except:
                pass
        if "transcode" in url:
            folder="videos"
            try:
                # get actual file extension
                if ".mp4" in url:
                    fname = url.split("%2F")[-1].split(",")[0].split('"')[0]
                    fname = urllib.parse.unquote(fname)
                elif ".webm" in url:
                    fname = url.split("%2F")[-1].split(",")[0].split('"')[0]
                    fname = urllib.parse.unquote(fname)
            except:
                pass
    # clean fname
    fname = fname.split("?")[0].split('"')[0].split(",")[0]
    fname = fname.strip()
    # avoid very long
    if len(fname) > 100:
        fname = fname[-100:]
    # avoid empty
    if not fname:
        fname = f"file_{abs(hash(url))}.bin"
    return os.path.join(folder, fname), url

tasks = [get_local_path(u) for u in urls]

# dedup by local path
dedup = {}
for local, orig in tasks:
    dedup[local] = orig

print(f"Downloading {len(dedup)} files...")

def download_one(item):
    local, url_orig = item
    # url_orig may contain , separating multiple urls in one malformed case
    # split by comma if contains ,https
    sub_urls = url_orig.split(",")
    results=[]
    for url in sub_urls:
        url=url.strip()
        if not url.startswith("http"):
            continue
        # ensure local path unique per sub
        if len(sub_urls)>1:
            parsed=urllib.parse.urlparse(url)
            fname=os.path.basename(parsed.path)
            fname=urllib.parse.unquote(fname).split("?")[0]
            local_path=os.path.join(os.path.dirname(local), fname)
        else:
            local_path=local
        # if exists skip
        if os.path.exists(local_path) and os.path.getsize(local_path)>0:
            results.append((url, local_path, "skip"))
            continue
        try:
            headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
            r=requests.get(url, headers=headers, timeout=15, stream=True)
            if r.status_code==200:
                pathlib.Path(os.path.dirname(local_path)).mkdir(parents=True, exist_ok=True)
                with open(local_path, "wb") as f:
                    for chunk in r.iter_content(8192):
                        f.write(chunk)
                results.append((url, local_path, f"ok {r.headers.get('content-length','')}"))
            else:
                results.append((url, local_path, f"fail {r.status_code}"))
        except Exception as e:
            results.append((url, local_path, f"error {e}"))
    return results

all_results=[]
with ThreadPoolExecutor(max_workers=10) as ex:
    futures=[ex.submit(download_one, item) for item in dedup.items()]
    for fut in as_completed(futures):
        res=fut.result()
        for r in res:
            print(r)
            all_results.append(r)

# Also download CSS and parse for more urls
css_files = [p for p in pathlib.Path("css").glob("*.css")] if pathlib.Path("css").exists() else []
extra_urls=set()
for css in css_files:
    try:
        txt=css.read_text(errors='ignore')
        # find url(...) 
        matches=re.findall(r'url\(([^\)]+)\)', txt)
        for m in matches:
            m=m.strip(' "\'')
            if m.startswith("http"):
                extra_urls.add(m)
    except:
        pass
print(f"Extra from CSS: {extra_urls}")
if extra_urls:
    open("extra_css_assets.txt","w").write("\n".join(extra_urls))
    # download them
    for url in extra_urls:
        try:
            parsed=urllib.parse.urlparse(url)
            fname=os.path.basename(parsed.path).split("?")[0]
            fname=urllib.parse.unquote(fname)
            if not fname:
                fname="font_"+str(abs(hash(url)))[:6]+".woff2"
            folder="css" if fname.endswith(".css") else "fonts" if any(x in fname for x in ["woff","ttf"]) else "images"
            local_path=os.path.join(folder, fname)
            if os.path.exists(local_path):
                continue
            headers={"User-Agent":"Mozilla/5.0"}
            r=requests.get(url, headers=headers, timeout=15, stream=True)
            if r.status_code==200:
                pathlib.Path(folder).mkdir(exist_ok=True)
                with open(local_path, "wb") as f:
                    for chunk in r.iter_content(8192):
                        f.write(chunk)
                print(f"Downloaded extra {url} -> {local_path}")
            else:
                print(f"Failed extra {url} {r.status_code}")
        except Exception as e:
            print(f"Error extra {url}: {e}")

print("Done")
