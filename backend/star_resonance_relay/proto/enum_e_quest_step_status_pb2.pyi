from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EQuestStepStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    QuestStepGoing: _ClassVar[EQuestStepStatus]
    QuestStepFinish: _ClassVar[EQuestStepStatus]
    QuestStepFail: _ClassVar[EQuestStepStatus]
QuestStepGoing: EQuestStepStatus
QuestStepFinish: EQuestStepStatus
QuestStepFail: EQuestStepStatus
