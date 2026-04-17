from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ESwimStage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EIdle: _ClassVar[ESwimStage]
    EDive: _ClassVar[ESwimStage]
    EFallInto: _ClassVar[ESwimStage]
    ESwimming: _ClassVar[ESwimStage]
    ESprint: _ClassVar[ESwimStage]
    EAshore: _ClassVar[ESwimStage]
    EDrowning: _ClassVar[ESwimStage]
EIdle: ESwimStage
EDive: ESwimStage
EFallInto: ESwimStage
ESwimming: ESwimStage
ESprint: ESwimStage
EAshore: ESwimStage
EDrowning: ESwimStage
