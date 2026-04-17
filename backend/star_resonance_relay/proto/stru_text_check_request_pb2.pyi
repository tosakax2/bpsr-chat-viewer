import stru_session_info_pb2 as _stru_session_info_pb2
import enum_text_check_scene_type_pb2 as _enum_text_check_scene_type_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TextCheckRequest(_message.Message):
    __slots__ = ("session", "scene_type", "str", "parame")
    class ParameEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SESSION_FIELD_NUMBER: _ClassVar[int]
    SCENE_TYPE_FIELD_NUMBER: _ClassVar[int]
    STR_FIELD_NUMBER: _ClassVar[int]
    PARAME_FIELD_NUMBER: _ClassVar[int]
    session: _stru_session_info_pb2.SessionInfo
    scene_type: _enum_text_check_scene_type_pb2.TextCheckSceneType
    str: _containers.RepeatedScalarFieldContainer[str]
    parame: _containers.ScalarMap[str, str]
    def __init__(self, session: _Optional[_Union[_stru_session_info_pb2.SessionInfo, _Mapping]] = ..., scene_type: _Optional[_Union[_enum_text_check_scene_type_pb2.TextCheckSceneType, str]] = ..., str: _Optional[_Iterable[str]] = ..., parame: _Optional[_Mapping[str, str]] = ...) -> None: ...
