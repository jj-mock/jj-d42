from uuid import uuid4

import jj
import httpx
from d42 import schema, validate_or_fail
from jj.mock import mocked
from jj_d42 import HistoryItemSchema


HistoryItemSchema = HistoryItemSchema + schema.dict({
    "request": schema.jj_history_request + schema.dict({
        "params": schema.unordered([
            schema.list([
                schema.str("access_token"),
                schema.uuid_str,
            ])
        ])
    })
})
HistorySchema = schema.list(HistoryItemSchema)

matcher = jj.match("*", "/users")
response = jj.Response(status=200, json=[])

with mocked(matcher, response) as mock:
    access_token = str(uuid4())
    resp = httpx.get("http://localhost:8080/users", params={"access_token": access_token})

assert validate_or_fail(
    HistorySchema % [
        {
            "request": {
                "method": "GET",
                "path": "/users",
            }
        }
    ],
    mock.history
)
