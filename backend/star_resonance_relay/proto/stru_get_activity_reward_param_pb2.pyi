from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetActivityRewardParam(_message.Message):
    __slots__ = ("activity_uuid", "reward_id")
    ACTIVITY_UUID_FIELD_NUMBER: _ClassVar[int]
    REWARD_ID_FIELD_NUMBER: _ClassVar[int]
    activity_uuid: int
    reward_id: int
    def __init__(self, activity_uuid: _Optional[int] = ..., reward_id: _Optional[int] = ...) -> None: ...
