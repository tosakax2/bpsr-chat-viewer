import enum_launch_platform_pb2 as _enum_launch_platform_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PrivilegeData(_message.Message):
    __slots__ = ("launch_platform", "is_privilege", "last_update_time")
    LAUNCH_PLATFORM_FIELD_NUMBER: _ClassVar[int]
    IS_PRIVILEGE_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    launch_platform: _enum_launch_platform_pb2.LaunchPlatform
    is_privilege: bool
    last_update_time: int
    def __init__(self, launch_platform: _Optional[_Union[_enum_launch_platform_pb2.LaunchPlatform, str]] = ..., is_privilege: bool = ..., last_update_time: _Optional[int] = ...) -> None: ...
