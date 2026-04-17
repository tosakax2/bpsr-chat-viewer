from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EFarmlandState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EFarmlandStateEmpty: _ClassVar[EFarmlandState]
    EFarmlandStateGrow: _ClassVar[EFarmlandState]
    EFarmlandStatePollen: _ClassVar[EFarmlandState]
    EFarmlandStateHarvest: _ClassVar[EFarmlandState]
    EFarmlandStateOver: _ClassVar[EFarmlandState]
EFarmlandStateEmpty: EFarmlandState
EFarmlandStateGrow: EFarmlandState
EFarmlandStatePollen: EFarmlandState
EFarmlandStateHarvest: EFarmlandState
EFarmlandStateOver: EFarmlandState
