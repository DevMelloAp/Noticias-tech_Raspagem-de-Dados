# Requisito 10
from tech_news.database import find_news


def top_5_news():
    list_top_5_news = []

    news = find_news()
    news_sorted_by_title = sorted(
        news, key=lambda row: row['title'], reverse=0
    )
    news_sorted_by_comments_count = sorted(
        news_sorted_by_title, key=lambda row: row['comments_count'], reverse=1
    )

    for new in news_sorted_by_comments_count:
        list_top_5_news.append((new["title"], new["url"]))

    return list_top_5_news[0:5]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
