# jj-d42

[![Codecov](https://img.shields.io/codecov/c/github/jj-mock/jj-d42/master.svg?style=flat-square)](https://codecov.io/gh/jj-mock/jj-d42)
[![PyPI](https://img.shields.io/pypi/v/jj-d42.svg?style=flat-square)](https://pypi.python.org/pypi/jj-d42/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/jj-d42?style=flat-square)](https://pypi.python.org/pypi/jj-d42/)
[![Python Version](https://img.shields.io/pypi/pyversions/jj-d42.svg?style=flat-square)](https://pypi.python.org/pypi/jj-d42/)


## Installation

```sh
pip3 install jj-d42
```

## Usage

```python
import jj
import httpx
from jj.mock import mocked
from jj_d42 import HistorySchema
from d42 import validate_or_fail


matcher = jj.match("GET", "/users")
response = jj.Response(status=200, json=[])

with mocked(matcher, response) as mock:
    resp = httpx.get("http://localhost:8080/users", params={"user_id": 1})

assert validate_or_fail(
    HistorySchema % [
        {
            "request": {
                "method": "GET",
                "path": "/users",
                "params": {"user_id": "1"},
            }
        }
    ],
    mock.history
)
```

More examples are available [here](https://github.com/jj-mock/jj-d42/tree/master/examples)
