from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ECommunityFurnitureLimitType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CommunityFurnitureLimitTypeUnlimited: _ClassVar[ECommunityFurnitureLimitType]
    CommunityFurnitureLimitTypeIndoorOnly: _ClassVar[ECommunityFurnitureLimitType]
    CommunityFurnitureLimitTypeOutdoorOnly: _ClassVar[ECommunityFurnitureLimitType]
CommunityFurnitureLimitTypeUnlimited: ECommunityFurnitureLimitType
CommunityFurnitureLimitTypeIndoorOnly: ECommunityFurnitureLimitType
CommunityFurnitureLimitTypeOutdoorOnly: ECommunityFurnitureLimitType
