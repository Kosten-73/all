import csv
import time
import random
from typing import List, Dict, Optional
from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup, FeatureNotFound

BASE = "https://books.toscrape.com/"
START_PAGES = [
    "catalogue/page-1.html",
    "catalogue/page-2.html",
    "catalogue/page-3.html",
    "catalogue/page-4.html",
    "catalogue/page-5.html",
]
OUTPUT_CSV = "книжки.csv"

HEADERS = {
    "User-Agent": "edu-scraper/1.0 (+https://your-university.example) - learning project"
}
MIN_DELAY = 1.0
MAX_DELAY = 2.5

RATING_MAP = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}


def polite_sleep():
    time.sleep(random.uniform(MIN_DELAY, MAX_DELAY))


def get_soup(url: str, session: requests.Session, timeout: int = 10) -> Optional[BeautifulSoup]:
    try:
        r = session.get(url, headers=HEADERS, timeout=timeout)
        r.raise_for_status()
    except requests.RequestException as e:
        print(f"[ОШИБКА] HTTP упал с ошибкой {url}: {e}")
        return None
    try:
        soup = BeautifulSoup(r.text, "lxml")
    except FeatureNotFound:
        soup = BeautifulSoup(r.text, "html.parser")
    return soup


def parse_book_article(article_tag, base_url) -> Dict:
    a = article_tag.select_one("h3 a")
    title = a.get("title", "").strip() if a else ""

    rel_href = a.get("href") if a else ""
    detail_url = urljoin(base_url, rel_href)

    img = article_tag.select_one(".image_container img")
    img_src = img.get("src") if img else ""
    image_url = urljoin(base_url, img_src)

    price_tag = article_tag.select_one("p.price_color")
    price_text = price_tag.get_text(strip=True) if price_tag else ""

    avail_tag = article_tag.select_one("p.instock.availability")
    availability = avail_tag.get_text(strip=True) if avail_tag else ""

    rating_tag = article_tag.select_one("p.star-rating")
    rating = None
    if rating_tag:
        classes = rating_tag.get("class", [])
        for c in classes:
            if c in RATING_MAP:
                rating = RATING_MAP[c]
                break
    return {
        "title": title,
        "price": price_text,
        "availability": availability,
        "rating": rating if rating is not None else "",
        "detail_page_url": detail_url,
        "image_url": image_url
    }


def scrape_pages(page_paths: List[str]) -> List[Dict]:
    session = requests.Session()
    results = []
    for rel in page_paths:
        page_url = urljoin(BASE, rel)
        print(f"[ИНФОРМАЦИЯ] обновляется {page_url}")
        soup = get_soup(page_url, session)
        if soup is None:
            print(f"[Предупреждение] Не удалось извлечь {page_url}, пропустим.")
            polite_sleep()
            continue

        articles = soup.select("article.product_pod")
        if not articles:
            print(
                f"[ПРЕДУПРЕЖДЕНИЕ] На странице {page_url} не найдено элементов product_pod — возможно, структура страницы изменилась.")
        for art in articles:
            try:
                item = parse_book_article(art, BASE)
                results.append(item)
            except Exception as e:
                print(f"[ОШИБКА] Не удалось разобрать статью в книге: {e}")
        polite_sleep()
    return results


def save_to_csv(items: List[Dict], filename: str):
    if not items:
        print("[ИНФОРМАЦИЯ] Нет элементов для сохранения.")
        return
    keys = ["title", "price", "availability", "rating", "detail_page_url", "image_url"]
    with open(filename, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        for it in items:
            writer.writerow(it)
    print(f"[ИНФОРМАЦИЯ] Сохраненные записи {len(items)} в {filename}")


if __name__ == "__main__":
    scraped = scrape_pages(START_PAGES)
    save_to_csv(scraped, OUTPUT_CSV)

# C:\Users\korudenko\PycharmProjects\botconfectioner\.venv2\Scripts\python.exe C:\Users\korudenko\PycharmProjects\Py3semestr2025RudenkoKTmo2-16\laba9\Task9-2.py
# [ИНФОРМАЦИЯ] обновляется https://books.toscrape.com/catalogue/page-1.html
# [ИНФОРМАЦИЯ] обновляется https://books.toscrape.com/catalogue/page-2.html
# [ИНФОРМАЦИЯ] обновляется https://books.toscrape.com/catalogue/page-3.html
# [ИНФОРМАЦИЯ] обновляется https://books.toscrape.com/catalogue/page-4.html
# [ИНФОРМАЦИЯ] обновляется https://books.toscrape.com/catalogue/page-5.html
# [ИНФОРМАЦИЯ] Сохраненные записи 100 в книжки.csv
#
# Process finished with exit code 0
