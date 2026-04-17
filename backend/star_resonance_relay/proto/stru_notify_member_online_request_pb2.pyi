from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyMemberOnlineRequest(_message.Message):
    __slots__ = ("member_id_list", "offline_timer")
    MEMBER_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    OFFLINE_TIMER_FIELD_NUMBER: _ClassVar[int]
    member_id_list: _containers.RepeatedScalarFieldContainer[int]
    offline_timer: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, member_id_list: _Optional[_Iterable[int]] = ..., offline_timer: _Optional[_Iterable[int]] = ...) -> None: ...
