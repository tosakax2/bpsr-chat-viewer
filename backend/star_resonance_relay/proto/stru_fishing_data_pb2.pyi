from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FishingData(_message.Message):
    __slots__ = ("rod_id", "area_id", "fish_id", "stage", "is_get_fish", "size")
    ROD_ID_FIELD_NUMBER: _ClassVar[int]
    AREA_ID_FIELD_NUMBER: _ClassVar[int]
    FISH_ID_FIELD_NUMBER: _ClassVar[int]
    STAGE_FIELD_NUMBER: _ClassVar[int]
    IS_GET_FISH_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    rod_id: int
    area_id: int
    fish_id: int
    stage: int
    is_get_fish: bool
    size: int
    def __init__(self, rod_id: _Optional[int] = ..., area_id: _Optional[int] = ..., fish_id: _Optional[int] = ..., stage: _Optional[int] = ..., is_get_fish: bool = ..., size: _Optional[int] = ...) -> None: ...
