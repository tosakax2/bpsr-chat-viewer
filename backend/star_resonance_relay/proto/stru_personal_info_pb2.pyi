from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PersonalInfo(_message.Message):
    __slots__ = ("showing_picture", "signature", "hobby_mark", "time_mark")
    SHOWING_PICTURE_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    HOBBY_MARK_FIELD_NUMBER: _ClassVar[int]
    TIME_MARK_FIELD_NUMBER: _ClassVar[int]
    showing_picture: str
    signature: str
    hobby_mark: _containers.RepeatedScalarFieldContainer[int]
    time_mark: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, showing_picture: _Optional[str] = ..., signature: _Optional[str] = ..., hobby_mark: _Optional[_Iterable[int]] = ..., time_mark: _Optional[_Iterable[int]] = ...) -> None: ...
