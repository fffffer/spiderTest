from pyquery import PyQuery as pq

#  基本语法和 Jquery 几乎一样
# html = '''
# <div>
#     <ul>
#          <li class="item-0" id="li_1">first item</li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#          <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a></li>
#      </ul>
# </div>
# '''
#
# doc = pq(html)
#
# print(doc('#li_1'))

# doc = pq(url="https://www.baidu.com",encoding="utf-8")
# print(doc('title').text())
#
html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
#
# doc = pq(html)
#
# items = doc('.list')

# .item-0.active 两个挨在一起表示并的关系
# lis = items.find('.item-0.active')
# .list .item-0 隔开表示层次关系
# lis = doc.find('.list .item-0')
# print(lis)

# 遍历方法
# lis = doc('li').items()
# for li in lis:
#     print(li)

# 获取属性
# doc = pq(html)
#
# print(doc('ul').attr('class'))
# print(doc('.item-0.active a').text())
# print(doc('.item-0.active a').attr.href)
