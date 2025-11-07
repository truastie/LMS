import pytest

from models.swagger_models import LoginModel, LoginResponseModel, AddingBookModel, AddingBookResponseModel, AddBooks, \
    AddBooksRequestModel
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

    def test_adding_book(self):
        client=Client()
        login_request=LoginModel(userName="rialversion",password="Trialversion!0")
        client.login(login_request)

        adding_book=AddingBookModel(
            userId="60ae8572-27a1-46f9-aa89-6fe606fcb031",
            collectionOfIsbns=[AddBooksRequestModel(isbn="9781449337711")]
        )
        client.post_add_book(request=adding_book, expected_model=AddingBookResponseModel(books=[AddBooks(isbn="9781449337711")]),
            status_code=201
        )