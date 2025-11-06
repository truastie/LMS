import allure
import requests
from pygments.lexers import data

from models.swagger_models import LoginModel, LoginResponseModel, AddingBookModel, AddingBookResponseModel
from tests_api.validate_response import validate_response


class ClientApi:
    def __init__(self, token=None):
        self.base_url = 'https://demoqa.com/'
        self.session = self._initialize_session()
        self.token = token

    @staticmethod
    def _initialize_session():
        return requests.Session()


    def request(self,
                method: str,
                url: str,
                json=None,
                headers=None):
        if headers is None:
            headers = {}
        if self.token:
            headers['Authorization'] = f"Bearer {self.token}"
        response = self.session.request(
            method=method,
            url=self.base_url + url,
            json=json,
            headers=headers
        )
        return response

class Client(ClientApi):
    def __init__(self, token=None):
        super().__init__(token=token)

    @allure.step('POST /Account/v1/Authorized')
    def login(self,
              request: LoginModel,
              expected_model=LoginResponseModel,
              status_code: int = 200):
        response = self.request(
            method='post',
            url='Account/v1/Authorized',
            json=request.model_dump()
        )

        validated_response = validate_response(response=response, model=expected_model, status_code=status_code)
        try:
            data = response.json()
        except ValueError:
            data = {}

        token = None
        if isinstance(data, dict):
            token = data.get('token') or data.get('accessToken') or data.get('jwtToken')

        if token:
            self.token = token
        return validated_response


    @allure.step('POST BookStore/v1/Books')
    def post_add_book(self,
                      request: AddingBookModel,
                      expected_model: AddingBookResponseModel,
                      status_code: int=201):
        response=self.request(
            method='post',
            url='BookStore/v1/Books',
            json=request.model_dump()
        )
        validated_response = validate_response(response=response, model=expected_model, status_code=status_code)
        return validated_response