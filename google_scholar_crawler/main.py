"""Fetch Google Scholar citation stats through SerpApi's Google Scholar Author API.

Writes two files into ./results, in the formats the homepage already reads:
  - gs_data_shieldsio.json  -> the "Citations" highlight card (and shields.io badges)
  - gs_data.json            -> the template's own stats script (total + per-paper counts)

Environment variables (set as GitHub Actions secrets):
  GOOGLE_SCHOLAR_ID  e.g. dnH7e-QAAAAJ
  SERPAPI_KEY        your SerpApi API key

Uses only the Python standard library. Exits non-zero (and writes nothing) on any
error, so the last good data on the google-scholar-stats branch is kept.
"""
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone

API_URL = "https://serpapi.com/search.json"


def fail(msg):
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


def fetch_author(author_id, api_key):
    params = {
        "engine": "google_scholar_author",
        "author_id": author_id,
        "hl": "en",      # English keys in the citation table
        "num": "100",    # up to 100 articles in a single request (counts as 1 search)
        "api_key": api_key,
    }
    url = API_URL + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": "academic-homepage-citations/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = json.load(resp)
    except urllib.error.HTTPError as e:
        try:
            detail = json.load(e).get("error", "")
        except Exception:
            detail = ""
        fail(f"SerpApi returned HTTP {e.code}. {detail}".strip())
    except urllib.error.URLError as e:
        fail(f"Could not reach SerpApi: {e.reason}")

    if data.get("error"):
        fail(f"SerpApi error: {data['error']}")
    status = (data.get("search_metadata") or {}).get("status")
    if status and status != "Success":
        fail(f"SerpApi search status: {status}")
    return data


def table_value(table, names):
    """Return the 'all' value of the first cited_by.table row whose key is in names."""
    for row in table or []:
        for key, cols in row.items():
            if key in names and isinstance(cols, dict) and "all" in cols:
                return cols["all"]
    return None


def main():
    author_id = os.environ.get("GOOGLE_SCHOLAR_ID", "").strip()
    api_key = os.environ.get("SERPAPI_KEY", "").strip()
    if not author_id:
        fail("GOOGLE_SCHOLAR_ID is not set. Add it under Settings > Secrets and variables > Actions.")
    if not api_key:
        fail("SERPAPI_KEY is not set. Add it under Settings > Secrets and variables > Actions.")

    data = fetch_author(author_id, api_key)
    table = (data.get("cited_by") or {}).get("table")
    citations = table_value(table, {"citations"})
    if citations is None:
        fail("Response has no cited_by.table citations value; the profile may be private or the ID wrong.")

    publications = {}
    for art in data.get("articles") or []:
        cid = art.get("citation_id")
        if not cid:
            continue
        publications[cid] = {
            "title": art.get("title"),
            "pub_year": art.get("year"),
            "num_citations": ((art.get("cited_by") or {}).get("value")) or 0,
        }

    author = data.get("author") or {}
    gs_data = {
        "name": author.get("name"),
        "affiliations": author.get("affiliations"),
        "citedby": citations,
        "hindex": table_value(table, {"h_index"}),
        "i10index": table_value(table, {"i10_index"}),
        "updated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "source": "SerpApi Google Scholar Author API",
        "publications": publications,
    }
    shields = {"schemaVersion": 1, "label": "citations", "message": str(citations)}

    os.makedirs("results", exist_ok=True)
    with open("results/gs_data.json", "w", encoding="utf-8") as f:
        json.dump(gs_data, f, ensure_ascii=False, indent=1)
    with open("results/gs_data_shieldsio.json", "w", encoding="utf-8") as f:
        json.dump(shields, f, ensure_ascii=False)

    print(f"OK: {gs_data['name']} has {citations} citations "
          f"(h-index {gs_data['hindex']}, {len(publications)} articles).")


if __name__ == "__main__":
    main()
