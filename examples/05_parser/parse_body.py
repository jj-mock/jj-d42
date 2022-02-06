from jj.mock import HistoryItem, default_history_adapter
import xmltodict


def parse_body(item: HistoryItem) -> HistoryItem:
    content_type = item["request"].headers.get("Content-Type", "")
    if content_type.lower().startswith("application/xml"):
        try:
            body = xmltodict.parse(item["request"].raw)
        except:
            pass
        else:
            item["request"] = item["request"].from_dict({
                **item["request"].to_dict(),
                "body": body
            })
            return item

    return default_history_adapter(item)
