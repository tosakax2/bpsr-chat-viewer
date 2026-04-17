from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ESceneVariableType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ESceneVariableTypeNone: _ClassVar[ESceneVariableType]
    ESceneVariableTypeGroup: _ClassVar[ESceneVariableType]
    ESceneVariableTypePlayer: _ClassVar[ESceneVariableType]
ESceneVariableTypeNone: ESceneVariableType
ESceneVariableTypeGroup: ESceneVariableType
ESceneVariableTypePlayer: ESceneVariableType
