from typing import Any

from niltype import Nil
from revolt import Substitutor

from ._history_request_schema import HistoryRequestSchema

__all__ = ("HistoryRequestSubstitutor",)


class HistoryRequestSubstitutor(Substitutor, extend=True):
    def visit_jj_history_request(self, schema: HistoryRequestSchema, *,
                                 value: Any = Nil, **kwargs: Any) -> HistoryRequestSchema:
        return schema
