import enum_e_buff_effect_logic_pb_type_pb2 as _enum_e_buff_effect_logic_pb_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BuffEffectLogicInfo(_message.Message):
    __slots__ = ("EffectType", "RawData", "IsLoop")
    EFFECTTYPE_FIELD_NUMBER: _ClassVar[int]
    RAWDATA_FIELD_NUMBER: _ClassVar[int]
    ISLOOP_FIELD_NUMBER: _ClassVar[int]
    EffectType: _enum_e_buff_effect_logic_pb_type_pb2.EBuffEffectLogicPbType
    RawData: bytes
    IsLoop: bool
    def __init__(self, EffectType: _Optional[_Union[_enum_e_buff_effect_logic_pb_type_pb2.EBuffEffectLogicPbType, str]] = ..., RawData: _Optional[bytes] = ..., IsLoop: bool = ...) -> None: ...
