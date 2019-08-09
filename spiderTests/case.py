import json

from bs4 import BeautifulSoup
import requests
import datetime
import time

def getHtml(url,data):

    data = requests.get(url,data)
    return data.text

def parse_html(html):
    soup = BeautifulSoup(html,'lxml')

    # 找到当前页的所有行
    table = soup.find('table', attrs={'id': 'report'})
    trs = table.find('tr').find_next_siblings()

    for tr in trs:
        tds = tr.find_all("td")
        yield [
            tds[0].text.strip(),
            tds[1].text.strip(),
            tds[2].text.strip(),
            tds[3].text.strip(),
            tds[4].text.strip(),
            tds[5].text.strip(),
            tds[6].text.strip(),
            tds[7].text.strip(),
            tds[8].text.strip(),
        ]


def write_to_file(content):
    with open('result.txt','a',encoding='utf-8') as file:
        file.write(json.dumps(content,ensure_ascii=False)+'\n')



def get_page_nums(url,date_time):
    data = {
        "pktrqks": date_time,
        "ktrqjs": date_time
    }

    html = getHtml(url,data)
    print(html)
    soup = BeautifulSoup(html,'lxml')
    res = soup.find('div',attrs={'class':'meneame'})
    pagenums = res.find('strong').text
    pagenums = int(pagenums)

    if pagenums % 15 == 0:
        pagenums = pagenums // 15
    else:
        pagenums = pagenums // 15 + 1

    return pagenums

def main():
    url = 'http://www.hshfy.sh.cn/shfy/gweb2017/ktgg_search_content.jsp?'
    date_time = datetime.date.fromtimestamp(time.time())

    pagenums = get_page_nums(url,date_time)

    pagenum = 1
    while pagenum <= pagenums:
        data = {
            "pktrqks": date_time,
            "ktrqjs": date_time,
            "pagesnum": pagenum,
        }

        html = getHtml(url,data)
        res = parse_html(html)
        for i in res:
            write_to_file(i)

        pagenum += 1

        print("当前打印%s" %(pagenum))
        time.sleep(2)


if __name__ == '__main__':
    main()