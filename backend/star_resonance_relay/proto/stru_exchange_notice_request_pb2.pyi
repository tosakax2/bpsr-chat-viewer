from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ExchangeNoticeRequest(_message.Message):
    __slots__ = ("type", "sub_type")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SUB_TYPE_FIELD_NUMBER: _ClassVar[int]
    type: int
    sub_type: int
    def __init__(self, type: _Optional[int] = ..., sub_type: _Optional[int] = ...) -> None: ...
