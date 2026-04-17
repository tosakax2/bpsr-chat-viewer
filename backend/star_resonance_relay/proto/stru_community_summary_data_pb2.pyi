from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CommunitySummaryData(_message.Message):
    __slots__ = ("community_id", "homeland_id", "is_single", "last_exit_cohabitation_time")
    COMMUNITY_ID_FIELD_NUMBER: _ClassVar[int]
    HOMELAND_ID_FIELD_NUMBER: _ClassVar[int]
    IS_SINGLE_FIELD_NUMBER: _ClassVar[int]
    LAST_EXIT_COHABITATION_TIME_FIELD_NUMBER: _ClassVar[int]
    community_id: int
    homeland_id: int
    is_single: bool
    last_exit_cohabitation_time: int
    def __init__(self, community_id: _Optional[int] = ..., homeland_id: _Optional[int] = ..., is_single: bool = ..., last_exit_cohabitation_time: _Optional[int] = ...) -> None: ...
