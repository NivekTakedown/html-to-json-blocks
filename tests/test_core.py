import unittest
from unittest.mock import Mock
from bs4 import BeautifulSoup
from html_to_json_blocks.core import HtmlToJsonConverter

class TestHtmlToJsonConverter(unittest.TestCase):

    def setUp(self):
        self.mock_image_transformer = Mock()
        self.mock_image_transformer.transform_image.side_effect = self.mock_transform_image
        self.converter = HtmlToJsonConverter(self.mock_image_transformer)

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

    def test_convert(self):
        html = '''
        <h1>Header 1</h1>
        <p>Paragraph with <a href="http://example.com">link</a> and <b>bold</b> text.</p>
        <ul>
            <li>List item 1</li>
            <li>List item 2 with <i>italic</i> text</li>
        </ul>
        <img src="image.png" alt="An image" width="100" height="100"/>
        '''
        soup = BeautifulSoup(html, "html.parser")
        images_info = [{
            "src": "image.png",
            "ext": "png",
            "url": "http://example.com/image.png",
            "hash": "123abc",
            "mime": "image/png",
            "name": "image.png",
            "size": 1024,
            "width": 100,
            "height": 100,
            "caption": "An image",
            "formats": {},
            "provider": "local",
            "createdAt": "2023-09-15T12:00:00",
            "updatedAt": "2023-09-15T12:00:00",
            "previewUrl": None,
            "alternativeText": "An image",
            "provider_metadata": None
        }]

        result = self.converter.convert(soup, images_info)
        expected = [
            {
                "type": "heading",
                "children": [
                    {
                        "text": "Header 1",
                        "type": "text"
                    }
                ],
                "level": 1,
                "size": "h1"
            },
            {
                "type": "paragraph",
                "children": [
                    {
                        "text": "Paragraph with",
                        "type": "text"
                    },
                    {
                        "type": "link",
                        "url": "http://example.com",
                        "children": [
                            {
                                "text": " link ",
                                "type": "text"
                            }
                        ]
                    },
                    {
                        "text": "and",
                        "type": "text"
                    },
                    {
                        "bold": True,
                        "text": " bold ",
                        "type": "text"
                    },
                    {
                        "text": "text.",
                        "type": "text"
                    }
                ]
            },
            {
                "type": "list",
                "format": "unordered",
                "children": [
                    {
                        "type": "list-item",
                        "children": [
                            {
                                "text": "List item 1",
                                "type": "text"
                            }
                        ]
                    },
                    {
                        "type": "list-item",
                        "children": [
                            {
                                "text": "List item 2 with",
                                "type": "text"
                            },
                            {
                                "italic": True,
                                "text": " italic ",
                                "type": "text"
                            },
                            {
                                "text": "text",
                                "type": "text"
                            }
                        ]
                    }
                ]
            },
            {
                "type": "image",
                "image": {
                    "url": "image.png",
                    "caption": "An image",
                    "width": 100,
                    "height": 100
                },
                "children": [
                    {
                        "text": "",
                        "type": "text"
                    }
                ]
            }
        ]

        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
