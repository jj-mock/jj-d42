from baby_steps import given, then, when
from jj.mock import HistoryRequest

from blahblah import generate
from jj_district42 import HistoryRequestSchema


def test_history_request_generation():
    with given:
        sch = HistoryRequestSchema()

    with when:
        res = generate(sch)

    with then:
        assert isinstance(res, HistoryRequest)
