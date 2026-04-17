from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CancelEffectBuffRequest(_message.Message):
    __slots__ = ("union_id", "effect_buff_pos")
    UNION_ID_FIELD_NUMBER: _ClassVar[int]
    EFFECT_BUFF_POS_FIELD_NUMBER: _ClassVar[int]
    union_id: int
    effect_buff_pos: int
    def __init__(self, union_id: _Optional[int] = ..., effect_buff_pos: _Optional[int] = ...) -> None: ...
