from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ExchangePutItemRequest(_message.Message):
    __slots__ = ("uuid", "num", "step", "is_public")
    UUID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    STEP_FIELD_NUMBER: _ClassVar[int]
    IS_PUBLIC_FIELD_NUMBER: _ClassVar[int]
    uuid: int
    num: int
    step: int
    is_public: bool
    def __init__(self, uuid: _Optional[int] = ..., num: _Optional[int] = ..., step: _Optional[int] = ..., is_public: bool = ...) -> None: ...
