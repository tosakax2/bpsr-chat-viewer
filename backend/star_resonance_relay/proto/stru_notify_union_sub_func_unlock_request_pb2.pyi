import enum_union_sub_func_pb2 as _enum_union_sub_func_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyUnionSubFuncUnlockRequest(_message.Message):
    __slots__ = ("sub_func_type",)
    SUB_FUNC_TYPE_FIELD_NUMBER: _ClassVar[int]
    sub_func_type: _enum_union_sub_func_pb2.UnionSubFunc
    def __init__(self, sub_func_type: _Optional[_Union[_enum_union_sub_func_pb2.UnionSubFunc, str]] = ...) -> None: ...
