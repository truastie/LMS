import pytest

from models.swagger_models import LoginModel, LoginResponseModel, AddingBookModel, AddingBookResponseModel
from utils.client import Client


@pytest.mark.positive

class TestApi:
    def test_login(self):
        Client().login(request=LoginModel(
            userName="trialversion",
            password="Trialversion!1"
        ),expected_model=LoginResponseModel(root=True),
            status_code=200
        )

    def test_adding_bool(self):
        Client().post_add_book(request=AddingBookModel(
            userId=""
        ), expected_model=AddingBookResponseModel(isbn=""),
            status_code=201
        )