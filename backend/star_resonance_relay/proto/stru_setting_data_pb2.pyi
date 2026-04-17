from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SettingData(_message.Message):
    __slots__ = ("setting_map",)
    class SettingMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    SETTING_MAP_FIELD_NUMBER: _ClassVar[int]
    setting_map: _containers.ScalarMap[int, str]
    def __init__(self, setting_map: _Optional[_Mapping[int, str]] = ...) -> None: ...
