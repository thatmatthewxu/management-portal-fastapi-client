import typing_extensions

from openapi_client.apis.tags import TagValues
from openapi_client.apis.tags.default_api import DefaultApi
from openapi_client.apis.tags.echo_api import EchoApi
from openapi_client.apis.tags.openstack_api import OpenstackApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.DEFAULT: DefaultApi,
        TagValues.ECHO: EchoApi,
        TagValues.OPENSTACK: OpenstackApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.DEFAULT: DefaultApi,
        TagValues.ECHO: EchoApi,
        TagValues.OPENSTACK: OpenstackApi,
    }
)
