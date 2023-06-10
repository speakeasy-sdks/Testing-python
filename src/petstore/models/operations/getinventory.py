"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Optional



@dataclasses.dataclass
class GetInventorySecurity:
    api_key: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'api_key' }})
    




@dataclasses.dataclass
class GetInventoryResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_inventory_200_application_json_object: Optional[dict[str, int]] = dataclasses.field(default=None)
    r"""successful operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

