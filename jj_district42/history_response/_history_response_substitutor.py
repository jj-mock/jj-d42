from typing import Any, cast

from jj.mock import HistoryResponse
from niltype import Nil

from revolt import Substitutor

from ._history_response_schema import HistoryResponseSchema

__all__ = ("HistoryResponseSubstitutor",)


class HistoryResponseSubstitutor(Substitutor, extend=True):
    def visit_jj_history_response(self, schema: HistoryResponseSchema, *,
                                  value: Any = Nil, **kwargs: Any) -> HistoryResponseSchema:
        if isinstance(value, HistoryResponse):
            value = value.to_dict()
        return cast(HistoryResponseSchema, self.visit_type_alias(schema, value=value, **kwargs))
