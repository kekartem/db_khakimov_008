import json


def find(client, date):
    file = open('db.json', 'r')
    db = json.load(file)['db']
    for i in db['trips']:
        if i['client']['id'] == client and i['date'][0] == date:
            print(i)


find(4, 6)
