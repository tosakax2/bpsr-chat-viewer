import stru_home_land_player_task_info_pb2 as _stru_home_land_player_task_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyHomeLandPlayerTaskInfoUpdateRequest(_message.Message):
    __slots__ = ("new_info",)
    NEW_INFO_FIELD_NUMBER: _ClassVar[int]
    new_info: _stru_home_land_player_task_info_pb2.HomeLandPlayerTaskInfo
    def __init__(self, new_info: _Optional[_Union[_stru_home_land_player_task_info_pb2.HomeLandPlayerTaskInfo, _Mapping]] = ...) -> None: ...
