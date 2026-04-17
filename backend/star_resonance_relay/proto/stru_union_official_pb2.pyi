from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UnionOfficial(_message.Message):
    __slots__ = ("official_id", "power", "name")
    class PowerEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bool
        def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
    OFFICIAL_ID_FIELD_NUMBER: _ClassVar[int]
    POWER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    official_id: int
    power: _containers.ScalarMap[int, bool]
    name: str
    def __init__(self, official_id: _Optional[int] = ..., power: _Optional[_Mapping[int, bool]] = ..., name: _Optional[str] = ...) -> None: ...
