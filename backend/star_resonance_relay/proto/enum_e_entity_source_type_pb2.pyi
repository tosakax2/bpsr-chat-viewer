from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EEntitySourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EntitySourceServer: _ClassVar[EEntitySourceType]
    EntitySourceClient: _ClassVar[EEntitySourceType]
    EntitySourceUser: _ClassVar[EEntitySourceType]
    EntitySourceScene: _ClassVar[EEntitySourceType]
    EntitySourceCommunity: _ClassVar[EEntitySourceType]
EntitySourceServer: EEntitySourceType
EntitySourceClient: EEntitySourceType
EntitySourceUser: EEntitySourceType
EntitySourceScene: EEntitySourceType
EntitySourceCommunity: EEntitySourceType
