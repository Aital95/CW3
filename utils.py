import json
from datetime import datetime


def get_data():
    with open('operations.json', 'r', encoding='utf-8') as file:
    #with open('./path/Kursach_3/venv/operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def filter_data(data):
    data = [x for x in data if 'state' in x and x['state'] == 'EXECUTED']
    return data


def sort_data(data):
    data = sorted(data, key=lambda x: x['date'], reverse=True)
    return data[:5]


def format_data(data):
    formatted_data = []
    for row in data:
        date = datetime.strptime(row['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime("%d.%m.%Y")
        description = row['description']
        recipient = row['to'].split()
        recipient_bill = recipient.pop(-1)
        recipient_bill = f"**{recipient_bill[-4:]}"
        transfer_summ = row['operationAmount']['amount']
        currency = row['operationAmount']['currency']['name']
        if "from" in row:
            from_arrow = "->"
            sender = row['from'].split()
            sender_bill = sender.pop(-1)
            sender_info = " ".join(sender)
            sender_bill = f"{sender_bill[:4]} {sender_bill[4:6]}** **** {sender_bill[-4:]}"

        else:
            sender_info = "Новый счет"
            sender_bill = ""
            from_arrow = ""




        formatted_data.append(f"""
{date} {description}
{sender_info} {sender_bill} {from_arrow} {recipient_bill}
{transfer_summ} {currency}""")
    return formatted_data