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
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
