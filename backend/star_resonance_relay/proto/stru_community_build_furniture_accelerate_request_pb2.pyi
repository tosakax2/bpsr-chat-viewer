from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CommunityBuildFurnitureAccelerateRequest(_message.Message):
    __slots__ = ("build_uuid", "count")
    BUILD_UUID_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    build_uuid: int
    count: int
    def __init__(self, build_uuid: _Optional[int] = ..., count: _Optional[int] = ...) -> None: ...
