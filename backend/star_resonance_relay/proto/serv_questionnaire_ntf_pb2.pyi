import stru_notify_questionnaire_finish_request_pb2 as _stru_notify_questionnaire_finish_request_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QuestionnaireNtf(_message.Message):
    __slots__ = ()
    class NotifyQuestionnaireFinish(_message.Message):
        __slots__ = ("request",)
        REQUEST_FIELD_NUMBER: _ClassVar[int]
        request: _stru_notify_questionnaire_finish_request_pb2.NotifyQuestionnaireFinishRequest
        def __init__(self, request: _Optional[_Union[_stru_notify_questionnaire_finish_request_pb2.NotifyQuestionnaireFinishRequest, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...
