import stru_newbie_backflow_elective_pb2 as _stru_newbie_backflow_elective_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BackflowActData(_message.Message):
    __slots__ = ("login_days", "refresh_time_stamp", "refresh_season_id", "sign_state", "award_received", "elective_data")
    class ElectiveDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_newbie_backflow_elective_pb2.NewbieBackflowElective
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_newbie_backflow_elective_pb2.NewbieBackflowElective, _Mapping]] = ...) -> None: ...
    LOGIN_DAYS_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TIME_STAMP_FIELD_NUMBER: _ClassVar[int]
    REFRESH_SEASON_ID_FIELD_NUMBER: _ClassVar[int]
    SIGN_STATE_FIELD_NUMBER: _ClassVar[int]
    AWARD_RECEIVED_FIELD_NUMBER: _ClassVar[int]
    ELECTIVE_DATA_FIELD_NUMBER: _ClassVar[int]
    login_days: int
    refresh_time_stamp: int
    refresh_season_id: int
    sign_state: _containers.RepeatedScalarFieldContainer[int]
    award_received: bool
    elective_data: _containers.MessageMap[int, _stru_newbie_backflow_elective_pb2.NewbieBackflowElective]
    def __init__(self, login_days: _Optional[int] = ..., refresh_time_stamp: _Optional[int] = ..., refresh_season_id: _Optional[int] = ..., sign_state: _Optional[_Iterable[int]] = ..., award_received: bool = ..., elective_data: _Optional[_Mapping[int, _stru_newbie_backflow_elective_pb2.NewbieBackflowElective]] = ...) -> None: ...
