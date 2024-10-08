from .TestBaseConverter import TestBaseConverterComplex
from .TestDefaultConverter_test_convert_html_to_json_blocks import TestDefaultConverter
from .TestDefaultImageTransformer_test_transform_image import TestDefaultImageTransformer
from .TestHtmlToJsonConverter_test_convert import TestHtmlToJsonConverterComplex

# Making sure the unittest main runs the tests when the test suite is executed
import unittest

if __name__ == '__main__':
    unittest.main()