from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EQuestFailCheck(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EQuestFailNone: _ClassVar[EQuestFailCheck]
    EQuestFailScene: _ClassVar[EQuestFailCheck]
    EQuestFailVisuallayer: _ClassVar[EQuestFailCheck]
    EQuestFailDeath: _ClassVar[EQuestFailCheck]
    EQuestTime: _ClassVar[EQuestFailCheck]
EQuestFailNone: EQuestFailCheck
EQuestFailScene: EQuestFailCheck
EQuestFailVisuallayer: EQuestFailCheck
EQuestFailDeath: EQuestFailCheck
EQuestTime: EQuestFailCheck
