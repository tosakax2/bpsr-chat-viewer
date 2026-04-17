import stru_stat_record_pb2 as _stru_stat_record_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StatisticsData(_message.Message):
    __slots__ = ("stat_record_map", "season_stat_record_map")
    class StatRecordMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_stat_record_pb2.StatRecord
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_stat_record_pb2.StatRecord, _Mapping]] = ...) -> None: ...
    class SeasonStatRecordMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_stat_record_pb2.StatRecord
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_stat_record_pb2.StatRecord, _Mapping]] = ...) -> None: ...
    STAT_RECORD_MAP_FIELD_NUMBER: _ClassVar[int]
    SEASON_STAT_RECORD_MAP_FIELD_NUMBER: _ClassVar[int]
    stat_record_map: _containers.MessageMap[int, _stru_stat_record_pb2.StatRecord]
    season_stat_record_map: _containers.MessageMap[int, _stru_stat_record_pb2.StatRecord]
    def __init__(self, stat_record_map: _Optional[_Mapping[int, _stru_stat_record_pb2.StatRecord]] = ..., season_stat_record_map: _Optional[_Mapping[int, _stru_stat_record_pb2.StatRecord]] = ...) -> None: ...
