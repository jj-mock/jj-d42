from typing import Any, cast

from d42 import schema
from d42.declaration import SchemaVisitor
from d42.declaration import SchemaVisitorReturnType as ReturnType
from d42.declaration.types import DictSchema, GenericTypeAliasSchema, TypeAliasProps

from jj_d42.types.header_list import HeaderListSchema
from jj_d42.types.param_list import ParamListSchema

__all__ = ("HistoryRequestSchema", "HistoryRequestProps", "RequestSchema",)


RequestSchema = schema.dict({
    "method": schema.str.len(1, ...),
    "path": schema.str,
    "segments": schema.dict,
    "params": ParamListSchema(),
    "headers": HeaderListSchema(),
    "body": schema.any,
    "raw": schema.bytes,
})


class HistoryRequestProps(TypeAliasProps):
    @property
    def type(self) -> DictSchema:
        return cast(DictSchema, self.get("type", RequestSchema))


class HistoryRequestSchema(GenericTypeAliasSchema[HistoryRequestProps]):
    def __accept__(self, visitor: SchemaVisitor[ReturnType], **kwargs: Any) -> ReturnType:
        try:
            return cast(ReturnType, visitor.visit_jj_history_request(self, **kwargs))
        except AttributeError:
            return visitor.visit_type_alias(self, **kwargs)

    def __add__(self, /, other: DictSchema) -> "HistoryRequestSchema":
        assert isinstance(other, DictSchema)
        merged = self.props.type + other
        return self.__class__(self.props.update(type=merged))
