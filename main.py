import os
import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler
import argparse
from jinja2 import Environment, FileSystemLoader, select_autoescape
import pandas
from dotenv import load_dotenv
from collections import defaultdict


def get_company_age():
    date_of_foundation = datetime.date(year=1920, month=1, day=1)
    delta = datetime.date.today() - date_of_foundation
    return int(delta.total_seconds()//86400//365)


def choose_the_word_by_age(age):
    if age % 100 > 4 and age % 100 < 21:
        return f'{age} лет'
    remains = age % 100 % 10
    if remains == 1:
        return f'{age} год'
    if remains > 1 and remains < 5:
        return f'{age} года'
    else:
        return f'{age} лет'


def create_file_path():
    parser = argparse.ArgumentParser()
    load_dotenv()
    parser.add_argument('-p', '--path', default=f'{os.getenv("DRINKS_PATH")}')
    return parser


def sort_drinks(drinks):
    drink_category = defaultdict(list)
    for elem in drinks:
        drink_category[elem['Категория']].append(elem)
    return drink_category


def main():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    path_to_drinkdata = create_file_path().parse_args()

    excel_data_df2 = pandas.read_excel(f'{path_to_drinkdata.path}', sheet_name='Лист1', usecols=[
        'Категория','Название','Сорт','Цена','Картинка','Акция'], na_values='nan', keep_default_na=False)

    data_drink = excel_data_df2.to_dict(orient='records')

    age = get_company_age()

    rendered_page = template.render(
        date_of_foundation=choose_the_word_by_age(age),
        data_drinks=sort_drinks(data_drink)
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
