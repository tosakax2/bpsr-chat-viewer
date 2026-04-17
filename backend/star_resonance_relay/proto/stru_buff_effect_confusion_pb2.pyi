import enum_e_buff_effect_confusion_type_pb2 as _enum_e_buff_effect_confusion_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BuffEffectConfusion(_message.Message):
    __slots__ = ("type", "rand_radius")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    RAND_RADIUS_FIELD_NUMBER: _ClassVar[int]
    type: _enum_e_buff_effect_confusion_type_pb2.EBuffEffectConfusionType
    rand_radius: float
    def __init__(self, type: _Optional[_Union[_enum_e_buff_effect_confusion_type_pb2.EBuffEffectConfusionType, str]] = ..., rand_radius: _Optional[float] = ...) -> None: ...
