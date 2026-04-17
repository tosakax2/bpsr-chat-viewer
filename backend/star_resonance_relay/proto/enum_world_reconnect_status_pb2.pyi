from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class WorldReconnectStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FastReconnect: _ClassVar[WorldReconnectStatus]
    NewSession: _ClassVar[WorldReconnectStatus]
FastReconnect: WorldReconnectStatus
NewSession: WorldReconnectStatus
