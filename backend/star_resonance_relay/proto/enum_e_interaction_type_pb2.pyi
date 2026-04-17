from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EInteractionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EInteractionTypeDefault: _ClassVar[EInteractionType]
    EInteractionTypePlayer: _ClassVar[EInteractionType]
    EInteractionTypeNotPlayer: _ClassVar[EInteractionType]
EInteractionTypeDefault: EInteractionType
EInteractionTypePlayer: EInteractionType
EInteractionTypeNotPlayer: EInteractionType
