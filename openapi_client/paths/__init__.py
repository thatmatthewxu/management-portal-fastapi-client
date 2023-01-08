# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from openapi_client.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    API_HEALTH = "/api/health"
    API_ECHO_ = "/api/echo/"
    API_OPENSTACK_PROJECT = "/api/openstack/project"
    API_OPENSTACK_PROJECTS_ALL = "/api/openstack/projects/all"
    API_OPENSTACK_QUOTAS = "/api/openstack/quotas"
    API_OPENSTACK_QUOTAS_ALL = "/api/openstack/quotas/all"
