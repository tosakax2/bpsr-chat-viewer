import stru_union_official_pb2 as _stru_union_official_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyUnionOfficialChangeRequest(_message.Message):
    __slots__ = ("union_official", "change_type")
    UNION_OFFICIAL_FIELD_NUMBER: _ClassVar[int]
    CHANGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    union_official: _stru_union_official_pb2.UnionOfficial
    change_type: int
    def __init__(self, union_official: _Optional[_Union[_stru_union_official_pb2.UnionOfficial, _Mapping]] = ..., change_type: _Optional[int] = ...) -> None: ...
