import stru_timer_refresh_list_pb2 as _stru_timer_refresh_list_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TimerRefreshDataList(_message.Message):
    __slots__ = ("refresh_data_list",)
    class RefreshDataListEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_timer_refresh_list_pb2.TimerRefreshList
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_timer_refresh_list_pb2.TimerRefreshList, _Mapping]] = ...) -> None: ...
    REFRESH_DATA_LIST_FIELD_NUMBER: _ClassVar[int]
    refresh_data_list: _containers.MessageMap[int, _stru_timer_refresh_list_pb2.TimerRefreshList]
    def __init__(self, refresh_data_list: _Optional[_Mapping[int, _stru_timer_refresh_list_pb2.TimerRefreshList]] = ...) -> None: ...
