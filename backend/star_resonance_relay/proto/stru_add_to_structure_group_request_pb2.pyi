from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AddToStructureGroupRequest(_message.Message):
    __slots__ = ("group_id", "structure_ids", "is_outer", "group_name")
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    STRUCTURE_IDS_FIELD_NUMBER: _ClassVar[int]
    IS_OUTER_FIELD_NUMBER: _ClassVar[int]
    GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    structure_ids: _containers.RepeatedScalarFieldContainer[int]
    is_outer: bool
    group_name: str
    def __init__(self, group_id: _Optional[int] = ..., structure_ids: _Optional[_Iterable[int]] = ..., is_outer: bool = ..., group_name: _Optional[str] = ...) -> None: ...
