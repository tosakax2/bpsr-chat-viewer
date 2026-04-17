import stru_union_effect_buff_pb2 as _stru_union_effect_buff_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyEffectBufChangeRequest(_message.Message):
    __slots__ = ("set_effect_buff", "cancel_effect_buff")
    SET_EFFECT_BUFF_FIELD_NUMBER: _ClassVar[int]
    CANCEL_EFFECT_BUFF_FIELD_NUMBER: _ClassVar[int]
    set_effect_buff: _stru_union_effect_buff_pb2.UnionEffectBuff
    cancel_effect_buff: _stru_union_effect_buff_pb2.UnionEffectBuff
    def __init__(self, set_effect_buff: _Optional[_Union[_stru_union_effect_buff_pb2.UnionEffectBuff, _Mapping]] = ..., cancel_effect_buff: _Optional[_Union[_stru_union_effect_buff_pb2.UnionEffectBuff, _Mapping]] = ...) -> None: ...
