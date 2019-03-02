import os
import unittest
import json

from homework6 import get_extension, parse_json, dump_json, main


class TestGetExtension(unittest.TestCase):

    def test_get_extension_ok(self):
        ext_list = ['csv', 'bin', 'json', 'xml']
        for ext in ext_list:
            self.assertEqual(get_extension(f'file.{ext}'), ext)

    def test_get_extension_none(self):
        self.assertIsNone(get_extension('file_name'))
        self.assertIsNone(get_extension(''))


class TestJson(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.file_name = 'files/test_data.json'
        cls.expected = [
            {
                "name": "value1",
                "last_name": "last1"
            },
            {
                "name": "value2",
                "last_name": "last2"
            }
        ]
        cls.dump_file_name = 'files/test_dump.json'

    def test_parse(self):
        data = parse_json(self.file_name)
        self.assertEqual(data, self.expected)

    def test_dump(self):
        dump_json(self.dump_file_name, self.expected)
        self.assertTrue(os.path.exists(self.dump_file_name))
        with open(self.dump_file_name) as file:
            file_data = file.read()
            self.assertEqual(file_data, json.dumps(self.expected, indent=4))
            self.assertEqual(json.loads(file_data), self.expected)


class TestMain(unittest.TestCase):
    def test_main(self):
        with self.assertRaises(Exception):
            main(['file.py'])

        self.assertIsNone(main(['file.py', 'input.doc', 'output.xls']))

if __name__ == '__main__':
    unittest.main()
