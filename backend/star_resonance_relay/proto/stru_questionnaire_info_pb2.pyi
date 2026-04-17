import stru_questionnaire_award_item_pb2 as _stru_questionnaire_award_item_pb2
import enum_questionnaire_status_pb2 as _enum_questionnaire_status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QuestionnaireInfo(_message.Message):
    __slots__ = ("id", "status", "can_answer", "name", "link", "level_limit", "day_limit", "awards")
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CAN_ANSWER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LINK_FIELD_NUMBER: _ClassVar[int]
    LEVEL_LIMIT_FIELD_NUMBER: _ClassVar[int]
    DAY_LIMIT_FIELD_NUMBER: _ClassVar[int]
    AWARDS_FIELD_NUMBER: _ClassVar[int]
    id: int
    status: _enum_questionnaire_status_pb2.QuestionnaireStatus
    can_answer: bool
    name: str
    link: str
    level_limit: int
    day_limit: int
    awards: _containers.RepeatedCompositeFieldContainer[_stru_questionnaire_award_item_pb2.QuestionnaireAwardItem]
    def __init__(self, id: _Optional[int] = ..., status: _Optional[_Union[_enum_questionnaire_status_pb2.QuestionnaireStatus, str]] = ..., can_answer: bool = ..., name: _Optional[str] = ..., link: _Optional[str] = ..., level_limit: _Optional[int] = ..., day_limit: _Optional[int] = ..., awards: _Optional[_Iterable[_Union[_stru_questionnaire_award_item_pb2.QuestionnaireAwardItem, _Mapping]]] = ...) -> None: ...
