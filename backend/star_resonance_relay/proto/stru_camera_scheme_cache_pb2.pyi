import stru_camera_scheme_info_pb2 as _stru_camera_scheme_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class cameraSchemeCache(_message.Message):
    __slots__ = ("camera_scheme_dict",)
    class CameraSchemeDictEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _stru_camera_scheme_info_pb2.cameraSchemeInfo
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_stru_camera_scheme_info_pb2.cameraSchemeInfo, _Mapping]] = ...) -> None: ...
    CAMERA_SCHEME_DICT_FIELD_NUMBER: _ClassVar[int]
    camera_scheme_dict: _containers.MessageMap[str, _stru_camera_scheme_info_pb2.cameraSchemeInfo]
    def __init__(self, camera_scheme_dict: _Optional[_Mapping[str, _stru_camera_scheme_info_pb2.cameraSchemeInfo]] = ...) -> None: ...
