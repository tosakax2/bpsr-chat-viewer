from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EAlbumRight(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EveryOneAccess: _ClassVar[EAlbumRight]
    FriendAccess: _ClassVar[EAlbumRight]
    SelfAccess: _ClassVar[EAlbumRight]
    UnionAccess: _ClassVar[EAlbumRight]
EveryOneAccess: EAlbumRight
FriendAccess: EAlbumRight
SelfAccess: EAlbumRight
UnionAccess: EAlbumRight
