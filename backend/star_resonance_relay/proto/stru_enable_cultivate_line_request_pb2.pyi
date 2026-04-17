from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class EnableCultivateLineRequest(_message.Message):
    __slots__ = ("zone_id",)
    ZONE_ID_FIELD_NUMBER: _ClassVar[int]
    zone_id: int
    def __init__(self, zone_id: _Optional[int] = ...) -> None: ...
