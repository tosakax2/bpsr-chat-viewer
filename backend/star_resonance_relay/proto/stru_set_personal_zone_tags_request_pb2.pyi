from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SetPersonalZoneTagsRequest(_message.Message):
    __slots__ = ("online_periods", "tags")
    ONLINE_PERIODS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    online_periods: _containers.RepeatedScalarFieldContainer[int]
    tags: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, online_periods: _Optional[_Iterable[int]] = ..., tags: _Optional[_Iterable[int]] = ...) -> None: ...
