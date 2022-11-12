# Requisito 6
from datetime import datetime
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
    try:
        date_time = datetime.strptime(date, "%Y-%m-%d").date()
        lista = []
        news = search_news(
            {"timestamp": re.escape(date_time.strftime("%d/%m/%Y"))}
        )

        for new in news:
            lista.append((new["title"], new["url"]))
        return lista

    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
