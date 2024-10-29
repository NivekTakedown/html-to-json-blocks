import unittest
from bs4 import BeautifulSoup
from html_to_json_blocks.converters.base_converter import BaseConverter
from unittest.mock import Mock
from datetime import datetime

class TestBaseConverter(unittest.TestCase):

    def setUp(self):
        self.converter = BaseConverter()
        self.mock_image_transformer = Mock()

    def test_convert_html_to_json_blocks(self):
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
            "ext": "jpg",
            "url": "example.jpg",
            "hash": "",
            "mime": "image/jpg",
            "name": "",
            "size": 0,
            "width": "200",
            "height": "100",
            "caption": "Example image",
            "formats": {},
            "provider": "local",
            "createdAt": "2024-10-29T10:32:20.672364",
            "updatedAt": "2024-10-29T10:32:20.672381",
            "previewUrl": None,
            "alternativeText": "Example image",
            "provider_metadata": None
        }]

        self.mock_image_transformer.transform_image.side_effect = self.mock_transform_image
        result = self.converter.convert_html_to_json_blocks(soup, images_info, self.mock_image_transformer)

        # Remove dynamic timestamps from the result for comparison
        for block in result:
            if block['type'] == 'image':
                block['image'].pop('createdAt', None)
                block['image'].pop('updatedAt', None)

        expected = [
            {
                "type": "heading",
                "children": [
                    {
                        "text": "Main Header",
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
                        "text": "This is a",
                        "type": "text"
                    },
                    {
                        "bold": True,
                        "text": " bold ",
                        "type": "text"
                    },
                    {
                        "text": "and",
                        "type": "text"
                    },
                    {
                        "italic": True,
                        "text": " italic ",
                        "type": "text"
                    },
                    {
                        "text": "paragraph with a",
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
                        "text": ".",
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
                                "text": "First item",
                                "type": "text"
                            }
                        ]
                    },
                    {
                        "type": "list-item",
                        "children": [
                            {
                                "text": "Second item with",
                                "type": "text"
                            },
                            {
                                "bold": True,
                                "text": " bold ",
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
                "type": "paragraph",
                "children": [
                    {
                        "text": "Another paragraph.",
                        "type": "text"
                    }
                ]
            },
            {
                "type": "image",
                "image": {
                    "ext": "jpg",
                    "url": "example.jpg",
                    "hash": "",
                    "mime": "image/jpg",
                    "name": "",
                    "size": 0,
                    "width": "200",
                    "height": "100",
                    "caption": "Example image",
                    "formats": {},
                    "provider": "local",
                    "previewUrl": None,
                    "alternativeText": "Example image",
                    "provider_metadata": None
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

    def mock_transform_image(self, img_node, images_info):
        return {
            "type": "image",
            "image": {
                "ext": "jpg",
                "url": img_node.get('src'),
                "hash": "",
                "mime": "image/jpg",
                "name": "",
                "size": 0,
                "width": img_node.get('width'),
                "height": img_node.get('height'),
                "caption": img_node.get('alt', ''),
                "formats": {},
                "provider": "local",
                "createdAt": datetime.now().isoformat(),
                "updatedAt": datetime.now().isoformat(),
                "previewUrl": None,
                "alternativeText": img_node.get('alt', ''),
                "provider_metadata": None
            },
            "children": [{"text": "", "type": "text"}]
        }

if __name__ == '__main__':
    unittest.main()
