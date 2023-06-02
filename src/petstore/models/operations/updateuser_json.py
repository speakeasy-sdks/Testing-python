"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import user as shared_user
from typing import Optional


@dataclasses.dataclass
class UpdateUserJSONRequest:
    
    username: str = dataclasses.field(metadata={'path_param': { 'field_name': 'username', 'style': 'simple', 'explode': False }})
    r"""name that need to be deleted"""
    user: Optional[shared_user.User] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""Update an existent user in the store"""
    

@dataclasses.dataclass
class UpdateUserJSONResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    