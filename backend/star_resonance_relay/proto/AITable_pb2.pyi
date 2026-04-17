import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AITableBase(_message.Message):
    __slots__ = ("id", "remarks", "normal_sub_tree", "is_recover_normal", "is_patrol", "is_play_action", "play_action_probability", "play_action_mode", "play_action_id", "is_random_move", "random_move_probability", "random_move_radius", "is_alert_normal_patrol", "is_walking_around", "way_point_name", "alert_normal_patrol_path", "is_alert_action", "alert_action_list", "normal_play_sub_tree", "battle_action_id_array", "battle_action_release_probability", "is_play_action_when_into_battle", "is_play_action_only_normal_into_battle", "in_battle_action_id", "alert_in_battle_action_id", "is_have_battle_action", "battle_skill_release_probability", "battle_skill_id", "normal_battle_sub_tree", "skill_release_probability", "is_not_move", "is_skill_release_close", "is_release_skill_when_into_battle", "normal_into_battle_skill_id", "battle_alert_sub_tree", "is_alert_move_require", "chase_and_alert_move_probability", "is_chase_monster", "is_have_back_skill", "back_skill_id", "is_need_translation_alert_move", "alert_move_probability", "alert_speed", "min_alert_dis", "max_alert_dis", "min_alert_move_time", "max_alert_move_time", "min_alert_back_time", "max_alert_back_time", "to_battle_action_json_name", "is_play_vigilance_action", "vigilance_action_json_name")
    ID_FIELD_NUMBER: _ClassVar[int]
    REMARKS_FIELD_NUMBER: _ClassVar[int]
    NORMAL_SUB_TREE_FIELD_NUMBER: _ClassVar[int]
    IS_RECOVER_NORMAL_FIELD_NUMBER: _ClassVar[int]
    IS_PATROL_FIELD_NUMBER: _ClassVar[int]
    IS_PLAY_ACTION_FIELD_NUMBER: _ClassVar[int]
    PLAY_ACTION_PROBABILITY_FIELD_NUMBER: _ClassVar[int]
    PLAY_ACTION_MODE_FIELD_NUMBER: _ClassVar[int]
    PLAY_ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    IS_RANDOM_MOVE_FIELD_NUMBER: _ClassVar[int]
    RANDOM_MOVE_PROBABILITY_FIELD_NUMBER: _ClassVar[int]
    RANDOM_MOVE_RADIUS_FIELD_NUMBER: _ClassVar[int]
    IS_ALERT_NORMAL_PATROL_FIELD_NUMBER: _ClassVar[int]
    IS_WALKING_AROUND_FIELD_NUMBER: _ClassVar[int]
    WAY_POINT_NAME_FIELD_NUMBER: _ClassVar[int]
    ALERT_NORMAL_PATROL_PATH_FIELD_NUMBER: _ClassVar[int]
    IS_ALERT_ACTION_FIELD_NUMBER: _ClassVar[int]
    ALERT_ACTION_LIST_FIELD_NUMBER: _ClassVar[int]
    NORMAL_PLAY_SUB_TREE_FIELD_NUMBER: _ClassVar[int]
    BATTLE_ACTION_ID_ARRAY_FIELD_NUMBER: _ClassVar[int]
    BATTLE_ACTION_RELEASE_PROBABILITY_FIELD_NUMBER: _ClassVar[int]
    IS_PLAY_ACTION_WHEN_INTO_BATTLE_FIELD_NUMBER: _ClassVar[int]
    IS_PLAY_ACTION_ONLY_NORMAL_INTO_BATTLE_FIELD_NUMBER: _ClassVar[int]
    IN_BATTLE_ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    ALERT_IN_BATTLE_ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    IS_HAVE_BATTLE_ACTION_FIELD_NUMBER: _ClassVar[int]
    BATTLE_SKILL_RELEASE_PROBABILITY_FIELD_NUMBER: _ClassVar[int]
    BATTLE_SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    NORMAL_BATTLE_SUB_TREE_FIELD_NUMBER: _ClassVar[int]
    SKILL_RELEASE_PROBABILITY_FIELD_NUMBER: _ClassVar[int]
    IS_NOT_MOVE_FIELD_NUMBER: _ClassVar[int]
    IS_SKILL_RELEASE_CLOSE_FIELD_NUMBER: _ClassVar[int]
    IS_RELEASE_SKILL_WHEN_INTO_BATTLE_FIELD_NUMBER: _ClassVar[int]
    NORMAL_INTO_BATTLE_SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    BATTLE_ALERT_SUB_TREE_FIELD_NUMBER: _ClassVar[int]
    IS_ALERT_MOVE_REQUIRE_FIELD_NUMBER: _ClassVar[int]
    CHASE_AND_ALERT_MOVE_PROBABILITY_FIELD_NUMBER: _ClassVar[int]
    IS_CHASE_MONSTER_FIELD_NUMBER: _ClassVar[int]
    IS_HAVE_BACK_SKILL_FIELD_NUMBER: _ClassVar[int]
    BACK_SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    IS_NEED_TRANSLATION_ALERT_MOVE_FIELD_NUMBER: _ClassVar[int]
    ALERT_MOVE_PROBABILITY_FIELD_NUMBER: _ClassVar[int]
    ALERT_SPEED_FIELD_NUMBER: _ClassVar[int]
    MIN_ALERT_DIS_FIELD_NUMBER: _ClassVar[int]
    MAX_ALERT_DIS_FIELD_NUMBER: _ClassVar[int]
    MIN_ALERT_MOVE_TIME_FIELD_NUMBER: _ClassVar[int]
    MAX_ALERT_MOVE_TIME_FIELD_NUMBER: _ClassVar[int]
    MIN_ALERT_BACK_TIME_FIELD_NUMBER: _ClassVar[int]
    MAX_ALERT_BACK_TIME_FIELD_NUMBER: _ClassVar[int]
    TO_BATTLE_ACTION_JSON_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_PLAY_VIGILANCE_ACTION_FIELD_NUMBER: _ClassVar[int]
    VIGILANCE_ACTION_JSON_NAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    remarks: str
    normal_sub_tree: str
    is_recover_normal: bool
    is_patrol: bool
    is_play_action: bool
    play_action_probability: int
    play_action_mode: int
    play_action_id: _table_basic_pb2.int_array
    is_random_move: bool
    random_move_probability: int
    random_move_radius: float
    is_alert_normal_patrol: bool
    is_walking_around: bool
    way_point_name: str
    alert_normal_patrol_path: str
    is_alert_action: bool
    alert_action_list: _table_basic_pb2.int_array
    normal_play_sub_tree: str
    battle_action_id_array: _table_basic_pb2.string_array
    battle_action_release_probability: int
    is_play_action_when_into_battle: bool
    is_play_action_only_normal_into_battle: bool
    in_battle_action_id: int
    alert_in_battle_action_id: int
    is_have_battle_action: bool
    battle_skill_release_probability: int
    battle_skill_id: int
    normal_battle_sub_tree: str
    skill_release_probability: int
    is_not_move: bool
    is_skill_release_close: bool
    is_release_skill_when_into_battle: bool
    normal_into_battle_skill_id: int
    battle_alert_sub_tree: str
    is_alert_move_require: bool
    chase_and_alert_move_probability: int
    is_chase_monster: bool
    is_have_back_skill: bool
    back_skill_id: int
    is_need_translation_alert_move: bool
    alert_move_probability: int
    alert_speed: float
    min_alert_dis: float
    max_alert_dis: float
    min_alert_move_time: int
    max_alert_move_time: int
    min_alert_back_time: int
    max_alert_back_time: int
    to_battle_action_json_name: str
    is_play_vigilance_action: bool
    vigilance_action_json_name: str
    def __init__(self, id: _Optional[int] = ..., remarks: _Optional[str] = ..., normal_sub_tree: _Optional[str] = ..., is_recover_normal: bool = ..., is_patrol: bool = ..., is_play_action: bool = ..., play_action_probability: _Optional[int] = ..., play_action_mode: _Optional[int] = ..., play_action_id: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., is_random_move: bool = ..., random_move_probability: _Optional[int] = ..., random_move_radius: _Optional[float] = ..., is_alert_normal_patrol: bool = ..., is_walking_around: bool = ..., way_point_name: _Optional[str] = ..., alert_normal_patrol_path: _Optional[str] = ..., is_alert_action: bool = ..., alert_action_list: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., normal_play_sub_tree: _Optional[str] = ..., battle_action_id_array: _Optional[_Union[_table_basic_pb2.string_array, _Mapping]] = ..., battle_action_release_probability: _Optional[int] = ..., is_play_action_when_into_battle: bool = ..., is_play_action_only_normal_into_battle: bool = ..., in_battle_action_id: _Optional[int] = ..., alert_in_battle_action_id: _Optional[int] = ..., is_have_battle_action: bool = ..., battle_skill_release_probability: _Optional[int] = ..., battle_skill_id: _Optional[int] = ..., normal_battle_sub_tree: _Optional[str] = ..., skill_release_probability: _Optional[int] = ..., is_not_move: bool = ..., is_skill_release_close: bool = ..., is_release_skill_when_into_battle: bool = ..., normal_into_battle_skill_id: _Optional[int] = ..., battle_alert_sub_tree: _Optional[str] = ..., is_alert_move_require: bool = ..., chase_and_alert_move_probability: _Optional[int] = ..., is_chase_monster: bool = ..., is_have_back_skill: bool = ..., back_skill_id: _Optional[int] = ..., is_need_translation_alert_move: bool = ..., alert_move_probability: _Optional[int] = ..., alert_speed: _Optional[float] = ..., min_alert_dis: _Optional[float] = ..., max_alert_dis: _Optional[float] = ..., min_alert_move_time: _Optional[int] = ..., max_alert_move_time: _Optional[int] = ..., min_alert_back_time: _Optional[int] = ..., max_alert_back_time: _Optional[int] = ..., to_battle_action_json_name: _Optional[str] = ..., is_play_vigilance_action: bool = ..., vigilance_action_json_name: _Optional[str] = ...) -> None: ...

class AITableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: AITableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[AITableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, AITableBase]
    def __init__(self, datas: _Optional[_Mapping[int, AITableBase]] = ...) -> None: ...
