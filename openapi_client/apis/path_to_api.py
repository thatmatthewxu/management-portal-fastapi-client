import typing_extensions

from openapi_client.paths import PathValues
from openapi_client.apis.paths.api_health import ApiHealth
from openapi_client.apis.paths.api_echo_ import ApiEcho
from openapi_client.apis.paths.api_openstack_project import ApiOpenstackProject
from openapi_client.apis.paths.api_openstack_projects_all import ApiOpenstackProjectsAll
from openapi_client.apis.paths.api_openstack_quotas import ApiOpenstackQuotas
from openapi_client.apis.paths.api_openstack_quotas_all import ApiOpenstackQuotasAll

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.API_HEALTH: ApiHealth,
        PathValues.API_ECHO_: ApiEcho,
        PathValues.API_OPENSTACK_PROJECT: ApiOpenstackProject,
        PathValues.API_OPENSTACK_PROJECTS_ALL: ApiOpenstackProjectsAll,
        PathValues.API_OPENSTACK_QUOTAS: ApiOpenstackQuotas,
        PathValues.API_OPENSTACK_QUOTAS_ALL: ApiOpenstackQuotasAll,
    }
)

path_to_api = PathToApi(
    {
        PathValues.API_HEALTH: ApiHealth,
        PathValues.API_ECHO_: ApiEcho,
        PathValues.API_OPENSTACK_PROJECT: ApiOpenstackProject,
        PathValues.API_OPENSTACK_PROJECTS_ALL: ApiOpenstackProjectsAll,
        PathValues.API_OPENSTACK_QUOTAS: ApiOpenstackQuotas,
        PathValues.API_OPENSTACK_QUOTAS_ALL: ApiOpenstackQuotasAll,
    }
)
