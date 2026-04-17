import stru_int_vec3_pb2 as _stru_int_vec3_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FashionColorInfo(_message.Message):
    __slots__ = ("id", "colors", "attachment_color")
    class ColorsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_int_vec3_pb2.IntVec3
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_int_vec3_pb2.IntVec3, _Mapping]] = ...) -> None: ...
    class AttachmentColorEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_int_vec3_pb2.IntVec3
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_int_vec3_pb2.IntVec3, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    COLORS_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_COLOR_FIELD_NUMBER: _ClassVar[int]
    id: int
    colors: _containers.MessageMap[int, _stru_int_vec3_pb2.IntVec3]
    attachment_color: _containers.MessageMap[int, _stru_int_vec3_pb2.IntVec3]
    def __init__(self, id: _Optional[int] = ..., colors: _Optional[_Mapping[int, _stru_int_vec3_pb2.IntVec3]] = ..., attachment_color: _Optional[_Mapping[int, _stru_int_vec3_pb2.IntVec3]] = ...) -> None: ...
