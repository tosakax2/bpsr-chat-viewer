import stru_union_official_pb2 as _stru_union_official_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReqChangeOfficialsRequest(_message.Message):
    __slots__ = ("union_id", "change_officials", "change_type")
    UNION_ID_FIELD_NUMBER: _ClassVar[int]
    CHANGE_OFFICIALS_FIELD_NUMBER: _ClassVar[int]
    CHANGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    union_id: int
    change_officials: _containers.RepeatedCompositeFieldContainer[_stru_union_official_pb2.UnionOfficial]
    change_type: int
    def __init__(self, union_id: _Optional[int] = ..., change_officials: _Optional[_Iterable[_Union[_stru_union_official_pb2.UnionOfficial, _Mapping]]] = ..., change_type: _Optional[int] = ...) -> None: ...
