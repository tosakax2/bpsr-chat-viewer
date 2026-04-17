from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ELevelEditorPosType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LevelEditorPosTypeBasic: _ClassVar[ELevelEditorPosType]
    LevelEditorPosTypePointId: _ClassVar[ELevelEditorPosType]
    LevelEditorPosTypeEntity: _ClassVar[ELevelEditorPosType]
    LevelEditorPosTypePos: _ClassVar[ELevelEditorPosType]
    LevelEditorPosTypePointGroup: _ClassVar[ELevelEditorPosType]
    LevelEditorPosTypePointGroupNonRepet: _ClassVar[ELevelEditorPosType]
LevelEditorPosTypeBasic: ELevelEditorPosType
LevelEditorPosTypePointId: ELevelEditorPosType
LevelEditorPosTypeEntity: ELevelEditorPosType
LevelEditorPosTypePos: ELevelEditorPosType
LevelEditorPosTypePointGroup: ELevelEditorPosType
LevelEditorPosTypePointGroupNonRepet: ELevelEditorPosType
