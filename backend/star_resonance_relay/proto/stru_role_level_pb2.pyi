import stru_level_proficiency_pb2 as _stru_level_proficiency_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RoleLevel(_message.Message):
    __slots__ = ("level", "cur_level_exp", "received_level_list", "proficiency_info", "active_exp_map", "last_season_day", "bless_exp_pool", "grant_bless_exp", "accumulate_bless_exp", "accumulate_exp", "prev_season_max_lv")
    class ReceivedLevelListEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bool
        def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
    class ActiveExpMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    CUR_LEVEL_EXP_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_LEVEL_LIST_FIELD_NUMBER: _ClassVar[int]
    PROFICIENCY_INFO_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_EXP_MAP_FIELD_NUMBER: _ClassVar[int]
    LAST_SEASON_DAY_FIELD_NUMBER: _ClassVar[int]
    BLESS_EXP_POOL_FIELD_NUMBER: _ClassVar[int]
    GRANT_BLESS_EXP_FIELD_NUMBER: _ClassVar[int]
    ACCUMULATE_BLESS_EXP_FIELD_NUMBER: _ClassVar[int]
    ACCUMULATE_EXP_FIELD_NUMBER: _ClassVar[int]
    PREV_SEASON_MAX_LV_FIELD_NUMBER: _ClassVar[int]
    level: int
    cur_level_exp: int
    received_level_list: _containers.ScalarMap[int, bool]
    proficiency_info: _stru_level_proficiency_pb2.LevelProficiency
    active_exp_map: _containers.ScalarMap[int, int]
    last_season_day: int
    bless_exp_pool: int
    grant_bless_exp: int
    accumulate_bless_exp: int
    accumulate_exp: int
    prev_season_max_lv: int
    def __init__(self, level: _Optional[int] = ..., cur_level_exp: _Optional[int] = ..., received_level_list: _Optional[_Mapping[int, bool]] = ..., proficiency_info: _Optional[_Union[_stru_level_proficiency_pb2.LevelProficiency, _Mapping]] = ..., active_exp_map: _Optional[_Mapping[int, int]] = ..., last_season_day: _Optional[int] = ..., bless_exp_pool: _Optional[int] = ..., grant_bless_exp: _Optional[int] = ..., accumulate_bless_exp: _Optional[int] = ..., accumulate_exp: _Optional[int] = ..., prev_season_max_lv: _Optional[int] = ...) -> None: ...
