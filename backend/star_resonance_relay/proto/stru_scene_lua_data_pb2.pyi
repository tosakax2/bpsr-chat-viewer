from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SceneLuaData(_message.Message):
    __slots__ = ("scene_lua_info",)
    class SceneLuaInfoEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    SCENE_LUA_INFO_FIELD_NUMBER: _ClassVar[int]
    scene_lua_info: _containers.ScalarMap[int, str]
    def __init__(self, scene_lua_info: _Optional[_Mapping[int, str]] = ...) -> None: ...
