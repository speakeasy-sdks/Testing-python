"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import pet as shared_pet
from typing import Optional


@dataclasses.dataclass
class UpdatePetFormSecurity:
    
    petstore_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'oauth2', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class UpdatePetFormResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    body: Optional[bytes] = dataclasses.field(default=None)
    pet: Optional[shared_pet.Pet] = dataclasses.field(default=None)
    r"""Successful operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    