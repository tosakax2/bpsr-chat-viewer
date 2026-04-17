import stru_quest_data_pb2 as _stru_quest_data_pb2
import stru_quest_history_pb2 as _stru_quest_history_pb2
import stru_world_quest_info_pb2 as _stru_world_quest_info_pb2
import stru_world_quest_list_pb2 as _stru_world_quest_list_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QuestDataList(_message.Message):
    __slots__ = ("quest_map", "finish_quest", "tracking_id", "finish_reset_quest", "history_map", "world_quest_time_stamp", "world_quest_info", "all_world_quest_list", "blue_world_quest_map", "filter_event_id", "accept_quest_list", "follow_world_quest_list", "track_optional_quest", "finish_reset_quest_count", "accept_quest_map", "version")
    class QuestMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_quest_data_pb2.QuestData
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_quest_data_pb2.QuestData, _Mapping]] = ...) -> None: ...
    class FinishQuestEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bool
        def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
    class FinishResetQuestEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class HistoryMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_quest_history_pb2.QuestHistory
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_quest_history_pb2.QuestHistory, _Mapping]] = ...) -> None: ...
    class WorldQuestInfoEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_world_quest_info_pb2.WorldQuestInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_world_quest_info_pb2.WorldQuestInfo, _Mapping]] = ...) -> None: ...
    class AllWorldQuestListEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class BlueWorldQuestMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class FilterEventIdEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_world_quest_list_pb2.worldQuestList
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_world_quest_list_pb2.worldQuestList, _Mapping]] = ...) -> None: ...
    class TrackOptionalQuestEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class FinishResetQuestCountEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class AcceptQuestMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bool
        def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
    QUEST_MAP_FIELD_NUMBER: _ClassVar[int]
    FINISH_QUEST_FIELD_NUMBER: _ClassVar[int]
    TRACKING_ID_FIELD_NUMBER: _ClassVar[int]
    FINISH_RESET_QUEST_FIELD_NUMBER: _ClassVar[int]
    HISTORY_MAP_FIELD_NUMBER: _ClassVar[int]
    WORLD_QUEST_TIME_STAMP_FIELD_NUMBER: _ClassVar[int]
    WORLD_QUEST_INFO_FIELD_NUMBER: _ClassVar[int]
    ALL_WORLD_QUEST_LIST_FIELD_NUMBER: _ClassVar[int]
    BLUE_WORLD_QUEST_MAP_FIELD_NUMBER: _ClassVar[int]
    FILTER_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    ACCEPT_QUEST_LIST_FIELD_NUMBER: _ClassVar[int]
    FOLLOW_WORLD_QUEST_LIST_FIELD_NUMBER: _ClassVar[int]
    TRACK_OPTIONAL_QUEST_FIELD_NUMBER: _ClassVar[int]
    FINISH_RESET_QUEST_COUNT_FIELD_NUMBER: _ClassVar[int]
    ACCEPT_QUEST_MAP_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    quest_map: _containers.MessageMap[int, _stru_quest_data_pb2.QuestData]
    finish_quest: _containers.ScalarMap[int, bool]
    tracking_id: int
    finish_reset_quest: _containers.ScalarMap[int, int]
    history_map: _containers.MessageMap[int, _stru_quest_history_pb2.QuestHistory]
    world_quest_time_stamp: int
    world_quest_info: _containers.MessageMap[int, _stru_world_quest_info_pb2.WorldQuestInfo]
    all_world_quest_list: _containers.ScalarMap[int, int]
    blue_world_quest_map: _containers.ScalarMap[int, int]
    filter_event_id: _containers.MessageMap[int, _stru_world_quest_list_pb2.worldQuestList]
    accept_quest_list: _containers.RepeatedScalarFieldContainer[int]
    follow_world_quest_list: _containers.RepeatedScalarFieldContainer[int]
    track_optional_quest: _containers.ScalarMap[int, int]
    finish_reset_quest_count: _containers.ScalarMap[int, int]
    accept_quest_map: _containers.ScalarMap[int, bool]
    version: int
    def __init__(self, quest_map: _Optional[_Mapping[int, _stru_quest_data_pb2.QuestData]] = ..., finish_quest: _Optional[_Mapping[int, bool]] = ..., tracking_id: _Optional[int] = ..., finish_reset_quest: _Optional[_Mapping[int, int]] = ..., history_map: _Optional[_Mapping[int, _stru_quest_history_pb2.QuestHistory]] = ..., world_quest_time_stamp: _Optional[int] = ..., world_quest_info: _Optional[_Mapping[int, _stru_world_quest_info_pb2.WorldQuestInfo]] = ..., all_world_quest_list: _Optional[_Mapping[int, int]] = ..., blue_world_quest_map: _Optional[_Mapping[int, int]] = ..., filter_event_id: _Optional[_Mapping[int, _stru_world_quest_list_pb2.worldQuestList]] = ..., accept_quest_list: _Optional[_Iterable[int]] = ..., follow_world_quest_list: _Optional[_Iterable[int]] = ..., track_optional_quest: _Optional[_Mapping[int, int]] = ..., finish_reset_quest_count: _Optional[_Mapping[int, int]] = ..., accept_quest_map: _Optional[_Mapping[int, bool]] = ..., version: _Optional[int] = ...) -> None: ...
