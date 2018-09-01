from bs4 import BeautifulSoup

html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
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


soup = BeautifulSoup(html, 'lxml')
# print(soup.prettify())
# print("    ")
# print(soup.title)
# print("    ")
# print(soup.title.name)
# print("    ")
# print(soup.title.string)
# print("    ")
# print(soup.title.parent.name)
# print("    ")
# print(soup.p)
# print("    ")
# print(soup.p["class"])
# print("    ")
# print(soup.a)
# print("    ")
# print(soup.find_all('a'))
# print("    ")
# print(soup.find(id='link3'))
# print("    ")
# for link in soup.find_all('a'):
#     print(link.get('href'))
# print(soup.get_text)

# print(soup.p.contents)

# print(soup.find_all('ul'))
# print(type(soup.find_all('ul')[0]))

# for each in soup.find_all('ul'):
#     # print(each.find_all('li'))
#     for every in each.find_all('li'):
#         # print(every.string)
#         if every.text == 'Foo':
#             print(every.attrs)

# print(soup.find_all(attrs={'class': 'element'}))
# print(soup.find_all(attrs={'name': 'element'}))
# print(soup.find_all(attrs={'id': 'list-1'}))

print(soup.select('.panel-heading'))
print(soup.select('ul li'))
print(soup.select('#list-2 .element'))
print(type(soup.select('ul')[0]))


