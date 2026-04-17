from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ApprovalRequestRequest(_message.Message):
    __slots__ = ("union_id", "v_approval_list")
    class VApprovalListEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bool
        def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
    UNION_ID_FIELD_NUMBER: _ClassVar[int]
    V_APPROVAL_LIST_FIELD_NUMBER: _ClassVar[int]
    union_id: int
    v_approval_list: _containers.ScalarMap[int, bool]
    def __init__(self, union_id: _Optional[int] = ..., v_approval_list: _Optional[_Mapping[int, bool]] = ...) -> None: ...
