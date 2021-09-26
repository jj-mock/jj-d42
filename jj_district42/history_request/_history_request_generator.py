from typing import Any

from blahblah import Generator
from jj.mock import HistoryRequest
from multidict import CIMultiDict, CIMultiDictProxy, MultiDict, MultiDictProxy

from ._history_request_schema import HistoryRequestSchema

__all__ = ("HistoryRequestGenerator",)


class HistoryRequestGenerator(Generator, extend=True):
    def visit_jj_history_request(self, schema: HistoryRequestSchema, **kwargs: Any) -> HistoryRequest:
        generated = HistoryRequest(
            method="GET",
            path="/",
            segments={},
            params=MultiDictProxy(MultiDict()),
            headers=CIMultiDictProxy(CIMultiDict()),
            body=b"",
        )
        return generated
