from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StiffTemplateTableBase(_message.Message):
    __slots__ = ("id", "des", "behit_type", "hor_impact_force", "ver_impact_force", "stiffing_time", "stiff_hang_time", "stiff_end_time", "minimum_hor_speed", "skill_flow_offset", "skill_flow_radius")
    ID_FIELD_NUMBER: _ClassVar[int]
    DES_FIELD_NUMBER: _ClassVar[int]
    BEHIT_TYPE_FIELD_NUMBER: _ClassVar[int]
    HOR_IMPACT_FORCE_FIELD_NUMBER: _ClassVar[int]
    VER_IMPACT_FORCE_FIELD_NUMBER: _ClassVar[int]
    STIFFING_TIME_FIELD_NUMBER: _ClassVar[int]
    STIFF_HANG_TIME_FIELD_NUMBER: _ClassVar[int]
    STIFF_END_TIME_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_HOR_SPEED_FIELD_NUMBER: _ClassVar[int]
    SKILL_FLOW_OFFSET_FIELD_NUMBER: _ClassVar[int]
    SKILL_FLOW_RADIUS_FIELD_NUMBER: _ClassVar[int]
    id: int
    des: str
    behit_type: int
    hor_impact_force: float
    ver_impact_force: float
    stiffing_time: float
    stiff_hang_time: float
    stiff_end_time: float
    minimum_hor_speed: float
    skill_flow_offset: float
    skill_flow_radius: float
    def __init__(self, id: _Optional[int] = ..., des: _Optional[str] = ..., behit_type: _Optional[int] = ..., hor_impact_force: _Optional[float] = ..., ver_impact_force: _Optional[float] = ..., stiffing_time: _Optional[float] = ..., stiff_hang_time: _Optional[float] = ..., stiff_end_time: _Optional[float] = ..., minimum_hor_speed: _Optional[float] = ..., skill_flow_offset: _Optional[float] = ..., skill_flow_radius: _Optional[float] = ...) -> None: ...

class StiffTemplateTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: StiffTemplateTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[StiffTemplateTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, StiffTemplateTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, StiffTemplateTableBase]] = ...) -> None: ...
