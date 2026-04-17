import stru_buff_effect_pb2 as _stru_buff_effect_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BuffEffectSync(_message.Message):
    __slots__ = ("Uuid", "BuffEffects")
    UUID_FIELD_NUMBER: _ClassVar[int]
    BUFFEFFECTS_FIELD_NUMBER: _ClassVar[int]
    Uuid: int
    BuffEffects: _containers.RepeatedCompositeFieldContainer[_stru_buff_effect_pb2.BuffEffect]
    def __init__(self, Uuid: _Optional[int] = ..., BuffEffects: _Optional[_Iterable[_Union[_stru_buff_effect_pb2.BuffEffect, _Mapping]]] = ...) -> None: ...
