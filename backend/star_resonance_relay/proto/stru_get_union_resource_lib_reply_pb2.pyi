import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_union_resource_pb2 as _stru_union_resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetUnionResourceLibReply(_message.Message):
    __slots__ = ("union_resource_lib", "err_code")
    class UnionResourceLibEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_union_resource_pb2.UnionResource
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_union_resource_pb2.UnionResource, _Mapping]] = ...) -> None: ...
    UNION_RESOURCE_LIB_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    union_resource_lib: _containers.MessageMap[int, _stru_union_resource_pb2.UnionResource]
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, union_resource_lib: _Optional[_Mapping[int, _stru_union_resource_pb2.UnionResource]] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
