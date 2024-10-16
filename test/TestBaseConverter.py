import unittest
from bs4 import BeautifulSoup, NavigableString
from converters.base_converter import BaseConverter
from unittest.mock import Mock


class TestBaseConverterComplex(unittest.TestCase):

    def setUp(self):
        self.converter = BaseConverter()
        self.mock_image_transformer = Mock()

    def test_convert_complex_html_structure(self):
        html = '''
        <div>
            <h1>Main Header</h1>
            <p>This is a <b>bold</b> and <i>italic</i> paragraph with a <a href="http://example.com">link</a>.</p>
            <ul>
                <li>First item</li>
                <li>Second item with <b>bold</b> text</li>
            </ul>
            <p>Another paragraph.</p>
            <img src="example.jpg" alt="Example image" width="200" height="100">
        </div>
        '''
        soup = BeautifulSoup(html, 'html.parser')
        images_info = [{
            "src": "example.jpg",
            "ext": "jpg",
            "url": "http://example.com/example.jpg",
            "hash": "123abc",
            "mime": "image/jpeg",
            "name": "example.jpg",
            "size": 2048,
            "width": 200,
            "height": 100,
            "caption": "Example image",
            "formats": {},
            "provider": "local",
            "createdAt": "2023-09-15T12:00:00",
            "updatedAt": "2023-09-15T12:00:00",
            "previewUrl": None,
            "alternativeText": "Example image",
            "provider_metadata": None
        }]

        self.mock_image_transformer.transform_image.side_effect = self.mock_transform_image
        result = self.converter.convert_html_to_json_blocks(soup, images_info, self.mock_image_transformer)

        expected = [
            {"type": "heading", "children": [{"text": "Main Header", "type": "text"}], "level": 1, "size": "h1"},
            {
                "type": "paragraph",
                "children": [
                    {"text": "This is a", "type": "text"},
                    {"bold": True, "text": " bold ", "type": "text"},
                    {"text": "and", "type": "text"},
                    {"italic": True, "text": " italic ", "type": "text"},
                    {"text": "paragraph with a", "type": "text"},
                    {
                        "type": "link",
                        "url": "http://example.com",
                        "children": [{"text": " link ", "type": "text"}]
                    },
                    {"text": ".", "type": "text"}
                ]
            },
            {
                "type": "list",
                "format": "unordered",
                "children": [
                    {"type": "list-item", "children": [{"text": "First item", "type": "text"}]},
                    {"type": "list-item",
                     "children": [{"text": "Second item with"}, {"bold": True, "text": " bold ", "type": "text"},
                                  {"text": "text", "type": "text"}]}
                ]
            },
            {"type": "paragraph", "children": [{"text": "Another paragraph.", "type": "text"}]},
            {"type": "image", "image": {"url": "example.jpg", "caption": "Example image", "width": 200, "height": 100},
             "children": [{"text": "", "type": "text"}]}
        ]

        self.assertEqual(result, expected)

    def mock_transform_image(self, img_node, images_info):
        return {
            "type": "image",
            "image": {
                "url": img_node.get('src'),
                "caption": img_node.get('alt', ''),
                "width": int(img_node.get('width')),
                "height": int(img_node.get('height')),
            },
            "children": [{"text": "", "type": "text"}]
        }


if __name__ == '__main__':
    unittest.main()


if __name__ == '__main__':
    unittest.main()