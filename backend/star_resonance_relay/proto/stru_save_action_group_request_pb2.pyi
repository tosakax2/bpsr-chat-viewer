import stru_action_group_save_info_pb2 as _stru_action_group_save_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SaveActionGroupRequest(_message.Message):
    __slots__ = ("action_group_id", "action_group_save_info")
    ACTION_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_GROUP_SAVE_INFO_FIELD_NUMBER: _ClassVar[int]
    action_group_id: int
    action_group_save_info: _stru_action_group_save_info_pb2.ActionGroupSaveInfo
    def __init__(self, action_group_id: _Optional[int] = ..., action_group_save_info: _Optional[_Union[_stru_action_group_save_info_pb2.ActionGroupSaveInfo, _Mapping]] = ...) -> None: ...
