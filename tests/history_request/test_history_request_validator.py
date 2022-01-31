from baby_steps import given, then, when

from jj_district42 import HistoryRequestSchema
from valera import validate

from ._utils import make_history_request


def test_request_history_type_validation():
    with given:
        sch = HistoryRequestSchema()
        req = make_history_request()

    with when:
        result = validate(sch, req)

    with then:
        assert result.get_errors() == []
