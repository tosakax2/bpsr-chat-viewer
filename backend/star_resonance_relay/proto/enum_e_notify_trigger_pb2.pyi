from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ENotifyTrigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ETypeInZone: _ClassVar[ENotifyTrigger]
    ETypeOutZone: _ClassVar[ENotifyTrigger]
    ETypeRange: _ClassVar[ENotifyTrigger]
ETypeInZone: ENotifyTrigger
ETypeOutZone: ENotifyTrigger
ETypeRange: ENotifyTrigger
