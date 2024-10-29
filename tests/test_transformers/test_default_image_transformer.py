import unittest
from bs4 import BeautifulSoup
from datetime import datetime
from html_to_json_blocks.transformers.default_image_transformer import DefaultImageTransformer

class TestDefaultImageTransformer(unittest.TestCase):

    def setUp(self):
        self.image_transformer = DefaultImageTransformer()

    def test_transform_image(self):
        html = '<img src="image.png" alt="An image" width="100" height="100">'
        img_node = BeautifulSoup(html, "html.parser").img
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
            "createdAt": datetime.now().isoformat(),
            "updatedAt": datetime.now().isoformat(),
            "previewUrl": None,
            "alternativeText": "An image",
            "provider_metadata": None
        }]
        result = self.image_transformer.transform_image(img_node, images_info)
        self.assertEqual(result['type'], 'image')
        self.assertEqual(result['children'][0]['type'], 'text')

if __name__ == '__main__':
    unittest.main()
