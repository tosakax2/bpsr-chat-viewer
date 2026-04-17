from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetMahjongInfoRequest(_message.Message):
    __slots__ = ("notify_world", "table_guid")
    NOTIFY_WORLD_FIELD_NUMBER: _ClassVar[int]
    TABLE_GUID_FIELD_NUMBER: _ClassVar[int]
    notify_world: int
    table_guid: str
    def __init__(self, notify_world: _Optional[int] = ..., table_guid: _Optional[str] = ...) -> None: ...
