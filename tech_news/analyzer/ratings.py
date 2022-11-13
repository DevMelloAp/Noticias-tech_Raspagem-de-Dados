# Requisito 10
import operator
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
    list_news = find_news()
    list_comments_by_categories = []

    for new in list_news:
        list_comments_by_categories.append(new["category"])

    counter = {}
    for category in list_comments_by_categories:
        if category in counter:
            counter[category] += 1
        else:
            counter[category] = 1

    lista_sorted_by_category = sorted(
        counter.items(), key=operator.itemgetter(0))
    lista_sorted_by_comments = sorted(
        lista_sorted_by_category, key=operator.itemgetter(1), reverse=1)

    final_list = []
    for item in lista_sorted_by_comments:
        final_list.append(item[0])

    return final_list[0:5]
