import stru_friendliness_exp_level_pb2 as _stru_friendliness_exp_level_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyFriendlinessExpLvRequest(_message.Message):
    __slots__ = ("change_list", "total_level", "total_exp", "today_total_add_exps", "update_time_stamp")
    CHANGE_LIST_FIELD_NUMBER: _ClassVar[int]
    TOTAL_LEVEL_FIELD_NUMBER: _ClassVar[int]
    TOTAL_EXP_FIELD_NUMBER: _ClassVar[int]
    TODAY_TOTAL_ADD_EXPS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_STAMP_FIELD_NUMBER: _ClassVar[int]
    change_list: _containers.RepeatedCompositeFieldContainer[_stru_friendliness_exp_level_pb2.FriendlinessExpLevel]
    total_level: int
    total_exp: int
    today_total_add_exps: int
    update_time_stamp: int
    def __init__(self, change_list: _Optional[_Iterable[_Union[_stru_friendliness_exp_level_pb2.FriendlinessExpLevel, _Mapping]]] = ..., total_level: _Optional[int] = ..., total_exp: _Optional[int] = ..., today_total_add_exps: _Optional[int] = ..., update_time_stamp: _Optional[int] = ...) -> None: ...
