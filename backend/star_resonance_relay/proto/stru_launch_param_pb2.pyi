import enum_launch_platform_pb2 as _enum_launch_platform_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LaunchParam(_message.Message):
    __slots__ = ("launch_platform", "unique_uid")
    LAUNCH_PLATFORM_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_UID_FIELD_NUMBER: _ClassVar[int]
    launch_platform: _enum_launch_platform_pb2.LaunchPlatform
    unique_uid: str
    def __init__(self, launch_platform: _Optional[_Union[_enum_launch_platform_pb2.LaunchPlatform, str]] = ..., unique_uid: _Optional[str] = ...) -> None: ...
