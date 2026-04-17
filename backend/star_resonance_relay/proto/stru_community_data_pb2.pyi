from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CommunityData(_message.Message):
    __slots__ = ("community_id", "homeland_id", "cohabitant_ids", "last_exit_cohabitation_time", "buy_count", "level")
    COMMUNITY_ID_FIELD_NUMBER: _ClassVar[int]
    HOMELAND_ID_FIELD_NUMBER: _ClassVar[int]
    COHABITANT_IDS_FIELD_NUMBER: _ClassVar[int]
    LAST_EXIT_COHABITATION_TIME_FIELD_NUMBER: _ClassVar[int]
    BUY_COUNT_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    community_id: int
    homeland_id: int
    cohabitant_ids: _containers.RepeatedScalarFieldContainer[int]
    last_exit_cohabitation_time: int
    buy_count: int
    level: int
    def __init__(self, community_id: _Optional[int] = ..., homeland_id: _Optional[int] = ..., cohabitant_ids: _Optional[_Iterable[int]] = ..., last_exit_cohabitation_time: _Optional[int] = ..., buy_count: _Optional[int] = ..., level: _Optional[int] = ...) -> None: ...
