from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UnionBuilding(_message.Message):
    __slots__ = ("building_id", "building_level", "upgrade_finish_time", "has_speed_up_sec")
    BUILDING_ID_FIELD_NUMBER: _ClassVar[int]
    BUILDING_LEVEL_FIELD_NUMBER: _ClassVar[int]
    UPGRADE_FINISH_TIME_FIELD_NUMBER: _ClassVar[int]
    HAS_SPEED_UP_SEC_FIELD_NUMBER: _ClassVar[int]
    building_id: int
    building_level: int
    upgrade_finish_time: int
    has_speed_up_sec: int
    def __init__(self, building_id: _Optional[int] = ..., building_level: _Optional[int] = ..., upgrade_finish_time: _Optional[int] = ..., has_speed_up_sec: _Optional[int] = ...) -> None: ...
