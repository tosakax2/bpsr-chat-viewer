from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BuffProfessionEffectData(_message.Message):
    __slots__ = ("profession_type", "profession_point", "profession_switch")
    PROFESSION_TYPE_FIELD_NUMBER: _ClassVar[int]
    PROFESSION_POINT_FIELD_NUMBER: _ClassVar[int]
    PROFESSION_SWITCH_FIELD_NUMBER: _ClassVar[int]
    profession_type: int
    profession_point: _containers.RepeatedScalarFieldContainer[int]
    profession_switch: _containers.RepeatedScalarFieldContainer[bool]
    def __init__(self, profession_type: _Optional[int] = ..., profession_point: _Optional[_Iterable[int]] = ..., profession_switch: _Optional[_Iterable[bool]] = ...) -> None: ...
