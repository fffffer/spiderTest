import datetime
import string
import time

import pymysql
import requests
from bs4 import BeautifulSoup



def get_html(n):
    url = 'https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA&cid2=653&cid3=655&page=' + str(n*2-1)
    headers = {
        'authority': 'search.jd.com',
        'method': 'GET',
        'path': '/im.php?r=1770779415&t=1565315379.7375&cs=6121bcfdb623cb194bcc80ae9037a1c8',
        'scheme': 'https',
        'referer': url,
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }
    html = requests.get(url,headers=headers)
    html.encoding = 'utf-8'
    return html.text

def get_last_html(n):
    # 获取当前的Unix时间戳，并且保留小数点后5位
    a = time.time()
    b = '%.5f' % a
    url = 'https://search.jd.com/s_new.php?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA&cid2=653&cid3=655&page='+str(n)+'&s='+str(48*n-20)+'&scrolling=y&log_id='+str(b)
    headers = {
        'authority': 'search.jd.com',
        'method': 'GET',
        'path': '/s_new.php?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA&cid2=653&cid3=655&page=4&s=86&scrolling=y&log_id=1565327127.45950&tpl=3_M&show_items=6176077,8058010,7652089,100004323348,100003258297,100005087998,7438288,50633925625,7652013,100000827661,100000822969,100002293114,100005945610,100000766433,100004050001,8485229,100006841262,100000084109,100001467225,100002493099,100005819880,8636676,100000773875,100003429677,33155679178,7437564,100003332220,100001548579,100005150846,7293054',
        'scheme': 'https',
        'referer': url,
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }
    html = requests.get(url,headers=headers)
    html.encoding = 'utf-8'
    return html.text


def insert_date(p_price,ps_items,p_name,p_sales,p_detail):
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='123123',
        db='shopmaster',
        charset='utf8',
    )

    cursor = conn.cursor()

    # 插入数据库，最后提交
    for i in range(len(p_price)):
        try:
            sql = "select goodsId from goods where goodsName = '" + p_name[i] + "';"
            goodsId = cursor.execute(sql)

            # 该字段不存在
            if goodsId == 0:
                date_time = datetime.date.fromtimestamp(time.time())
                sql = "insert into `shopmaster`.`goods`(`goodsName`, `price`, `num`, `upTime`, `category`, `detailCate`, `description`, `activityId`, `sales`) values(%s, %s, %s, %s, %s, %s,%s, %s, %s);"
                info = [(p_name[i],float(p_price[i]),100,date_time,1,"1",p_detail[i],1,200)]

                cursor.executemany(sql, info)
                # 找到该条语句的 goodsId
                sql = "select goodsId from goods where goodsName = '" + p_name[i] + "';"
                cursor.execute(sql)
                goodsId = cursor.fetchone()[0]

                # 插入图片 存储图片
                get_img(ps_items[i])
                sql = "insert imagepath(goodId,path) values(%s,%s);"
                info = [(goodsId,ps_items[i][-20:-3] + '.jpg')]
                cursor.executemany(sql,info)
        except Exception as e:
            print("插入失败:" + str(e))
            continue
        else:
            conn.commit()
            print("插入成功")


def parse_html(html):
    soup = BeautifulSoup(html,'lxml')
    lis = soup.find_all('li',attrs={'class':'gl-item'})
    p_price = []
    ps_items = []
    p_name = []
    p_detail = []
    p_sales = []
    for li in range(len(lis)):
        p_price.append(lis[li].select('div div.p-price strong i')[0].text)
        ps_items.append(lis[li].select('div div.p-img a img')[0].attrs['source-data-lazy-img'])
        p_detail.append(lis[li].select('div div.p-name em')[0].text)
        p_name.append(p_detail[li][:20])
        p_sales.append(lis[li].select('div div.p-commit strong a')[0].text)

    # print(p_sales)
    # insert_date(p_price,ps_items,p_name,p_sales,p_detail)

def get_img(imgs_url):

    imgs_url = "https:" + imgs_url
    html = requests.get(imgs_url)

    if html.status_code == 200:
        with open('D:/images/'+ imgs_url[-20:-3] + '.jpg', 'wb') as f:
            f.write(html.content)

    f.close()


def main():
     for i in range(1,2):
        html = get_html(i)
        print(html)
        # parse_html(html)
        #
        # html = get_last_html(i)
        # parse_html(html)






if __name__ == '__main__':
    main()
    exit()