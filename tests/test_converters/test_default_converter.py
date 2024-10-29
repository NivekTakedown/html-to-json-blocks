import unittest
from bs4 import BeautifulSoup
from html_to_json_blocks.converters.default_converter import DefaultConverter

class TestDefaultConverter(unittest.TestCase):

    def setUp(self):
        self.converter = DefaultConverter()

    def test_convert_html_to_json_blocks(self):
        html = "<p>Paragraph</p><h1>Header</h1>"
        soup = BeautifulSoup(html, "html.parser")
        images_info = []
        result = self.converter.convert_html_to_json_blocks(soup, images_info)
        expected = [
            {"type": "paragraph", "children": [{"text": "Paragraph", "type": "text"}]},
            {"type": "heading", "children": [{"text": "Header", "type": "text"}], "level": 1, "size": "h1"}
        ]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
