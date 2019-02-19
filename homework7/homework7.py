"""
1. Переписать код из homework6 используя ООП

2. Реализовать класс "очередь" https://en.wikipedia.org/wiki/Queue_(abstract_data_type)
- в качестве инициализации принимает размер очереди, если параметр не указан, то очередь - бесконечная
- выдать сообщение об ошибке, если в полную очередь добавить элемент нельзя, или из пустой очереди достать элемент

3. Реализовать класс "стек" https://en.wikipedia.org/wiki/Stack_(abstract_data_type)
- в качестве инициализации принимает размер стека, если параметр не указан, то стек - бесконечный
- выдать сообщение об ошибке, если в полный стек добавить элемент нельзя, или из пустого стека достать элемент
"""
import sys
import csv
import json
import pickle
import xml.etree.ElementTree as eTree


class BaseParser:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def get_extension(self, file_name):
        if not file_name:
            return
        extension = file_name.rsplit('.', 1)[-1]
        if file_name != extension:
            return extension

    def default(self, file_name, data):
        print(data)

    def convert(self):
        input_extension = self.get_extension(self.input_file)
        output_extension = self.get_extension(self.output_file)

        parse_method = getattr(self, f'parse_{input_extension}')
        dump_method = getattr(self, f'dump_{output_extension}', self.default)
        data = parse_method(self.input_file)
        dump_method(self.output_file, data)


class BinParser(BaseParser):
    def parse_bin(self, file_name):
        file = open(file_name, 'rb')
        data = pickle.load(file)
        file.close()
        return data

    def dump_bin(self, file_name, data):
        file = open(file_name, 'wb')
        pickle.dump(data, file)
        file.close()
        return pickle.dumps(data)


class JsonParser(BaseParser):
    def parse_json(self, file_name):
        file = open(file_name)
        data = file.read()
        file.close()
        return json.loads(data)

    def dump_json(self, file_name, data):
        file = open(file_name, 'w')
        file.write(json.dumps(data, indent=4))
        file.close()


class CsvParser(BaseParser):
    def parse_csv(self, file_name):
        file = open(file_name)
        reader = csv.DictReader(file)
        result = []
        for line in reader:
            result.append(dict(line))
        file.close()
        return result

    def dump_csv(self, file_name, data):
        file = open(file_name, 'w')
        if data:
            writer = csv.DictWriter(file, fieldnames=list(data[0].keys()))
            writer.writeheader()
            writer.writerows(data)
        file.close()


class XmlParser(BaseParser):
    def parse_xml(self, file_name):
        parser = eTree.parse(file_name)
        root = parser.getroot()
        result = []
        for item in root:
            _object = {}
            for attr in item:
                _object[attr.tag] = attr.text
            result.append(_object)
        return result

    def dump_xml(self, file_name, data):
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


class Parser(BinParser, XmlParser, CsvParser, JsonParser):
    pass


def main(argv):
    argv = argv[1:3]
    if not argv:
        print("Bad arguments")
        return
    input_file, output_file = (argv[0], argv[1]) \
        if len(argv) > 1 else (argv[0], None)
    Parser(input_file, output_file).convert()

if __name__ == '__main__':
    main(sys.argv)
