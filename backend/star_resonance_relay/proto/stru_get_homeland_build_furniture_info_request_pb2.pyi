from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetHomelandBuildFurnitureInfoRequest(_message.Message):
    __slots__ = ("build_type",)
    BUILD_TYPE_FIELD_NUMBER: _ClassVar[int]
    build_type: int
    def __init__(self, build_type: _Optional[int] = ...) -> None: ...
