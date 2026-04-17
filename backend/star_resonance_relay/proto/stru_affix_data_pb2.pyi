from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AffixData(_message.Message):
    __slots__ = ("affix_ids",)
    AFFIX_IDS_FIELD_NUMBER: _ClassVar[int]
    affix_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, affix_ids: _Optional[_Iterable[int]] = ...) -> None: ...
