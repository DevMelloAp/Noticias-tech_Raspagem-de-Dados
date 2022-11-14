# Requisito 12
import sys
from tech_news.analyzer.ratings import top_5_categories, top_5_news
from tech_news.analyzer.search_engine import (
    search_by_category, search_by_date, search_by_tag, search_by_title)

from tech_news.scraper import get_tech_news


def function(option, value):
    if option == "0":
        return get_tech_news(int(value))
    elif option == "1":
        return search_by_title(value)
    elif option == "2":
        return search_by_date(value)
    elif option == "3":
        return search_by_tag(value)
    else:
        return search_by_category(value)


def analyzer_menu():
    try:
        option = int(input(
            "Selecione uma das opções a seguir:\n"
            " 0 - Popular o banco com notícias;\n"
            " 1 - Buscar notícias por título;\n"
            " 2 - Buscar notícias por data;\n"
            " 3 - Buscar notícias por tag;\n"
            " 4 - Buscar notícias por categoria;\n"
            " 5 - Listar top 5 notícias;\n"
            " 6 - Listar top 5 categorias;\n"
            " 7 - Sair.\n"
        ))

        options_text = {
            "0": "Digite quantas notícias serão buscadas:",
            "1": "Digite o título:",
            "2": "Digite a data no formato aaaa-mm-dd:",
            "3": "Digite a tag:",
            "4": "Digite a categoria:",
            "5": top_5_news(),
            "6": top_5_categories(),
            "7": sys.stdout.write("Encerrando script\n")
        }

        option_str = str(option)

        value = input(options_text[option_str])

        result = function(option_str, value)

        return result

    except KeyError:
        sys.stderr.write("Opção inválida\n")

    except ValueError:
        sys.stderr.write("Opção inválida")
