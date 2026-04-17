from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyBuildingUpgradeEndRequest(_message.Message):
    __slots__ = ("building_id", "build_level")
    BUILDING_ID_FIELD_NUMBER: _ClassVar[int]
    BUILD_LEVEL_FIELD_NUMBER: _ClassVar[int]
    building_id: int
    build_level: int
    def __init__(self, building_id: _Optional[int] = ..., build_level: _Optional[int] = ...) -> None: ...
