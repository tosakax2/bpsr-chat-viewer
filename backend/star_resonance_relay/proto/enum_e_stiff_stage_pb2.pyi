from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EStiffStage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Stiffing: _ClassVar[EStiffStage]
    StiffEnd: _ClassVar[EStiffStage]
    StiffStandup: _ClassVar[EStiffStage]
Stiffing: EStiffStage
StiffEnd: EStiffStage
StiffStandup: EStiffStage
