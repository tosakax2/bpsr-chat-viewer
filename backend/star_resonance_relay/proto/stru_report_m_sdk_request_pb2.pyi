from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ReportMSdkRequest(_message.Message):
    __slots__ = ("open_id", "rule_name", "trace_id", "exec_time")
    OPEN_ID_FIELD_NUMBER: _ClassVar[int]
    RULE_NAME_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    EXEC_TIME_FIELD_NUMBER: _ClassVar[int]
    open_id: str
    rule_name: str
    trace_id: str
    exec_time: int
    def __init__(self, open_id: _Optional[str] = ..., rule_name: _Optional[str] = ..., trace_id: _Optional[str] = ..., exec_time: _Optional[int] = ...) -> None: ...
