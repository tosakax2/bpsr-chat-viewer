import stru_action_group_mount_info_pb2 as _stru_action_group_mount_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ActionGroupActionClip(_message.Message):
    __slots__ = ("begin_time", "end_time", "fade_time", "action_id", "action_begin_time", "action_end_time", "mount_info")
    BEGIN_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    FADE_TIME_FIELD_NUMBER: _ClassVar[int]
    ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_BEGIN_TIME_FIELD_NUMBER: _ClassVar[int]
    ACTION_END_TIME_FIELD_NUMBER: _ClassVar[int]
    MOUNT_INFO_FIELD_NUMBER: _ClassVar[int]
    begin_time: float
    end_time: float
    fade_time: float
    action_id: int
    action_begin_time: float
    action_end_time: float
    mount_info: _stru_action_group_mount_info_pb2.ActionGroupMountInfo
    def __init__(self, begin_time: _Optional[float] = ..., end_time: _Optional[float] = ..., fade_time: _Optional[float] = ..., action_id: _Optional[int] = ..., action_begin_time: _Optional[float] = ..., action_end_time: _Optional[float] = ..., mount_info: _Optional[_Union[_stru_action_group_mount_info_pb2.ActionGroupMountInfo, _Mapping]] = ...) -> None: ...
