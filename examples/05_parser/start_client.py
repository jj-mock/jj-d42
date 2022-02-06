import jj
import httpx
from jj.mock import mocked
from jj_district42 import HistorySchema
from valera import validate_or_fail

from parse_body import parse_body


matcher = jj.match("*", "/users")
response = jj.Response(status=200, json=[])

with mocked(matcher, response, history_adapter=parse_body) as mock:
    payload = """
        <user>
            <id>1</id>
            <name>Bob</name>
        </user>
    """
    resp = httpx.post("http://localhost:8080/users", data=payload, headers={
        "Content-Type": "application/xml"
    })

assert validate_or_fail(
    HistorySchema % [
        {
            "request": {
                "method": "POST",
                "path": "/users",
                "body": {
                    "user": {
                        "id": "1",
                        "name": "Bob",
                    }
                }
            }
        }
    ],
    mock.history
)
