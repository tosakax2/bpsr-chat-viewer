from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EChangeSceneType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ChangeSceneTypeNormal: _ClassVar[EChangeSceneType]
    ChangeSceneTransfer: _ClassVar[EChangeSceneType]
    ChangeSceneTypeLogin: _ClassVar[EChangeSceneType]
    ChangeSceneReconnect: _ClassVar[EChangeSceneType]
    ChangeSceneDisconnect: _ClassVar[EChangeSceneType]
    ReceiveLoadMapSuccess: _ClassVar[EChangeSceneType]
ChangeSceneTypeNormal: EChangeSceneType
ChangeSceneTransfer: EChangeSceneType
ChangeSceneTypeLogin: EChangeSceneType
ChangeSceneReconnect: EChangeSceneType
ChangeSceneDisconnect: EChangeSceneType
ReceiveLoadMapSuccess: EChangeSceneType
