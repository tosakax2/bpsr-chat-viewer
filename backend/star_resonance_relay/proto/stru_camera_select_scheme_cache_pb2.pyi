import stru_camera_scheme_info_pb2 as _stru_camera_scheme_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class cameraSelectSchemeCache(_message.Message):
    __slots__ = ("camera_scheme_cache",)
    CAMERA_SCHEME_CACHE_FIELD_NUMBER: _ClassVar[int]
    camera_scheme_cache: _stru_camera_scheme_info_pb2.cameraSchemeInfo
    def __init__(self, camera_scheme_cache: _Optional[_Union[_stru_camera_scheme_info_pb2.cameraSchemeInfo, _Mapping]] = ...) -> None: ...
