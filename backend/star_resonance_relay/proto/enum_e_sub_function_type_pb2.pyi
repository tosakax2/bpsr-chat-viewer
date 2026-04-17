from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ESubFunctionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ESubFunctionTypeNone: _ClassVar[ESubFunctionType]
    ESubFunctionTypeWorldChat: _ClassVar[ESubFunctionType]
    ESubFunctionTypeSceneChat: _ClassVar[ESubFunctionType]
    ESubFunctionTypeTeamChat: _ClassVar[ESubFunctionType]
    ESubFunctionTypeUnionChat: _ClassVar[ESubFunctionType]
ESubFunctionTypeNone: ESubFunctionType
ESubFunctionTypeWorldChat: ESubFunctionType
ESubFunctionTypeSceneChat: ESubFunctionType
ESubFunctionTypeTeamChat: ESubFunctionType
ESubFunctionTypeUnionChat: ESubFunctionType
