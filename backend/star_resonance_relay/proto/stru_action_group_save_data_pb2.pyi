import stru_action_group_save_info_pb2 as _stru_action_group_save_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ActionGroupSaveData(_message.Message):
    __slots__ = ("action_group_save_infos", "is_init")
    class ActionGroupSaveInfosEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_action_group_save_info_pb2.ActionGroupSaveInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_action_group_save_info_pb2.ActionGroupSaveInfo, _Mapping]] = ...) -> None: ...
    ACTION_GROUP_SAVE_INFOS_FIELD_NUMBER: _ClassVar[int]
    IS_INIT_FIELD_NUMBER: _ClassVar[int]
    action_group_save_infos: _containers.MessageMap[int, _stru_action_group_save_info_pb2.ActionGroupSaveInfo]
    is_init: bool
    def __init__(self, action_group_save_infos: _Optional[_Mapping[int, _stru_action_group_save_info_pb2.ActionGroupSaveInfo]] = ..., is_init: bool = ...) -> None: ...
