from typing import Any, cast

from jj.mock import HistoryRequest
from niltype import Nil

from jj_district42.utils import request_to_dict
from revolt import Substitutor

from ._history_request_schema import HistoryRequestSchema

__all__ = ("HistoryRequestSubstitutor",)


class HistoryRequestSubstitutor(Substitutor, extend=True):
    def visit_jj_history_request(self, schema: HistoryRequestSchema, *,
                                 value: Any = Nil, **kwargs: Any) -> HistoryRequestSchema:
        if isinstance(value, HistoryRequest):
            value = request_to_dict(value)
        return cast(HistoryRequestSchema, self.visit_type_alias(schema, value=value, **kwargs))
