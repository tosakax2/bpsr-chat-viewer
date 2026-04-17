from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DecomposeModRequest(_message.Message):
    __slots__ = ("mod_uuids",)
    MOD_UUIDS_FIELD_NUMBER: _ClassVar[int]
    mod_uuids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, mod_uuids: _Optional[_Iterable[int]] = ...) -> None: ...
