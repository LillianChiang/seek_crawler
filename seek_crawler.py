import urllib3
import requests
import time
from bs4 import BeautifulSoup

def str_to_file(file, text):
    print('Output: ' + file)
    f = open(file, 'w', encoding='utf-8-sig')
    f.write(text)
    f.close()

def strip(text):
    return text.replace(' ', '').replace('\r', '').replace('\n', '')

if __name__ == '__main__':
    #build the connection
    urllib3.disable_warnings()
    s = requests.Session()
    url = 'https://www.seek.com.au/job/51216701?type=promoted#searchRequestToken=8740079d-4e26-48c7-a0cb-a836419c60ac'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0'}
    resp = requests.get(url, headers = headers, verify = False)
    resp.close()
    
    #analysis the website
    test = ''
    soup = BeautifulSoup(resp.text, 'html.parser')  
    span_list=soup.find('span',{'class':'_3FrNV7v _12_uzrS E6m4BZb'})
    for span in span_list:
            print(span.h1.text) 

    Q=soup.find('div',{'data-automation':'mobileTemplate'})
    ul_list=Q.find_all('ul')
    for ul in ul_list:
            print(ul.text)

    #Output file
    str_to_file('homework.csv', test)

    #done
    print('\nProgram exist\n')