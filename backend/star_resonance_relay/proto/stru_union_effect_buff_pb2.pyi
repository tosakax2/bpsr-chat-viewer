from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UnionEffectBuff(_message.Message):
    __slots__ = ("buff_pos", "effect_buff_id", "end_time")
    BUFF_POS_FIELD_NUMBER: _ClassVar[int]
    EFFECT_BUFF_ID_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    buff_pos: int
    effect_buff_id: int
    end_time: int
    def __init__(self, buff_pos: _Optional[int] = ..., effect_buff_id: _Optional[int] = ..., end_time: _Optional[int] = ...) -> None: ...
