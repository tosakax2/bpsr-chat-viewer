from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CommunityKickPlayerRequest(_message.Message):
    __slots__ = ("community_id", "homeland_id", "char_ids", "is_outer")
    COMMUNITY_ID_FIELD_NUMBER: _ClassVar[int]
    HOMELAND_ID_FIELD_NUMBER: _ClassVar[int]
    CHAR_IDS_FIELD_NUMBER: _ClassVar[int]
    IS_OUTER_FIELD_NUMBER: _ClassVar[int]
    community_id: int
    homeland_id: int
    char_ids: _containers.RepeatedScalarFieldContainer[int]
    is_outer: bool
    def __init__(self, community_id: _Optional[int] = ..., homeland_id: _Optional[int] = ..., char_ids: _Optional[_Iterable[int]] = ..., is_outer: bool = ...) -> None: ...
