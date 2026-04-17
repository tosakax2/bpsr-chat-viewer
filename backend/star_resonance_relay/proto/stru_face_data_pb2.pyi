import stru_int_vec3_pb2 as _stru_int_vec3_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FaceData(_message.Message):
    __slots__ = ("face_info", "color_info", "height", "body_size", "voice_id")
    class FaceInfoEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class ColorInfoEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_int_vec3_pb2.IntVec3
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_int_vec3_pb2.IntVec3, _Mapping]] = ...) -> None: ...
    FACE_INFO_FIELD_NUMBER: _ClassVar[int]
    COLOR_INFO_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    BODY_SIZE_FIELD_NUMBER: _ClassVar[int]
    VOICE_ID_FIELD_NUMBER: _ClassVar[int]
    face_info: _containers.ScalarMap[int, int]
    color_info: _containers.MessageMap[int, _stru_int_vec3_pb2.IntVec3]
    height: float
    body_size: int
    voice_id: int
    def __init__(self, face_info: _Optional[_Mapping[int, int]] = ..., color_info: _Optional[_Mapping[int, _stru_int_vec3_pb2.IntVec3]] = ..., height: _Optional[float] = ..., body_size: _Optional[int] = ..., voice_id: _Optional[int] = ...) -> None: ...
