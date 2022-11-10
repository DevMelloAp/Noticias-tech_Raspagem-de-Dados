# Requisito 1
import time
import requests
from parsel import Selector


def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(
            url,
            headers={"user-agent": "Fake user-agent"},
            timeout=3
        )
        if response.status_code == 200:
            return response.text
        elif response.status_code:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)

    list_link_new = selector.css(".cs-overlay-link::attr(href)").getall()

    return list_link_new


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)

    next = selector.css(".next.page-numbers::attr(href)").get()

    if not next:
        return None

    else:
        return next


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)

    url = selector.css("head link[rel=canonical]::attr(href)").get()
    category = selector.css("div.meta-category > a > span.label::text").get()
    title = selector.css(
        ".entry-title::text").get().replace("\xa0", " ").strip()
    timestamp = selector.css(".meta-date::text").get()
    writer = selector.css(".author a::text").get()
    comments_count = len(selector.css("footer.comment-meta").getall())
    summary = "".join(
        selector.css("div.entry-content > p:first-of-type *::text").getall()
        ).replace("\xa0", " ").strip()
    tags = selector.css("section.post-tags ul li a::text").getall()

    return(
        {
            "url": url,
            "title": title,
            "timestamp": timestamp,
            "writer": writer,
            "comments_count": comments_count,
            "summary": summary,
            "tags": tags,
            "category": category
        }
    )


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
