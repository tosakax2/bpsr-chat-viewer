import stru_battle_pass_pb2 as _stru_battle_pass_pb2
import stru_season_bp_quest_list_pb2 as _stru_season_bp_quest_list_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SeasonCenterHistory(_message.Message):
    __slots__ = ("battle_pass", "bp_quest_list")
    BATTLE_PASS_FIELD_NUMBER: _ClassVar[int]
    BP_QUEST_LIST_FIELD_NUMBER: _ClassVar[int]
    battle_pass: _stru_battle_pass_pb2.BattlePass
    bp_quest_list: _stru_season_bp_quest_list_pb2.SeasonBpQuestList
    def __init__(self, battle_pass: _Optional[_Union[_stru_battle_pass_pb2.BattlePass, _Mapping]] = ..., bp_quest_list: _Optional[_Union[_stru_season_bp_quest_list_pb2.SeasonBpQuestList, _Mapping]] = ...) -> None: ...
