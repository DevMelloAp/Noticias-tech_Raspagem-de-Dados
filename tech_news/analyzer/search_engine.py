# Requisito 6
from tech_news.database import search_news
import re


def search_by_title(title):
    lista = []
    news = search_news({"title": {"$regex": re.compile(title, re.IGNORECASE)}})

    for new in news:
        lista.append((new["title"], new["url"]))
    return lista


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
