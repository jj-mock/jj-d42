from typing import Any

from blahblah import Generator
from jj.mock import HistoryResponse
from multidict import CIMultiDict, CIMultiDictProxy

from ._history_response_schema import HistoryResponseSchema

__all__ = ("HistoryResponseGenerator",)


class HistoryResponseGenerator(Generator, extend=True):
    def visit_jj_history_response(self, schema: HistoryResponseSchema,
                                  **kwargs: Any) -> HistoryResponse:
        generated = HistoryResponse(
            status=200,
            reason="OK",
            headers=CIMultiDictProxy(CIMultiDict()),
            body=b"",
        )
        return generated
