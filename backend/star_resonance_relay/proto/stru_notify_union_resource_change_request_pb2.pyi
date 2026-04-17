import stru_union_resource_pb2 as _stru_union_resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyUnionResourceChangeRequest(_message.Message):
    __slots__ = ("change_resource_lib", "donor_mem_id")
    class ChangeResourceLibEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_union_resource_pb2.UnionResource
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_union_resource_pb2.UnionResource, _Mapping]] = ...) -> None: ...
    CHANGE_RESOURCE_LIB_FIELD_NUMBER: _ClassVar[int]
    DONOR_MEM_ID_FIELD_NUMBER: _ClassVar[int]
    change_resource_lib: _containers.MessageMap[int, _stru_union_resource_pb2.UnionResource]
    donor_mem_id: int
    def __init__(self, change_resource_lib: _Optional[_Mapping[int, _stru_union_resource_pb2.UnionResource]] = ..., donor_mem_id: _Optional[int] = ...) -> None: ...
