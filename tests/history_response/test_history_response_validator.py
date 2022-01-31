from baby_steps import given, then, when

from jj_district42 import HistoryResponseSchema
from valera import validate

from ._utils import make_history_response


def test_response_history_type_validation():
    with given:
        sch = HistoryResponseSchema()
        req = make_history_response()

    with when:
        result = validate(sch, req)

    with then:
        assert result.get_errors() == []
