from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LinkingInfo(_message.Message):
    __slots__ = ("is_delete", "effectid", "buff_uuid", "target_uuids")
    IS_DELETE_FIELD_NUMBER: _ClassVar[int]
    EFFECTID_FIELD_NUMBER: _ClassVar[int]
    BUFF_UUID_FIELD_NUMBER: _ClassVar[int]
    TARGET_UUIDS_FIELD_NUMBER: _ClassVar[int]
    is_delete: bool
    effectid: int
    buff_uuid: int
    target_uuids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, is_delete: bool = ..., effectid: _Optional[int] = ..., buff_uuid: _Optional[int] = ..., target_uuids: _Optional[_Iterable[int]] = ...) -> None: ...
