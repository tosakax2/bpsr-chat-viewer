from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EQuestStatusType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    QuestDefault: _ClassVar[EQuestStatusType]
    QuestCanAccept: _ClassVar[EQuestStatusType]
    QuestAccept: _ClassVar[EQuestStatusType]
    QuestFinish: _ClassVar[EQuestStatusType]
    QuestEnd: _ClassVar[EQuestStatusType]
    QuestNotEnough: _ClassVar[EQuestStatusType]
QuestDefault: EQuestStatusType
QuestCanAccept: EQuestStatusType
QuestAccept: EQuestStatusType
QuestFinish: EQuestStatusType
QuestEnd: EQuestStatusType
QuestNotEnough: EQuestStatusType
