from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ESceneLineStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SceneLineStatusNone: _ClassVar[ESceneLineStatus]
    SceneLineStatusLow: _ClassVar[ESceneLineStatus]
    SceneLineStatusMedium: _ClassVar[ESceneLineStatus]
    SceneLineStatusHigh: _ClassVar[ESceneLineStatus]
    SceneLineStatusFull: _ClassVar[ESceneLineStatus]
    SceneLineStatusRecycle: _ClassVar[ESceneLineStatus]
SceneLineStatusNone: ESceneLineStatus
SceneLineStatusLow: ESceneLineStatus
SceneLineStatusMedium: ESceneLineStatus
SceneLineStatusHigh: ESceneLineStatus
SceneLineStatusFull: ESceneLineStatus
SceneLineStatusRecycle: ESceneLineStatus
