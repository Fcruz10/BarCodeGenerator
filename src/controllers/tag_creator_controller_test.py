from unittest.mock import patch
from src.drivers.barcode_handler import BarCodeHandler
from .tag_creator_controller import TagCreateController

@patch.object(BarCodeHandler, 'create_barcode')
def test_Create(mock_creator_barcode):
    mock_value = "image_path"
    mock_creator_barcode.return_value = mock_value
    tag_creator_controller = TagCreateController()

    result = tag_creator_controller.create(mock_value)

    assert isinstance(result, dict)
    assert "data" in result
    assert "type" in result["data"]
    assert "count" in result["data"]
    assert "path" in result["data"]

    assert result["data"]["type"] == "Tag Image"
    assert result["data"]["count"] == 1
    assert result["data"]["path"] == f'{ mock_value }.png'

