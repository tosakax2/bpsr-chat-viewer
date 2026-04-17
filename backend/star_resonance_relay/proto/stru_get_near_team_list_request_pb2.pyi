from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetNearTeamListRequest(_message.Message):
    __slots__ = ("map_id", "is_refresh", "member_count", "ignore_self_talent")
    MAP_ID_FIELD_NUMBER: _ClassVar[int]
    IS_REFRESH_FIELD_NUMBER: _ClassVar[int]
    MEMBER_COUNT_FIELD_NUMBER: _ClassVar[int]
    IGNORE_SELF_TALENT_FIELD_NUMBER: _ClassVar[int]
    map_id: int
    is_refresh: bool
    member_count: int
    ignore_self_talent: bool
    def __init__(self, map_id: _Optional[int] = ..., is_refresh: bool = ..., member_count: _Optional[int] = ..., ignore_self_talent: bool = ...) -> None: ...
