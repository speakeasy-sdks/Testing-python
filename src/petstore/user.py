"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from petstore import utils
from petstore.models import operations, shared
from typing import Optional

class User:
    r"""Operations about user"""
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def create_user_form(self, request: shared.User) -> operations.CreateUserFormResponse:
        r"""Create user
        This can only be done by the logged in user.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/user'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'form')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json;q=1, application/xml;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateUserFormResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if True:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.User])
                res.user = out
            if utils.match_content_type(content_type, 'application/xml'):
                res.body = http_res.content

        return res

    
    def create_user_json(self, request: shared.User) -> operations.CreateUserJSONResponse:
        r"""Create user
        This can only be done by the logged in user.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/user'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json;q=1, application/xml;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateUserJSONResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if True:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.User])
                res.user = out
            if utils.match_content_type(content_type, 'application/xml'):
                res.body = http_res.content

        return res

    
    def create_user_raw(self, request: bytes) -> operations.CreateUserRawResponse:
        r"""Create user
        This can only be done by the logged in user.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/user'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'raw')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json;q=1, application/xml;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateUserRawResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if True:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.User])
                res.user = out
            if utils.match_content_type(content_type, 'application/xml'):
                res.body = http_res.content

        return res

    
    def create_users_with_list_input(self, request: list[shared.User]) -> operations.CreateUsersWithListInputResponse:
        r"""Creates list of users with given input array
        Creates list of users with given input array
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/user/createWithList'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json;q=1, application/xml;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateUsersWithListInputResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.User])
                res.user = out
            if utils.match_content_type(content_type, 'application/xml'):
                res.body = http_res.content
        else:
            pass

        return res

    
    def delete_user(self, request: operations.DeleteUserRequest) -> operations.DeleteUserResponse:
        r"""Delete user
        This can only be done by the logged in user.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.DeleteUserRequest, base_url, '/user/{username}', request)
        headers = {}
        headers['Accept'] = '*/*'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteUserResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        

        return res

    
    def get_user_by_name(self, request: operations.GetUserByNameRequest) -> operations.GetUserByNameResponse:
        r"""Get user by user name"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetUserByNameRequest, base_url, '/user/{username}', request)
        headers = {}
        headers['Accept'] = 'application/json;q=1, application/xml;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetUserByNameResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.User])
                res.user = out
            if utils.match_content_type(content_type, 'application/xml'):
                res.body = http_res.content
        elif http_res.status_code in [400, 404]:
            pass

        return res

    
    def login_user(self, request: operations.LoginUserRequest) -> operations.LoginUserResponse:
        r"""Logs user into the system"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/user/login'
        headers = {}
        query_params = utils.get_query_params(operations.LoginUserRequest, request)
        headers['Accept'] = 'application/json;q=1, application/xml;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.LoginUserResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            res.headers = http_res.headers
            
            if utils.match_content_type(content_type, 'application/json'):
                res.login_user_200_application_json_string = http_res.content
            if utils.match_content_type(content_type, 'application/xml'):
                res.login_user_200_application_xml_string = http_res.content
        elif http_res.status_code == 400:
            pass

        return res

    
    def logout_user(self) -> operations.LogoutUserResponse:
        r"""Logs out current logged in user session"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/user/logout'
        headers = {}
        headers['Accept'] = '*/*'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.LogoutUserResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        

        return res

    
    def update_user_form(self, request: operations.UpdateUserFormRequest) -> operations.UpdateUserFormResponse:
        r"""Update user
        This can only be done by the logged in user.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.UpdateUserFormRequest, base_url, '/user/{username}', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "user", 'form')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = '*/*'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('PUT', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpdateUserFormResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        

        return res

    
    def update_user_json(self, request: operations.UpdateUserJSONRequest) -> operations.UpdateUserJSONResponse:
        r"""Update user
        This can only be done by the logged in user.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.UpdateUserJSONRequest, base_url, '/user/{username}', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "user", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = '*/*'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('PUT', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpdateUserJSONResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        

        return res

    
    def update_user_raw(self, request: operations.UpdateUserRawRequest) -> operations.UpdateUserRawResponse:
        r"""Update user
        This can only be done by the logged in user.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.UpdateUserRawRequest, base_url, '/user/{username}', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'raw')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = '*/*'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('PUT', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpdateUserRawResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        

        return res

    