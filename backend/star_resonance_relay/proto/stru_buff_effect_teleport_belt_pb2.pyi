from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BuffEffectTeleportBelt(_message.Message):
    __slots__ = ("dir", "strength", "is_impact_hover", "is_use_weight_factor")
    DIR_FIELD_NUMBER: _ClassVar[int]
    STRENGTH_FIELD_NUMBER: _ClassVar[int]
    IS_IMPACT_HOVER_FIELD_NUMBER: _ClassVar[int]
    IS_USE_WEIGHT_FACTOR_FIELD_NUMBER: _ClassVar[int]
    dir: float
    strength: float
    is_impact_hover: bool
    is_use_weight_factor: bool
    def __init__(self, dir: _Optional[float] = ..., strength: _Optional[float] = ..., is_impact_hover: bool = ..., is_use_weight_factor: bool = ...) -> None: ...
