from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AcceptQuestInfo(_message.Message):
    __slots__ = ("quest_id", "param_list")
    QUEST_ID_FIELD_NUMBER: _ClassVar[int]
    PARAM_LIST_FIELD_NUMBER: _ClassVar[int]
    quest_id: int
    param_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, quest_id: _Optional[int] = ..., param_list: _Optional[_Iterable[int]] = ...) -> None: ...
