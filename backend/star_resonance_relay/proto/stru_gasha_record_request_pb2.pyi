from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GashaRecordRequest(_message.Message):
    __slots__ = ("pool_id", "start_id", "count")
    POOL_ID_FIELD_NUMBER: _ClassVar[int]
    START_ID_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    pool_id: int
    start_id: int
    count: int
    def __init__(self, pool_id: _Optional[int] = ..., start_id: _Optional[int] = ..., count: _Optional[int] = ...) -> None: ...
