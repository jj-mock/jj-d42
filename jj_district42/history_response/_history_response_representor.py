from typing import Any

from district42.representor import Representor

from ._history_response_schema import HistoryResponseSchema

__all__ = ("HistoryResponseRepresentor",)


class HistoryResponseRepresentor(Representor, extend=True):
    def visit_jj_history_response(self, schema: HistoryResponseSchema, *, indent: int = 0, **kwargs: Any) -> str:
        r = f"{self._name}.jj_history_response"
        return r
