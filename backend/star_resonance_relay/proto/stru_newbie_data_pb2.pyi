import stru_newbie_act_data_pb2 as _stru_newbie_act_data_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NewbieData(_message.Message):
    __slots__ = ("total_online_time", "is_newbie", "is_cancel_newbie", "season_id", "activate_times", "is_not_show_tag", "begin_time", "act_data")
    TOTAL_ONLINE_TIME_FIELD_NUMBER: _ClassVar[int]
    IS_NEWBIE_FIELD_NUMBER: _ClassVar[int]
    IS_CANCEL_NEWBIE_FIELD_NUMBER: _ClassVar[int]
    SEASON_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVATE_TIMES_FIELD_NUMBER: _ClassVar[int]
    IS_NOT_SHOW_TAG_FIELD_NUMBER: _ClassVar[int]
    BEGIN_TIME_FIELD_NUMBER: _ClassVar[int]
    ACT_DATA_FIELD_NUMBER: _ClassVar[int]
    total_online_time: int
    is_newbie: bool
    is_cancel_newbie: bool
    season_id: int
    activate_times: int
    is_not_show_tag: bool
    begin_time: int
    act_data: _stru_newbie_act_data_pb2.NewbieActData
    def __init__(self, total_online_time: _Optional[int] = ..., is_newbie: bool = ..., is_cancel_newbie: bool = ..., season_id: _Optional[int] = ..., activate_times: _Optional[int] = ..., is_not_show_tag: bool = ..., begin_time: _Optional[int] = ..., act_data: _Optional[_Union[_stru_newbie_act_data_pb2.NewbieActData, _Mapping]] = ...) -> None: ...
