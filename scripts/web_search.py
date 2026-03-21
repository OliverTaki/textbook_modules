"""
web_search.py — Librarian 役が使うウェブ検索・ページ取得ユーティリティ
- DuckDuckGo でキーワード検索
- Wikipedia（日本語）記事取得
- 一般ページのテキスト抽出
"""

import urllib.request, urllib.parse, urllib.error
import json, re, time
from pathlib import Path

HEADERS = {
    "User-Agent": (
        "KnowledgeMapBot/1.0 (https://github.com/OliverTaki/textbook_modules; "
        "educational research) Python-urllib/3"
    )
}
TIMEOUT = 15   # 秒

# ─────────────────────────────────────────────────────────────
def _fetch(url, timeout=TIMEOUT):
    """指定URLのHTMLを取得してテキストを返す。失敗時は空文字。"""
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read()
            enc = resp.headers.get_content_charset("utf-8")
            return raw.decode(enc, errors="replace")
    except Exception as e:
        return f"[FETCH ERROR] {e}"

def _strip_html(html):
    """HTMLタグと余分な空白を除去してプレーンテキストを返す。"""
    text = re.sub(r"<script[^>]*>.*?</script>", "", html, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r"<style[^>]*>.*?</style>",  "", text,  flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"&nbsp;",  " ", text)
    text = re.sub(r"&amp;",   "&", text)
    text = re.sub(r"&lt;",    "<", text)
    text = re.sub(r"&gt;",    ">", text)
    text = re.sub(r"&quot;",  '"', text)
    text = re.sub(r"\s{2,}",  "\n", text)
    return text.strip()

# ─────────────────────────────────────────────────────────────
def search_ddg(query, max_results=5):
    """
    DuckDuckGo HTML 検索。{title, url, snippet} のリストを返す。
    API キー不要。リクエスト過多を防ぐため 1 秒待機。
    """
    q = urllib.parse.quote_plus(query)
    url = f"https://html.duckduckgo.com/html/?q={q}&kl=jp-jp"
    html = _fetch(url)
    results = []
    # DDG HTML から <a class="result__a"> と <a class="result__snippet"> を抽出
    links    = re.findall(r'<a[^>]+class="result__a"[^>]*href="([^"]+)"[^>]*>(.*?)</a>', html, re.DOTALL)
    snippets = re.findall(r'class="result__snippet"[^>]*>(.*?)</a>', html, re.DOTALL)
    for i, (href, title) in enumerate(links[:max_results]):
        snippet = snippets[i] if i < len(snippets) else ""
        results.append({
            "title":   _strip_html(title).strip(),
            "url":     href,
            "snippet": _strip_html(snippet).strip()[:200]
        })
    time.sleep(1)
    return results

# ─────────────────────────────────────────────────────────────
def fetch_wikipedia_ja(topic, max_chars=8000):
    """
    日本語 Wikipedia の API で記事を取得する。
    extract（プレーンテキスト）を返す。見つからない場合は空文字。
    """
    q = urllib.parse.quote(topic)
    url = (
        f"https://ja.wikipedia.org/w/api.php"
        f"?action=query&prop=extracts&exintro=false&explaintext=true"
        f"&titles={q}&format=json&utf8=1&redirects=1"
    )
    html = _fetch(url)
    try:
        data  = json.loads(html)
        pages = data.get("query", {}).get("pages", {})
        for pid, page in pages.items():
            if pid == "-1":
                return ""
            return page.get("extract", "")[:max_chars]
    except Exception:
        return ""

# ─────────────────────────────────────────────────────────────
def fetch_page_text(url, max_chars=5000):
    """指定URLをフェッチしてプレーンテキスト（max_chars文字）を返す。"""
    html = _fetch(url)
    if html.startswith("[FETCH ERROR]"):
        return html
    return _strip_html(html)[:max_chars]

# ─────────────────────────────────────────────────────────────
def collect_references(module_id, title, ref_dir: Path, max_pages=3):
    """
    module_id / title に関連する参照資料を収集し ref_dir に保存する。
    INDEX.md を生成して返す。

    Parameters:
        module_id : モジュールID（例: ELM-001）
        title     : モジュールタイトル（日本語）
        ref_dir   : 保存先ディレクトリ（Path）
        max_pages : DDG 検索結果から取得する最大ページ数
    Returns:
        index_text (str): INDEX.md の内容
    """
    ref_dir.mkdir(parents=True, exist_ok=True)
    sources = []

    # 1. Wikipedia（日本語）
    wiki_text = fetch_wikipedia_ja(title)
    if wiki_text and len(wiki_text) > 100:
        path = ref_dir / "wikipedia.txt"
        path.write_text(wiki_text, encoding="utf-8")
        sources.append({
            "id": "WIKI-JA",
            "title": f"Wikipedia（日本語）: {title}",
            "url": f"https://ja.wikipedia.org/wiki/{urllib.parse.quote(title)}",
            "file": "wikipedia.txt",
            "license": "CC BY-SA 4.0",
            "chars": len(wiki_text)
        })

    # 2. DuckDuckGo 検索
    query = f"数学 {title} 解説 教材"
    results = search_ddg(query, max_results=max_pages + 2)
    saved = 0
    for i, r in enumerate(results):
        if saved >= max_pages:
            break
        if not r["url"].startswith("http"):
            continue
        text = fetch_page_text(r["url"])
        if text.startswith("[FETCH ERROR]") or len(text) < 100:
            continue
        fname = f"ref_{saved+1:02d}.txt"
        (ref_dir / fname).write_text(
            f"SOURCE: {r['url']}\nTITLE: {r['title']}\n\n{text}",
            encoding="utf-8"
        )
        sources.append({
            "id": f"DDG-{saved+1:02d}",
            "title": r["title"],
            "url": r["url"],
            "file": fname,
            "license": "unknown",
            "chars": len(text)
        })
        saved += 1
        time.sleep(1)

    # 3. INDEX.md を生成
    lines = [f"# References: {module_id} — {title}\n"]
    lines.append(f"収集日: {__import__('datetime').date.today()}\n\n")
    lines.append("| ID | タイトル | URL | ライセンス | 文字数 |\n")
    lines.append("|----|---------|----|-----------|-------|\n")
    for s in sources:
        lines.append(f"| {s['id']} | {s['title'][:40]} | {s['url'][:60]} | {s['license']} | {s['chars']} |\n")
    index_text = "".join(lines)
    (ref_dir / "INDEX.md").write_text(index_text, encoding="utf-8")
    return index_text, sources
