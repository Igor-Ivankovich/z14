import xml.etree.ElementTree as eTree
from xml import etree

data = eTree.parse('example.xml')
root = data.getroot()
for item in root:
    print(item.attrib)
    # for child in item.getchildren():
    #     print(child.tag, child.text)
    element = item.find('publish_date')
    print(element.tag, element.text)


root = eTree.Element('root')
book = eTree.Element('book')
title = eTree.Element('title')
title.text = "Some text"
book.append(title)
root.append(book)
root.append(eTree.Element('book'))

print(eTree.dump(root))
