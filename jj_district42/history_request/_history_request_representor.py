from typing import Any

from district42.representor import Representor

from ._history_request_schema import HistoryRequestSchema

__all__ = ("HistoryRequestRepresentor",)


class HistoryRequestRepresentor(Representor, extend=True):
    def visit_jj_history_request(self, schema: HistoryRequestSchema, *, indent: int = 0, **kwargs: Any) -> str:
        r = f"{self._name}.jj_history_request"
        return r
