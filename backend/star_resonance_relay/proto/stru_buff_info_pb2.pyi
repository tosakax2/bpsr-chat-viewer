import stru_fight_source_info_pb2 as _stru_fight_source_info_pb2
import stru_buff_effect_logic_info_pb2 as _stru_buff_effect_logic_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BuffInfo(_message.Message):
    __slots__ = ("BuffUuid", "BaseId", "Level", "HostUuid", "TableUuid", "CreateTime", "FireUuid", "Layer", "PartId", "Count", "Duration", "FightSourceInfo", "LogicEffect")
    BUFFUUID_FIELD_NUMBER: _ClassVar[int]
    BASEID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    HOSTUUID_FIELD_NUMBER: _ClassVar[int]
    TABLEUUID_FIELD_NUMBER: _ClassVar[int]
    CREATETIME_FIELD_NUMBER: _ClassVar[int]
    FIREUUID_FIELD_NUMBER: _ClassVar[int]
    LAYER_FIELD_NUMBER: _ClassVar[int]
    PARTID_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    FIGHTSOURCEINFO_FIELD_NUMBER: _ClassVar[int]
    LOGICEFFECT_FIELD_NUMBER: _ClassVar[int]
    BuffUuid: int
    BaseId: int
    Level: int
    HostUuid: int
    TableUuid: int
    CreateTime: int
    FireUuid: int
    Layer: int
    PartId: int
    Count: int
    Duration: int
    FightSourceInfo: _stru_fight_source_info_pb2.FightSourceInfo
    LogicEffect: _stru_buff_effect_logic_info_pb2.BuffEffectLogicInfo
    def __init__(self, BuffUuid: _Optional[int] = ..., BaseId: _Optional[int] = ..., Level: _Optional[int] = ..., HostUuid: _Optional[int] = ..., TableUuid: _Optional[int] = ..., CreateTime: _Optional[int] = ..., FireUuid: _Optional[int] = ..., Layer: _Optional[int] = ..., PartId: _Optional[int] = ..., Count: _Optional[int] = ..., Duration: _Optional[int] = ..., FightSourceInfo: _Optional[_Union[_stru_fight_source_info_pb2.FightSourceInfo, _Mapping]] = ..., LogicEffect: _Optional[_Union[_stru_buff_effect_logic_info_pb2.BuffEffectLogicInfo, _Mapping]] = ...) -> None: ...
