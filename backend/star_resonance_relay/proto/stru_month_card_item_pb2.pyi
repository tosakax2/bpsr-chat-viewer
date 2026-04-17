from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MonthCardItem(_message.Message):
    __slots__ = ("item_id", "create_time")
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    item_id: int
    create_time: int
    def __init__(self, item_id: _Optional[int] = ..., create_time: _Optional[int] = ...) -> None: ...
