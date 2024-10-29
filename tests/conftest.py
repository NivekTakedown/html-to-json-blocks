import pytest
from unittest.mock import Mock
from html_to_json_blocks.transformers import DefaultImageTransformer

@pytest.fixture
def mock_image_transformer():
    return Mock(spec=DefaultImageTransformer)
