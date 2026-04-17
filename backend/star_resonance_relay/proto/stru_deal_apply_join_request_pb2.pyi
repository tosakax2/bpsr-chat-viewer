from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DealApplyJoinRequest(_message.Message):
    __slots__ = ("applicant_id", "agree")
    APPLICANT_ID_FIELD_NUMBER: _ClassVar[int]
    AGREE_FIELD_NUMBER: _ClassVar[int]
    applicant_id: int
    agree: bool
    def __init__(self, applicant_id: _Optional[int] = ..., agree: bool = ...) -> None: ...
