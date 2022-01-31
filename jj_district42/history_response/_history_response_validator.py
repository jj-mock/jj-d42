from typing import Any

from jj.mock import HistoryResponse
from niltype import Nil, Nilable
from th import PathHolder

from jj_district42.utils import response_to_dict
from valera import ValidationResult, Validator

from ._history_response_schema import HistoryResponseSchema

__all__ = ("HistoryResponseValidator",)


class HistoryResponseValidator(Validator, extend=True):
    def visit_jj_history_response(self, schema: HistoryResponseSchema, *,
                                  value: Any = Nil, path: Nilable[PathHolder] = Nil,
                                  **kwargs: Any) -> ValidationResult:
        if isinstance(value, HistoryResponse):
            value = response_to_dict(value)
        return self.visit_type_alias(schema, value=value, path=path, **kwargs)
