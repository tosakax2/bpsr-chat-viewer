from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TeamMemberGroupInfo(_message.Message):
    __slots__ = ("group_id", "char_ids")
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    CHAR_IDS_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    char_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, group_id: _Optional[int] = ..., char_ids: _Optional[_Iterable[int]] = ...) -> None: ...
