from threading import Thread

import requests


def date_1():
    data = requests.get(url="https://jsonplaceholder.typicode.com/photos")
    print(f"Status_code = {data.status_code}")


def date_2():
    data = requests.get(url='https://www.xitmuzon.net/')
    print(f"Status_code = {data.status_code}")


def date_3():
    data = requests.get(url='https://www.olx.uz/')
    print(f"Status_code = {data.status_code}")


def date_4():
    data = requests.get(url='https://www.uzhits.net/')
    print(f"Status_code = {data.status_code}")


def date_5():
    data = requests.get(url='https://www.asilmedia.org/')
    print(f"Status_code = {data.status_code}")


oqim_1 = Thread(target=date_1)
oqim_2 = Thread(target=date_2)
oqim_3 = Thread(target=date_3)
oqim_4 = Thread(target=date_4)
oqim_5 = Thread(target=date_5)
oqimlar = [oqim_1, oqim_2, oqim_3, oqim_4, oqim_5]
for i in oqimlar:
    i.start()

for i in oqimlar:
    i.join()
