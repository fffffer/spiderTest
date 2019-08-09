from bs4 import BeautifulSoup

# html = '''
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title"><b>The Dormouse's story</b></p>
#
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
# <p class="story">...</p>
# '''

# soup = BeautifulSoup(html,'lxml')
# print(soup.prettify())
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.parent.name)
# print(soup.p)
# print(soup.p['class'])
# print(soup.a)
# print(soup.find_all('a'))
# print(soup.find(id='link3'))

# for link in soup.find_all('a'):
#     print(link.get('href'))
#
# print(soup.get_text)

# print(soup.title)
# print(type(soup.title))
# print(soup.head)
# print(soup.p)


# html = """
# <html>
#     <head>
#         <title>The Dormouse's story</title>
#     </head>
#     <body>
#         <p class="story">
#             Once upon a time there were three little sisters; and their names were
#             <a href="http://example.com/elsie" class="sister" id="link1">
#                 <span>Elsie</span>
#             </a>
#             <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
#             and
#             <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
#             and they lived at the bottom of a well.
#         </p>
#         <p class="story">...</p>
# """
#
# soup = BeautifulSoup(html,'lxml')
# print(soup.p.contents[1])



html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element" id="li_1">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''

soup = BeautifulSoup(html,'lxml')
# print(soup.find_all('li',text='Foo'))
print(soup.find_all(attrs={"class":"list","id":"list-1"}))

# select CSS选择器 （.class     #id） 返回的是数组
# print(soup.select('ul li'))
# print(soup.select('.li_1'))


# 获取内容
# for li in soup.find_all('li'):
#     print(li.get_text())

# 获取属性
# for ul in soup.select('ul'):
#     print(ul.attrs['id'])
#     print(ul.attrs['class'])
