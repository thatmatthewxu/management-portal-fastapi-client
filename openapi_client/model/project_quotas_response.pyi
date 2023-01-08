# coding: utf-8

"""
    core

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from openapi_client import schemas  # noqa: F401


class ProjectQuotasResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "cloud",
            "project_name_or_id",
            "quotas",
            "success",
            "message",
        }
        
        class properties:
            success = schemas.BoolSchema
            project_name_or_id = schemas.StrSchema
            cloud = schemas.StrSchema
            
            
            class quotas(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    any_of_1 = schemas.DictSchema
                    
                    @classmethod
                    @functools.lru_cache()
                    def any_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            Quota,
                            cls.any_of_1,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'quotas':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            message = schemas.StrSchema
            __annotations__ = {
                "success": success,
                "project_name_or_id": project_name_or_id,
                "cloud": cloud,
                "quotas": quotas,
                "message": message,
            }
    
    cloud: MetaOapg.properties.cloud
    project_name_or_id: MetaOapg.properties.project_name_or_id
    quotas: MetaOapg.properties.quotas
    success: MetaOapg.properties.success
    message: MetaOapg.properties.message
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["success"]) -> MetaOapg.properties.success: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["project_name_or_id"]) -> MetaOapg.properties.project_name_or_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cloud"]) -> MetaOapg.properties.cloud: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["quotas"]) -> MetaOapg.properties.quotas: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["success", "project_name_or_id", "cloud", "quotas", "message", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["success"]) -> MetaOapg.properties.success: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["project_name_or_id"]) -> MetaOapg.properties.project_name_or_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cloud"]) -> MetaOapg.properties.cloud: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["quotas"]) -> MetaOapg.properties.quotas: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["success", "project_name_or_id", "cloud", "quotas", "message", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        cloud: typing.Union[MetaOapg.properties.cloud, str, ],
        project_name_or_id: typing.Union[MetaOapg.properties.project_name_or_id, str, ],
        quotas: typing.Union[MetaOapg.properties.quotas, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        success: typing.Union[MetaOapg.properties.success, bool, ],
        message: typing.Union[MetaOapg.properties.message, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ProjectQuotasResponse':
        return super().__new__(
            cls,
            *args,
            cloud=cloud,
            project_name_or_id=project_name_or_id,
            quotas=quotas,
            success=success,
            message=message,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.quota import Quota
