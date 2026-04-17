import stru_launch_param_pb2 as _stru_launch_param_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PrivilegeActivateRequest(_message.Message):
    __slots__ = ("launch_param",)
    LAUNCH_PARAM_FIELD_NUMBER: _ClassVar[int]
    launch_param: _stru_launch_param_pb2.LaunchParam
    def __init__(self, launch_param: _Optional[_Union[_stru_launch_param_pb2.LaunchParam, _Mapping]] = ...) -> None: ...
