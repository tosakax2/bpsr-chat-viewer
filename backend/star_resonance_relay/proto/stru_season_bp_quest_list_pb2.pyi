import stru_season_bp_quest_data_pb2 as _stru_season_bp_quest_data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SeasonBpQuestList(_message.Message):
    __slots__ = ("season_map", "random_map", "refresh_time_stamp")
    class SeasonMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_season_bp_quest_data_pb2.SeasonBpQuestData
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_season_bp_quest_data_pb2.SeasonBpQuestData, _Mapping]] = ...) -> None: ...
    SEASON_MAP_FIELD_NUMBER: _ClassVar[int]
    RANDOM_MAP_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TIME_STAMP_FIELD_NUMBER: _ClassVar[int]
    season_map: _containers.MessageMap[int, _stru_season_bp_quest_data_pb2.SeasonBpQuestData]
    random_map: _containers.RepeatedScalarFieldContainer[int]
    refresh_time_stamp: int
    def __init__(self, season_map: _Optional[_Mapping[int, _stru_season_bp_quest_data_pb2.SeasonBpQuestData]] = ..., random_map: _Optional[_Iterable[int]] = ..., refresh_time_stamp: _Optional[int] = ...) -> None: ...
