# coding: utf-8

"""
    core

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""

from openapi_client.paths.api_openstack_quotas_all.get import GetAllProjectsAndQuotasApiOpenstackQuotasAllGet
from openapi_client.paths.api_openstack_projects_all.get import GetAllProjectsApiOpenstackProjectsAllGet
from openapi_client.paths.api_openstack_project.get import GetProjectByNameOrIdApiOpenstackProjectGet
from openapi_client.paths.api_openstack_quotas.get import GetProjectQuotasByNameOrIdApiOpenstackQuotasGet


class OpenstackApi(
    GetAllProjectsAndQuotasApiOpenstackQuotasAllGet,
    GetAllProjectsApiOpenstackProjectsAllGet,
    GetProjectByNameOrIdApiOpenstackProjectGet,
    GetProjectQuotasByNameOrIdApiOpenstackQuotasGet,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
