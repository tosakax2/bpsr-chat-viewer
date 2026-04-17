import stru_battle_pass_pb2 as _stru_battle_pass_pb2
import stru_season_bp_quest_list_pb2 as _stru_season_bp_quest_list_pb2
import stru_season_center_history_pb2 as _stru_season_center_history_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SeasonCenter(_message.Message):
    __slots__ = ("season_id", "battle_pass", "bp_quest_list", "season_history")
    class SeasonHistoryEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_season_center_history_pb2.SeasonCenterHistory
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_season_center_history_pb2.SeasonCenterHistory, _Mapping]] = ...) -> None: ...
    SEASON_ID_FIELD_NUMBER: _ClassVar[int]
    BATTLE_PASS_FIELD_NUMBER: _ClassVar[int]
    BP_QUEST_LIST_FIELD_NUMBER: _ClassVar[int]
    SEASON_HISTORY_FIELD_NUMBER: _ClassVar[int]
    season_id: int
    battle_pass: _stru_battle_pass_pb2.BattlePass
    bp_quest_list: _stru_season_bp_quest_list_pb2.SeasonBpQuestList
    season_history: _containers.MessageMap[int, _stru_season_center_history_pb2.SeasonCenterHistory]
    def __init__(self, season_id: _Optional[int] = ..., battle_pass: _Optional[_Union[_stru_battle_pass_pb2.BattlePass, _Mapping]] = ..., bp_quest_list: _Optional[_Union[_stru_season_bp_quest_list_pb2.SeasonBpQuestList, _Mapping]] = ..., season_history: _Optional[_Mapping[int, _stru_season_center_history_pb2.SeasonCenterHistory]] = ...) -> None: ...
