import stru_action_group_info_pb2 as _stru_action_group_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SyncActionGroupInfo(_message.Message):
    __slots__ = ("action_group_info", "begin_time")
    ACTION_GROUP_INFO_FIELD_NUMBER: _ClassVar[int]
    BEGIN_TIME_FIELD_NUMBER: _ClassVar[int]
    action_group_info: _stru_action_group_info_pb2.ActionGroupInfo
    begin_time: int
    def __init__(self, action_group_info: _Optional[_Union[_stru_action_group_info_pb2.ActionGroupInfo, _Mapping]] = ..., begin_time: _Optional[int] = ...) -> None: ...
