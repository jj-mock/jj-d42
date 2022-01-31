from baby_steps import given, then, when

from jj_district42 import HistoryResponseSchema
from revolt import substitute


def test_history_response_substitution():
    with given:
        sch = HistoryResponseSchema()

    with when:
        res = substitute(sch, {})

    with then:
        assert id(res) != id(sch)
