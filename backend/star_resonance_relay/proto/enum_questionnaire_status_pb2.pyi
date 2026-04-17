from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class QuestionnaireStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    QuestionnaireNotAnswered: _ClassVar[QuestionnaireStatus]
    QuestionnaireAnswered: _ClassVar[QuestionnaireStatus]
    QuestionnaireEmailed: _ClassVar[QuestionnaireStatus]
QuestionnaireNotAnswered: QuestionnaireStatus
QuestionnaireAnswered: QuestionnaireStatus
QuestionnaireEmailed: QuestionnaireStatus
