from typing import Any, Dict

from jj.mock import HistoryRequest, HistoryResponse

__all__ = ("request_to_dict", "response_to_dict",)


def request_to_dict(request: HistoryRequest) -> Dict[str, Any]:
    params = [[key, val] for key, val in request.params.items()]
    headers = [[key, val] for key, val in request.headers.items()]
    return {
        "method": request.method,
        "path": request.path,
        "segments": request.segments,
        "params": params,
        "headers": headers,
        "body": request.body,
    }


def response_to_dict(response: HistoryResponse) -> Dict[str, Any]:
    headers = [[key, val] for key, val in response.headers.items()]
    return {
        "status": response.status,
        "reason": response.reason,
        "headers": headers,
        "body": response.body,
    }
