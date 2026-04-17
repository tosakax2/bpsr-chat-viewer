from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ModAttrInfo(_message.Message):
    __slots__ = ("type", "id", "value", "effect_parameter")
    class EffectParameterEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    EFFECT_PARAMETER_FIELD_NUMBER: _ClassVar[int]
    type: int
    id: int
    value: int
    effect_parameter: _containers.ScalarMap[int, str]
    def __init__(self, type: _Optional[int] = ..., id: _Optional[int] = ..., value: _Optional[int] = ..., effect_parameter: _Optional[_Mapping[int, str]] = ...) -> None: ...
