import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape
import pandas

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

def company_years_old():
    date_of_foundation = datetime.date(year=1920, month=1, day=1)
    delta = datetime.date.today() - date_of_foundation
    years_old = int(delta.total_seconds()//86400//365)
    if years_old % 100 > 4 and years_old % 100 < 21:
        return f'{years_old} лет'
    else:
        remains = years_old % 100 % 10
        if remains == 1:
            return f'{years_old} год'
        if remains > 1 and remains < 5:
            return f'{years_old} года'
        else:
            return f'{years_old} лет'


def drink_category(drink_list):
    drink_category_dict = {}
    for elem in drink_list:
        if elem['Категория'] not in drink_category_dict:
            drink_category_dict[elem['Категория']] = []

    for elem in drink_list:
        drink_category_dict[elem['Категория']].append(elem)
    return drink_category_dict



excel_data_df2 = pandas.read_excel('wine3.xlsx', sheet_name='Лист1', usecols=[
    'Категория','Название','Сорт','Цена','Картинка','Акция'], na_values='nan', keep_default_na=False)

list_data_drink = excel_data_df2.to_dict(orient='records')

rendered_page = template.render(
    date_of_foundation=company_years_old(),
    list_data_drink=drink_category(list_data_drink)
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
