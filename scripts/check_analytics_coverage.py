"""Check every sitemap page for one working GoatCounter loader tag."""

import json
import sys
import urllib.request
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor


SITEMAP = "https://jiedianshouce.com/sitemap.xml"
TAG = b'data-goatcounter="/analytics/count"'
HEADERS = {"User-Agent": "NodeHandbookAnalyticsAudit/1.0"}


def fetch(url):
    request = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(request, timeout=15) as response:
        return response.status, response.read()


def check(url):
    try:
        status, body = fetch(url)
        count = body.count(TAG)
        return {"url": url, "status": status, "tracking_tags": count}
    except Exception as exc:
        return {"url": url, "status": 0, "tracking_tags": 0, "error": str(exc)}


def main():
    _, sitemap = fetch(SITEMAP)
    root = ET.fromstring(sitemap)
    urls = [element.text for element in root.findall(".//{*}loc") if element.text]
    with ThreadPoolExecutor(max_workers=8) as pool:
        results = list(pool.map(check, urls))
    failures = [item for item in results if item["status"] != 200 or item["tracking_tags"] != 1]
    print(json.dumps({"pages": len(results), "passing": len(results) - len(failures), "failures": failures}, ensure_ascii=False, indent=2))
    return 1 if failures or not results else 0


if __name__ == "__main__":
    sys.exit(main())
