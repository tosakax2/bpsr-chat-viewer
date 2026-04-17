import enum_e_gravitational_type_pb2 as _enum_e_gravitational_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BuffEffectLogicGravity(_message.Message):
    __slots__ = ("type", "strength", "strength_low", "internal_radius", "external_radius", "entity_type", "camp_target_type", "is_impact_hover", "is_use_weight_factor")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STRENGTH_FIELD_NUMBER: _ClassVar[int]
    STRENGTH_LOW_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_RADIUS_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_RADIUS_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    CAMP_TARGET_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_IMPACT_HOVER_FIELD_NUMBER: _ClassVar[int]
    IS_USE_WEIGHT_FACTOR_FIELD_NUMBER: _ClassVar[int]
    type: _enum_e_gravitational_type_pb2.EGravitationalType
    strength: float
    strength_low: float
    internal_radius: float
    external_radius: float
    entity_type: int
    camp_target_type: int
    is_impact_hover: bool
    is_use_weight_factor: bool
    def __init__(self, type: _Optional[_Union[_enum_e_gravitational_type_pb2.EGravitationalType, str]] = ..., strength: _Optional[float] = ..., strength_low: _Optional[float] = ..., internal_radius: _Optional[float] = ..., external_radius: _Optional[float] = ..., entity_type: _Optional[int] = ..., camp_target_type: _Optional[int] = ..., is_impact_hover: bool = ..., is_use_weight_factor: bool = ...) -> None: ...
