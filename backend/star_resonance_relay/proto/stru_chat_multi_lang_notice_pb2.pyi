from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ChatMultiLangNotice(_message.Message):
    __slots__ = ("config_id", "args")
    CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    config_id: int
    args: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, config_id: _Optional[int] = ..., args: _Optional[_Iterable[str]] = ...) -> None: ...
