from typing import Any

from jj.mock import HistoryResponse

from blahblah import Generator

from ._history_response_schema import HistoryResponseSchema

__all__ = ("HistoryResponseGenerator",)


class HistoryResponseGenerator(Generator, extend=True):
    def visit_jj_history_response(self,
                                  schema: HistoryResponseSchema,
                                  **kwargs: Any) -> HistoryResponse:
        generated = self.visit_type_alias(schema, **kwargs)
        return HistoryResponse(**generated)
