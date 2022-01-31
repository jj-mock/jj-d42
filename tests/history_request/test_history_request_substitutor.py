from baby_steps import given, then, when

from jj_district42 import HistoryRequestSchema
from revolt import substitute


def test_history_request_substitution():
    with given:
        sch = HistoryRequestSchema()

    with when:
        res = substitute(sch, {})

    with then:
        assert id(res) != id(sch)
