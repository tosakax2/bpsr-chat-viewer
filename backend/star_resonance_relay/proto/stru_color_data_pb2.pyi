import stru_int_vec3_pb2 as _stru_int_vec3_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ColorData(_message.Message):
    __slots__ = ("color_dict", "reset_dict", "attachment_color", "attachment_reset")
    class ColorDictEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_int_vec3_pb2.IntVec3
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_int_vec3_pb2.IntVec3, _Mapping]] = ...) -> None: ...
    class ResetDictEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bool
        def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
    class AttachmentColorEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_int_vec3_pb2.IntVec3
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_int_vec3_pb2.IntVec3, _Mapping]] = ...) -> None: ...
    class AttachmentResetEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bool
        def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
    COLOR_DICT_FIELD_NUMBER: _ClassVar[int]
    RESET_DICT_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_COLOR_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_RESET_FIELD_NUMBER: _ClassVar[int]
    color_dict: _containers.MessageMap[int, _stru_int_vec3_pb2.IntVec3]
    reset_dict: _containers.ScalarMap[int, bool]
    attachment_color: _containers.MessageMap[int, _stru_int_vec3_pb2.IntVec3]
    attachment_reset: _containers.ScalarMap[int, bool]
    def __init__(self, color_dict: _Optional[_Mapping[int, _stru_int_vec3_pb2.IntVec3]] = ..., reset_dict: _Optional[_Mapping[int, bool]] = ..., attachment_color: _Optional[_Mapping[int, _stru_int_vec3_pb2.IntVec3]] = ..., attachment_reset: _Optional[_Mapping[int, bool]] = ...) -> None: ...
