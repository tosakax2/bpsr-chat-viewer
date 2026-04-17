from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EQuestAcceptType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    QuestAcceptTypeNone: _ClassVar[EQuestAcceptType]
    QuestAcceptTypeFlow: _ClassVar[EQuestAcceptType]
    QuestAcceptTypeItem: _ClassVar[EQuestAcceptType]
QuestAcceptTypeNone: EQuestAcceptType
QuestAcceptTypeFlow: EQuestAcceptType
QuestAcceptTypeItem: EQuestAcceptType
