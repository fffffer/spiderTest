import numpy
import pymysql
import requests
from bs4 import BeautifulSoup


def get_html(url):
    html = requests.get(url)
    return html.text

def insertData(title,content):
    # 连接数据库
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='123123',
        db='shopmaster',
        charset='utf8',
    )

    cursor = conn.cursor()

    # 插入数据库，最后提交
    for i in range(len(title)):
        try:
            sql = "insert into category_copy1(cateName,cateChild) values(%s,%s);"
            info = [(title[i], content[i][j]) for j in range(len(content[i]))]
            cursor.executemany(sql,info)
        except Exception as e:
            print("插入失败:" + e)
        else:
            conn.commit()
            print("插入成功")



def main():
    url = 'https://www.jd.com/allSort.aspx'
    data = {
        'headers': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
    }
    html = get_html(url)
    soup = BeautifulSoup(html,'lxml')

    dts = soup.select('dt a')
    dds = soup.select('dd')

    title = []
    content = []

    for i in range(len(dts)):
        child_tag = dds[i].select('a')
        title.append(dts[i].text)
        flag = []
        for j in range(len(child_tag)):
            flag.append(child_tag[j].text)

        content.append(flag)

    insertData(title,content)
    # print(dds)
    # dds = divs.find_all('dd')
    # print(dds)
    #     print(i)




if __name__ == '__main__':
    main()


    def parse_html(html):
        soup = BeautifulSoup(html, 'lxml')
        lis = soup.find_all('li', attrs={'class': 'gl-item'})
        p_price = lis[0].select('div div.p-price strong i')[0].text
        p_img = lis[0].select('div div.p-img a img')[0].attrs['source-data-lazy-img']
        get_img(p_img)


    def get_img(url):
        html = requests.get(url)
        if html.status_code == 200:
            with open('D:/images/1.jpg', 'wb') as f:
                f.write(html.content)