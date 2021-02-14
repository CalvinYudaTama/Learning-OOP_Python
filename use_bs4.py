import requests
from  bs4 import BeautifulSoup

url  = 'https://kompas.com'

try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f'Sucess Response = {response.status_code}')
        soup = BeautifulSoup(response.text, features="html.parser")
        print(f'Hasil pemanggilan{url}')
        print(f'Title{soup.title.string}')
    else:
        print(f'Whoops Ada Kesalahan {response.status_code}')
except Exception as e:
        print(f'There Program Ada Error{e}')
print('Program end')

