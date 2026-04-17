import stru_device_info_pb2 as _stru_device_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExitGameRequest(_message.Message):
    __slots__ = ("device_info",)
    DEVICE_INFO_FIELD_NUMBER: _ClassVar[int]
    device_info: _stru_device_info_pb2.DeviceInfo
    def __init__(self, device_info: _Optional[_Union[_stru_device_info_pb2.DeviceInfo, _Mapping]] = ...) -> None: ...
