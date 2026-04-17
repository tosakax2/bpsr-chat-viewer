import enum_e_receive_reward_status_pb2 as _enum_e_receive_reward_status_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommonAwardInfo(_message.Message):
    __slots__ = ("id", "award_status")
    ID_FIELD_NUMBER: _ClassVar[int]
    AWARD_STATUS_FIELD_NUMBER: _ClassVar[int]
    id: int
    award_status: _enum_e_receive_reward_status_pb2.EReceiveRewardStatus
    def __init__(self, id: _Optional[int] = ..., award_status: _Optional[_Union[_enum_e_receive_reward_status_pb2.EReceiveRewardStatus, str]] = ...) -> None: ...
