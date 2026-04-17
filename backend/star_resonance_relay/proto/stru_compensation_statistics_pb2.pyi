import stru_compensation_season_statistics_pb2 as _stru_compensation_season_statistics_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CompensationStatistics(_message.Message):
    __slots__ = ("season_data", "last_season_id", "cur_point", "max_point", "last_week")
    class SeasonDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_compensation_season_statistics_pb2.CompensationSeasonStatistics
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_compensation_season_statistics_pb2.CompensationSeasonStatistics, _Mapping]] = ...) -> None: ...
    class LastWeekEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    SEASON_DATA_FIELD_NUMBER: _ClassVar[int]
    LAST_SEASON_ID_FIELD_NUMBER: _ClassVar[int]
    CUR_POINT_FIELD_NUMBER: _ClassVar[int]
    MAX_POINT_FIELD_NUMBER: _ClassVar[int]
    LAST_WEEK_FIELD_NUMBER: _ClassVar[int]
    season_data: _containers.MessageMap[int, _stru_compensation_season_statistics_pb2.CompensationSeasonStatistics]
    last_season_id: int
    cur_point: int
    max_point: int
    last_week: _containers.ScalarMap[int, int]
    def __init__(self, season_data: _Optional[_Mapping[int, _stru_compensation_season_statistics_pb2.CompensationSeasonStatistics]] = ..., last_season_id: _Optional[int] = ..., cur_point: _Optional[int] = ..., max_point: _Optional[int] = ..., last_week: _Optional[_Mapping[int, int]] = ...) -> None: ...
