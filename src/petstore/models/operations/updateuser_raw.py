"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Optional



@dataclasses.dataclass
class UpdateUserRawRequest:
    username: str = dataclasses.field(metadata={'path_param': { 'field_name': 'username', 'style': 'simple', 'explode': False }})
    r"""name that need to be deleted"""
    request_body: Optional[bytes] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/xml' }})
    r"""Update an existent user in the store"""
    




@dataclasses.dataclass
class UpdateUserRawResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

