import pytest
from TheCatAPI import get_random_cat_image

def test_get_random_cat_image_success(mocker):
    mock_get = mocker.patch('TheCatAPI.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [{
        'url': 'https://cdn2.thecatapi.com/images/abc.jpg'
    }]

    cat_url = get_random_cat_image()
    assert cat_url == 'https://cdn2.thecatapi.com/images/abc.jpg'

def test_get_random_cat_image_failure(mocker):
    mock_get = mocker.patch('TheCatAPI.requests.get')
    mock_get.return_value.status_code = 404

    cat_url = get_random_cat_image()
    assert cat_url is None

