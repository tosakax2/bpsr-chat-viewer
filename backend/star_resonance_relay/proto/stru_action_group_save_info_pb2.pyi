import stru_action_group_info_pb2 as _stru_action_group_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ActionGroupSaveInfo(_message.Message):
    __slots__ = ("action_group_info", "icon_id", "name", "save_time")
    ACTION_GROUP_INFO_FIELD_NUMBER: _ClassVar[int]
    ICON_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SAVE_TIME_FIELD_NUMBER: _ClassVar[int]
    action_group_info: _stru_action_group_info_pb2.ActionGroupInfo
    icon_id: int
    name: str
    save_time: int
    def __init__(self, action_group_info: _Optional[_Union[_stru_action_group_info_pb2.ActionGroupInfo, _Mapping]] = ..., icon_id: _Optional[int] = ..., name: _Optional[str] = ..., save_time: _Optional[int] = ...) -> None: ...
