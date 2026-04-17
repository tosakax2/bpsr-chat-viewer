import enum_launch_platform_pb2 as _enum_launch_platform_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LaunchPrivilegeData(_message.Message):
    __slots__ = ("launch_platform", "is_privilege", "bak_launch_platform", "bak_privilege")
    LAUNCH_PLATFORM_FIELD_NUMBER: _ClassVar[int]
    IS_PRIVILEGE_FIELD_NUMBER: _ClassVar[int]
    BAK_LAUNCH_PLATFORM_FIELD_NUMBER: _ClassVar[int]
    BAK_PRIVILEGE_FIELD_NUMBER: _ClassVar[int]
    launch_platform: _enum_launch_platform_pb2.LaunchPlatform
    is_privilege: bool
    bak_launch_platform: _enum_launch_platform_pb2.LaunchPlatform
    bak_privilege: bool
    def __init__(self, launch_platform: _Optional[_Union[_enum_launch_platform_pb2.LaunchPlatform, str]] = ..., is_privilege: bool = ..., bak_launch_platform: _Optional[_Union[_enum_launch_platform_pb2.LaunchPlatform, str]] = ..., bak_privilege: bool = ...) -> None: ...
