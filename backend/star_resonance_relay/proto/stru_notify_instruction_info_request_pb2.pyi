from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyInstructionInfoRequest(_message.Message):
    __slots__ = ("type", "title", "msg", "url", "data", "logout_time", "rule_name", "trace_id", "modal", "logout_type")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    LOGOUT_TIME_FIELD_NUMBER: _ClassVar[int]
    RULE_NAME_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    MODAL_FIELD_NUMBER: _ClassVar[int]
    LOGOUT_TYPE_FIELD_NUMBER: _ClassVar[int]
    type: int
    title: str
    msg: str
    url: str
    data: str
    logout_time: int
    rule_name: str
    trace_id: str
    modal: int
    logout_type: int
    def __init__(self, type: _Optional[int] = ..., title: _Optional[str] = ..., msg: _Optional[str] = ..., url: _Optional[str] = ..., data: _Optional[str] = ..., logout_time: _Optional[int] = ..., rule_name: _Optional[str] = ..., trace_id: _Optional[str] = ..., modal: _Optional[int] = ..., logout_type: _Optional[int] = ...) -> None: ...
