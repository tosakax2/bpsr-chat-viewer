import enum_e_buff_event_type_pb2 as _enum_e_buff_event_type_pb2
import stru_buff_effect_logic_info_pb2 as _stru_buff_effect_logic_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BuffEffect(_message.Message):
    __slots__ = ("Type", "BuffUuid", "HostUuid", "TriggerTime", "LogicEffect")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    BUFFUUID_FIELD_NUMBER: _ClassVar[int]
    HOSTUUID_FIELD_NUMBER: _ClassVar[int]
    TRIGGERTIME_FIELD_NUMBER: _ClassVar[int]
    LOGICEFFECT_FIELD_NUMBER: _ClassVar[int]
    Type: _enum_e_buff_event_type_pb2.EBuffEventType
    BuffUuid: int
    HostUuid: int
    TriggerTime: int
    LogicEffect: _containers.RepeatedCompositeFieldContainer[_stru_buff_effect_logic_info_pb2.BuffEffectLogicInfo]
    def __init__(self, Type: _Optional[_Union[_enum_e_buff_event_type_pb2.EBuffEventType, str]] = ..., BuffUuid: _Optional[int] = ..., HostUuid: _Optional[int] = ..., TriggerTime: _Optional[int] = ..., LogicEffect: _Optional[_Iterable[_Union[_stru_buff_effect_logic_info_pb2.BuffEffectLogicInfo, _Mapping]]] = ...) -> None: ...
