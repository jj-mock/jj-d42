from typing import Any

from jj.mock import HistoryRequest
from niltype import Nil, Nilable
from th import PathHolder

from jj_district42.utils import request_to_dict
from valera import ValidationResult, Validator

from ._history_request_schema import HistoryRequestSchema

__all__ = ("HistoryRequestValidator",)


class HistoryRequestValidator(Validator, extend=True):
    def visit_jj_history_request(self, schema: HistoryRequestSchema, *,
                                 value: Any = Nil, path: Nilable[PathHolder] = Nil,
                                 **kwargs: Any) -> ValidationResult:
        if isinstance(value, HistoryRequest):
            value = request_to_dict(value)
        return self.visit_type_alias(schema, value=value, path=path, **kwargs)
