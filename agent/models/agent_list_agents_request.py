# coding: utf-8

"""
    agent/service.proto

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: version not set
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
from agent.models.list_request_filters import ListRequestFilters
from agent.models.list_request_sort import ListRequestSort
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class AgentListAgentsRequest(BaseModel):
    """
    AgentListAgentsRequest
    """ # noqa: E501
    page_token: Optional[StrictStr] = Field(default=None, alias="pageToken")
    sorts: Optional[List[ListRequestSort]] = None
    filters_mask: Optional[StrictStr] = Field(default=None, alias="filtersMask")
    filters: Optional[ListRequestFilters] = None
    __properties: ClassVar[List[str]] = ["pageToken", "sorts", "filtersMask", "filters"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AgentListAgentsRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in sorts (list)
        _items = []
        if self.sorts:
            for _item in self.sorts:
                if _item:
                    _items.append(_item.to_dict())
            _dict['sorts'] = _items
        # override the default output from pydantic by calling `to_dict()` of filters
        if self.filters:
            _dict['filters'] = self.filters.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of AgentListAgentsRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pageToken": obj.get("pageToken"),
            "sorts": [ListRequestSort.from_dict(_item) for _item in obj.get("sorts")] if obj.get("sorts") is not None else None,
            "filtersMask": obj.get("filtersMask"),
            "filters": ListRequestFilters.from_dict(obj.get("filters")) if obj.get("filters") is not None else None
        })
        return _obj


