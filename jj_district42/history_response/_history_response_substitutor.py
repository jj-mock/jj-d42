from typing import Any

from niltype import Nil
from revolt import Substitutor

from ._history_response_schema import HistoryResponseSchema

__all__ = ("HistoryResponseSubstitutor",)


class HistoryResponseSubstitutor(Substitutor, extend=True):
    def visit_jj_history_response(self, schema: HistoryResponseSchema, *,
                                  value: Any = Nil, **kwargs: Any) -> HistoryResponseSchema:
        return schema
