from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EPetFollowType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENormalFollow: _ClassVar[EPetFollowType]
    EForceFollow: _ClassVar[EPetFollowType]
ENormalFollow: EPetFollowType
EForceFollow: EPetFollowType
