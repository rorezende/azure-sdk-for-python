# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------

from datetime import datetime

from azure.core import MatchConditions
from azure.core.tracing.decorator import distributed_trace
from msrest import Serializer

from . import VERSION
from ._generated import AzureAppConfiguration
from ._models import ConfigurationSetting
from ._utils import get_match_headers


class AppConfigurationClient(object):
    """A Client for the AppConfiguration Service.
    
    :param str account_url: The URL for the service.
    :param TokenCredential credential: The credentials to authenticate with the service.
    """

    def __init__(self, account_url, credential, **kwargs):
        # type: (str, TokenCredential) -> None

        try:
            if not account_url.lower().startswith('http'):
                full_url = "https://" + account_url
            else:
                full_url = account_url
        except AttributeError:
            raise ValueError("Base URL must be a string.")

        user_agent_moniker = "learnappconfig/{}".format(VERSION)

        self._client = AzureAppConfiguration(
            credential=credential,
            endpoint=full_url,
            credential_scopes=[full_url.strip("/") + "/.default"],
            sdk_moniker=user_agent_moniker,
            **kwargs)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> AppConfigurationClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)

    @classmethod
    def from_connection_string(cls, connection_string, **kwargs):
        # type: (str) -> AppConfigurationClient
        """Build an AppConfigurationClient from a connection string.

        :param str connection_string: A connection string, as retrieved
         from the Azure portal.
        """
        pass

    @distributed_trace
    def get_configuration_setting(self, key, label=None, **kwargs):
        # type: (str, Optional[str]) -> ConfigurationSetting
        """Get the value of a particular configuration settings.

        :param str key: The key name of the setting.
        :param str label: The label of the setting.
        :keyword datetime accept_datetime: The last modified date filter.
        :keyword select: The specific properties of the setting that should be returned.
        :paramtype select: List[Union[str, ~azure.learnappconfig.SettingFields]]
        :raises ~azure.core.exceptions.ResourceNotFoundError: If no matching configuration setting exists.
        """
        etag = kwargs.get('etag', None)
        label = kwargs.get('label', None)
        select = kwargs.get('select', None)
        match_condition = kwargs.get('match_condition', None)
        if_match, if_none_match = get_match_headers(etag, match_condition)

        accept_datetime = kwargs.pop('accept_datetime', None)
        if isinstance(accept_datetime, datetime):
            accept_datetime = Serializer.serialize_rfc(accept_datetime)
        result = self._client.get_key_value(
            key=key,
            label=label,
            if_match=if_match,
            if_none_match=if_none_match,
            select=select,
            accept_datetime=accept_datetime,
            **kwargs)

        return ConfigurationSetting(
            key=result.key,
            label=result.label,
            value=result.value,
            etag=result.etag,
            last_modified=result.last_modified,
            read_only=result.locked,
            content_type=result.content_type,
            tags=result.tags
        )
