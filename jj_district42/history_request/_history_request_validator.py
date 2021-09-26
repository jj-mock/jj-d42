from typing import Any

from niltype import Nil, Nilable
from th import PathHolder
from valera import ValidationResult, Validator

from ._history_request_schema import HistoryRequestSchema

__all__ = ("HistoryRequestValidator",)


class HistoryRequestValidator(Validator, extend=True):
    def visit_jj_history_request(self, schema: HistoryRequestSchema, *,
                                 value: Any = Nil, path: Nilable[PathHolder] = Nil,
                                 **kwargs: Any) -> ValidationResult:
        result = self._validation_result_factory()
        if path is Nil:
            path = self._path_holder_factory()
        return result
