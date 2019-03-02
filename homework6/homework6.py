"""

Написать !консольную! программу, которая на вход получает имя входного файла,
имя выходного и решает определенную задачу.
Задача программы:
1) По расширению файлов определить какой тип данных в них.
 - <file_name>.json - в файле лежит json
 - <file_name>.csv - лежит csv
 - <file_name>.xml - лежит xml
  - <file_name>.bin - лежит объект, упакованный при помощи pickle
2) Перегнать данные из одного файла в другой соблюдая тип данных
Пример:
python homework6.py data.json data.csv
из json который лежит в data.json сделать csv и положить в файл data.csv

PS: для проверки существования файла можно использовать os.path.exists(<path>)
3) Второй файл в аргументе может быть не указан.
python homework6.py data.json

Если второй аргумент не указан, то данные из файла data.json вывести на экран в
виде питоновского объекта.


PS: глубина вложенности данных - 1
т.е. для xml не может быть вложености глубже тегов внутри тега <item>
<root>
   <item>
      <author>Gambardella, Matthew</author>
      <title>XML Developer's Guide</title>
      <genre>Computer</genre>
      <price>44.95</price>
      <publish_date>2000-10-01</publish_date>
      <description>An in-depth look at creating applications
      with XML.</description>
   </item>
   <item>
      <author>Ralls, Kim</author>
      <title>Midnight Rain</title>
      <genre>Fantasy</genre>
      <price>5.95</price>
      <publish_date>2000-12-16</publish_date>
      <description>A former architect battles corporate zombies,
      an evil sorceress, and her own childhood to become queen
      of the world.</description>
   </item>
</root>

для json не могут быть объекты внутри объектов
"""
import json
import sys
import csv

import pickle
import xml.etree.ElementTree as eTree


def get_extension(file_name):
    if not file_name:
        return
    extension = file_name.rsplit('.', 1)[-1]
    if file_name != extension:
        return extension


def parse_bin(file_name):
    file = open(file_name, 'rb')
    data = pickle.load(file)
    file.close()
    return data


def dump_bin(file_name, data):
    file = open(file_name, 'wb')
    pickle.dump(data, file)
    file.close()
    return pickle.dumps(data)


def parse_json(file_name):
    file = open(file_name)
    data = file.read()
    file.close()
    return json.loads(data)


def dump_json(file_name, data):
    file = open(file_name, 'w')
    file.write(json.dumps(data, indent=4))
    file.close()


def parse_csv(file_name):
    file = open(file_name)
    reader = csv.DictReader(file)
    result = []
    for line in reader:
        result.append(dict(line))
    file.close()
    return result


def dump_csv(file_name, data):
    file = open(file_name, 'w')
    if data:
        writer = csv.DictWriter(file, fieldnames=list(data[0].keys()))
        writer.writeheader()
        writer.writerows(data)
    file.close()


def parse_xml(file_name):
    parser = eTree.parse(file_name)
    root = parser.getroot()
    result = []
    for item in root:
        _object = {}
        for attr in item:
            _object[attr.tag] = attr.text
        result.append(_object)
    return result


def dump_xml(file_name, data):
    file = open(file_name)
    items = ''
    for item in data:
        item_str = ''
        for key, value in item.items():
            item_str += f'<{key}>{value}</{key}>'
        items += f'<item>{item_str}</item>'
    result = f'<root>{items}</root>'
    file.write(result)
    file.close()


def dump_console(file_name, data):
    print(data)


def main(argv):
    argv = argv[1:3]
    if not argv:
        raise Exception("Bad arguments")
    input_file, output_file = (argv[0], argv[1]) \
        if len(argv) > 1 else (argv[0], None)

    functions = {
        'bin': (parse_bin, dump_bin),
        'json': (parse_json, dump_json),
        'csv': (parse_csv, dump_csv),
        'xml': (parse_xml, dump_xml),
        None: (None, dump_console)
    }
    ext_in_file = get_extension(input_file)
    ext_out_file = get_extension(output_file)

    parse_func = functions.get(ext_in_file)
    dump_func = functions.get(ext_out_file)
    if not parse_func or not dump_func:
        print('Wrong extension')
        return

    data = parse_func[0](input_file)
    dump_func[1](output_file, data)

if __name__ == '__main__':
    main(sys.argv)
