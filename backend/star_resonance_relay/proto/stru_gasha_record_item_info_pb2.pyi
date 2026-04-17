from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GashaRecordItemInfo(_message.Message):
    __slots__ = ("config_id", "count", "time", "quality")
    CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    QUALITY_FIELD_NUMBER: _ClassVar[int]
    config_id: int
    count: int
    time: int
    quality: int
    def __init__(self, config_id: _Optional[int] = ..., count: _Optional[int] = ..., time: _Optional[int] = ..., quality: _Optional[int] = ...) -> None: ...
