from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CommunityBuildFurnitureReceiveRequest(_message.Message):
    __slots__ = ("build_uuid", "is_all")
    BUILD_UUID_FIELD_NUMBER: _ClassVar[int]
    IS_ALL_FIELD_NUMBER: _ClassVar[int]
    build_uuid: int
    is_all: bool
    def __init__(self, build_uuid: _Optional[int] = ..., is_all: bool = ...) -> None: ...
