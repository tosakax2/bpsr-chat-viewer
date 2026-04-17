from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ERideType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RideTypeNormal: _ClassVar[ERideType]
    RideTypeRider: _ClassVar[ERideType]
    RideTypeVehicle: _ClassVar[ERideType]
    RideTypePlatform: _ClassVar[ERideType]
    RideTypePublicVehicle: _ClassVar[ERideType]
RideTypeNormal: ERideType
RideTypeRider: ERideType
RideTypeVehicle: ERideType
RideTypePlatform: ERideType
RideTypePublicVehicle: ERideType
