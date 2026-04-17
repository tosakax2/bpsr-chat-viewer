from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class CommunityWarehouseOpType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CommunityWarehouseOpTypeAdd: _ClassVar[CommunityWarehouseOpType]
    CommunityWarehouseOpTypeUpdate: _ClassVar[CommunityWarehouseOpType]
    CommunityWarehouseOpTypeDelete: _ClassVar[CommunityWarehouseOpType]
CommunityWarehouseOpTypeAdd: CommunityWarehouseOpType
CommunityWarehouseOpTypeUpdate: CommunityWarehouseOpType
CommunityWarehouseOpTypeDelete: CommunityWarehouseOpType
