# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import Action
    from ._models_py3 import Answer
    from ._models_py3 import CreativeWork
    from ._models_py3 import Error
    from ._models_py3 import ErrorResponse, ErrorResponseException
    from ._models_py3 import Identifiable
    from ._models_py3 import QueryContext
    from ._models_py3 import Response
    from ._models_py3 import ResponseBase
    from ._models_py3 import SearchAction
    from ._models_py3 import SearchResultsAnswer
    from ._models_py3 import Suggestions
    from ._models_py3 import SuggestionsSuggestionGroup
    from ._models_py3 import Thing
except (SyntaxError, ImportError):
    from ._models import Action
    from ._models import Answer
    from ._models import CreativeWork
    from ._models import Error
    from ._models import ErrorResponse, ErrorResponseException
    from ._models import Identifiable
    from ._models import QueryContext
    from ._models import Response
    from ._models import ResponseBase
    from ._models import SearchAction
    from ._models import SearchResultsAnswer
    from ._models import Suggestions
    from ._models import SuggestionsSuggestionGroup
    from ._models import Thing
from ._auto_suggest_client_enums import (
    ErrorCode,
    ResponseFormat,
    SafeSearch,
    ScenarioType,
    SearchKind,
)

__all__ = [
    'Action',
    'Answer',
    'CreativeWork',
    'Error',
    'ErrorResponse', 'ErrorResponseException',
    'Identifiable',
    'QueryContext',
    'Response',
    'ResponseBase',
    'SearchAction',
    'SearchResultsAnswer',
    'Suggestions',
    'SuggestionsSuggestionGroup',
    'Thing',
    'ScenarioType',
    'SearchKind',
    'ErrorCode',
    'SafeSearch',
    'ResponseFormat',
]
