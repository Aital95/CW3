from utils import sort_data, get_data, filter_data, format_data
from .my_conftest import test_data
import json


def test_sort_data(test_data):
    sorted_data = sort_data(test_data)
    assert [x['date'] for x in sorted_data] == ['2019-07-03T18:35:29.512364', '2018-06-30T02:08:58.425572', '2017-08-26T10:50:58.294041']


def test_get_data():
    with open('C:/Users/user/PycharmProjects/Kursach_3/operations.json', 'r', encoding='utf-8') as file:
        json_data = json.load(file)
    return json_data



def test_filter_data(test_data):
    result = filter_data(test_data)
    assert result == test_data
  #       filter_data(test_data) == [{
  #   "id": 939719570,
  #   "state": "EXECUTED",
  #   "date": "2018-06-30T02:08:58.425572",
  #   "operationAmount": {
  #     "amount": "9824.07",
  #     "currency": {
  #       "name": "USD",
  #       "code": "USD"
  #     }
  #   },
  #   "description": "Перевод организации",
  #   "from": "Счет 75106830613657916952",
  #   "to": "Счет 11776614605963066702"
  # }]


def test_format_data(test_data):
    assert format_data(test_data) == ['\n26.08.2017 Перевод организации\nMaestro 1596 83** **** 5199 -> **9589\n31957.58 руб.',
                                      '\n03.07.2019 Перевод организации\nMasterCard 7158 30** **** 6758 -> **5560\n8221.37 USD',
                                      '\n30.06.2018 Перевод организации\nСчет 7510 68** **** 6952 -> **6702\n9824.07 USD']

