from typing import Any

from jj.mock import HistoryRequest
from niltype import Nil, Nilable
from th import PathHolder

from valera import ValidationResult, Validator

from ._history_request_schema import HistoryRequestSchema

__all__ = ("HistoryRequestValidator",)


class HistoryRequestValidator(Validator, extend=True):
    def visit_jj_history_request(self, schema: HistoryRequestSchema, *,
                                 value: Any = Nil, path: Nilable[PathHolder] = Nil,
                                 **kwargs: Any) -> ValidationResult:
        if isinstance(value, HistoryRequest):
            value = value.to_dict()
        return self.visit_type_alias(schema, value=value, path=path, **kwargs)
