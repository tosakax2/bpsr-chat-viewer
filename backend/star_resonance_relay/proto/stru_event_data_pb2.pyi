from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class EventData(_message.Message):
    __slots__ = ("event_type", "int_params", "long_params", "float_params", "str_params")
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    INT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    LONG_PARAMS_FIELD_NUMBER: _ClassVar[int]
    FLOAT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    STR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    event_type: int
    int_params: _containers.RepeatedScalarFieldContainer[int]
    long_params: _containers.RepeatedScalarFieldContainer[int]
    float_params: _containers.RepeatedScalarFieldContainer[float]
    str_params: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, event_type: _Optional[int] = ..., int_params: _Optional[_Iterable[int]] = ..., long_params: _Optional[_Iterable[int]] = ..., float_params: _Optional[_Iterable[float]] = ..., str_params: _Optional[_Iterable[str]] = ...) -> None: ...
