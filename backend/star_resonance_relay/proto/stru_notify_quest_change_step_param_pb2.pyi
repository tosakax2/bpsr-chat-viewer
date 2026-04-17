from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyQuestChangeStepParam(_message.Message):
    __slots__ = ("quest_id", "last_step", "last_step_status", "curr_setp", "last_quest_status")
    QUEST_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_STEP_FIELD_NUMBER: _ClassVar[int]
    LAST_STEP_STATUS_FIELD_NUMBER: _ClassVar[int]
    CURR_SETP_FIELD_NUMBER: _ClassVar[int]
    LAST_QUEST_STATUS_FIELD_NUMBER: _ClassVar[int]
    quest_id: int
    last_step: int
    last_step_status: int
    curr_setp: int
    last_quest_status: int
    def __init__(self, quest_id: _Optional[int] = ..., last_step: _Optional[int] = ..., last_step_status: _Optional[int] = ..., curr_setp: _Optional[int] = ..., last_quest_status: _Optional[int] = ...) -> None: ...
