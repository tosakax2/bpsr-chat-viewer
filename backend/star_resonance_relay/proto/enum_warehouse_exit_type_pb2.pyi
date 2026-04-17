from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class WarehouseExitType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WarehouseExitTypeSelf: _ClassVar[WarehouseExitType]
    WarehouseExitTypeBeKickOut: _ClassVar[WarehouseExitType]
    WarehouseExitTypeDisband: _ClassVar[WarehouseExitType]
WarehouseExitTypeSelf: WarehouseExitType
WarehouseExitTypeBeKickOut: WarehouseExitType
WarehouseExitTypeDisband: WarehouseExitType
