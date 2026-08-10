import pathlib, re, urllib.parse, requests, os
from concurrent.futures import ThreadPoolExecutor, as_completed

# Gather all html files
html_files = list(pathlib.Path("pages").glob("*.html")) + [pathlib.Path("index.html")]
all_txt = ""
for f in html_files:
    try:
        all_txt += f.read_text(errors='ignore') + "\n"
    except:
        pass

# Find all https urls
pattern = r'https://[^\s"\'<>\)]+'
urls = re.findall(pattern, all_txt)
# clean
cleaned=set()
for u in urls:
    u=u.rstrip(').,;"\'')
    # filter cdn relevant
    if any(x in u for x in ["website-files.com","cloudfront.net"]):
        # skip preconnect base without file
        if u in ["https://cdn.prod.website-files.com"]:
            continue
        # remove encoded query weirdness but keep
        cleaned.add(u)

print(f"Found {len(cleaned)} total CDN urls from all pages")

existing = set()
# list existing images files sizes
for root, dirs, files in os.walk("."):
    for f in files:
        existing.add(f)

# try to find new ones not yet downloaded
to_download=[]
for url in cleaned:
    parsed=urllib.parse.urlparse(url)
    fname=urllib.parse.unquote(os.path.basename(parsed.path)).split("?")[0].split('"')[0].split(",")[0]
    fname=fname.strip()
    if not fname:
        continue
    # check if we already have a file containing this name approx
    if len(fname)<3:
        continue
    # search if fname already in filesystem (case insensitive)
    found=False
    for root, dirs, files in os.walk("."):
        for ef in files:
            if fname in ef or ef in fname:
                found=True
                break
        if found:
            break
    if not found:
        to_download.append(url)

print(f"Need to download {len(to_download)} new assets")
# dedup
to_download=list(set(to_download))
print(to_download[:100])

# download
def dl(url):
    try:
        # handle names with spaces and parentheses
        parsed=urllib.parse.urlparse(url)
        fname=urllib.parse.unquote(os.path.basename(parsed.path)).split("?")[0]
        fname=fname.split('"')[0].split(",")[0].strip()
        if not fname or len(fname)>120:
            # fallback
            fname = "asset_" + str(abs(hash(url)))[:8] + "." + (parsed.path.split(".")[-1][:4] if "." in parsed.path else "bin")
        # decide folder
        ext = fname.split(".")[-1].lower()
        if ext in ["css"]:
            folder="css"
        elif ext in ["js"]:
            folder="js"
        elif ext in ["mp4","webm"]:
            folder="videos"
        elif ext in ["woff","woff2","ttf","otf"]:
            folder="fonts"
        elif ext in ["svg","png","jpg","jpeg","webp","avif","gif"]:
            folder="images"
        else:
            folder="images"
        local=os.path.join(folder, fname)
        if os.path.exists(local) and os.path.getsize(local)>0:
            return f"skip {local}"
        headers={"User-Agent":"Mozilla/5.0"}
        r=requests.get(url, headers=headers, timeout=20, stream=True)
        if r.status_code==200:
            pathlib.Path(folder).mkdir(exist_ok=True)
            with open(local,"wb") as f:
                for chunk in r.iter_content(8192):
                    f.write(chunk)
            return f"ok {url} -> {local} {r.headers.get('content-length','')}"
        else:
            return f"fail {url} {r.status_code}"
    except Exception as e:
        return f"error {url} {e}"

import concurrent.futures
with ThreadPoolExecutor(max_workers=12) as ex:
    futures=[ex.submit(dl, u) for u in to_download]
    for fut in as_completed(futures):
        print(fut.result())

