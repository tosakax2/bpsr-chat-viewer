import stru_backflow_act_data_pb2 as _stru_backflow_act_data_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BackflowData(_message.Message):
    __slots__ = ("begin_time", "is_backflow", "season_id", "activate_times", "is_not_show_tag", "act_data")
    BEGIN_TIME_FIELD_NUMBER: _ClassVar[int]
    IS_BACKFLOW_FIELD_NUMBER: _ClassVar[int]
    SEASON_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVATE_TIMES_FIELD_NUMBER: _ClassVar[int]
    IS_NOT_SHOW_TAG_FIELD_NUMBER: _ClassVar[int]
    ACT_DATA_FIELD_NUMBER: _ClassVar[int]
    begin_time: int
    is_backflow: bool
    season_id: int
    activate_times: int
    is_not_show_tag: bool
    act_data: _stru_backflow_act_data_pb2.BackflowActData
    def __init__(self, begin_time: _Optional[int] = ..., is_backflow: bool = ..., season_id: _Optional[int] = ..., activate_times: _Optional[int] = ..., is_not_show_tag: bool = ..., act_data: _Optional[_Union[_stru_backflow_act_data_pb2.BackflowActData, _Mapping]] = ...) -> None: ...
