from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CommunityBuildFurnitureSimpleInfo(_message.Message):
    __slots__ = ("build_uuid", "furniture_id", "end_time")
    BUILD_UUID_FIELD_NUMBER: _ClassVar[int]
    FURNITURE_ID_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    build_uuid: int
    furniture_id: int
    end_time: int
    def __init__(self, build_uuid: _Optional[int] = ..., furniture_id: _Optional[int] = ..., end_time: _Optional[int] = ...) -> None: ...
