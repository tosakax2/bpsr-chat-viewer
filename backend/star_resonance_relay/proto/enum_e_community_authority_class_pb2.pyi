from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ECommunityAuthorityClass(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CommunityAuthorityClassNone: _ClassVar[ECommunityAuthorityClass]
    CommunityAuthorityClassHome: _ClassVar[ECommunityAuthorityClass]
    CommunityAuthorityClassPlayer: _ClassVar[ECommunityAuthorityClass]
CommunityAuthorityClassNone: ECommunityAuthorityClass
CommunityAuthorityClassHome: ECommunityAuthorityClass
CommunityAuthorityClassPlayer: ECommunityAuthorityClass
