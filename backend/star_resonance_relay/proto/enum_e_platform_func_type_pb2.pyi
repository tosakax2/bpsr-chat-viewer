from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EPlatformFuncType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EFuncTypeDefault: _ClassVar[EPlatformFuncType]
    EHeadProfile: _ClassVar[EPlatformFuncType]
    EPhotograph: _ClassVar[EPlatformFuncType]
    EUnionPhoto: _ClassVar[EPlatformFuncType]
    EIdIpUnionFormalPhoto: _ClassVar[EPlatformFuncType]
EFuncTypeDefault: EPlatformFuncType
EHeadProfile: EPlatformFuncType
EPhotograph: EPlatformFuncType
EUnionPhoto: EPlatformFuncType
EIdIpUnionFormalPhoto: EPlatformFuncType
