from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetMailAppendixRequest(_message.Message):
    __slots__ = ("mail_ids", "only_get")
    MAIL_IDS_FIELD_NUMBER: _ClassVar[int]
    ONLY_GET_FIELD_NUMBER: _ClassVar[int]
    mail_ids: _containers.RepeatedScalarFieldContainer[int]
    only_get: bool
    def __init__(self, mail_ids: _Optional[_Iterable[int]] = ..., only_get: bool = ...) -> None: ...
