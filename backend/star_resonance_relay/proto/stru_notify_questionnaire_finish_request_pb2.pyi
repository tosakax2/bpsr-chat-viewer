from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyQuestionnaireFinishRequest(_message.Message):
    __slots__ = ("questionnaire_id",)
    QUESTIONNAIRE_ID_FIELD_NUMBER: _ClassVar[int]
    questionnaire_id: int
    def __init__(self, questionnaire_id: _Optional[int] = ...) -> None: ...
