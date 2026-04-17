from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ETargetShareType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NotShare: _ClassVar[ETargetShareType]
    TeamShare: _ClassVar[ETargetShareType]
    DungeonShare: _ClassVar[ETargetShareType]
NotShare: ETargetShareType
TeamShare: ETargetShareType
DungeonShare: ETargetShareType
