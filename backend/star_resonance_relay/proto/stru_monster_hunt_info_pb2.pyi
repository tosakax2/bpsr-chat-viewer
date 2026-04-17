import stru_monster_hunt_target_pb2 as _stru_monster_hunt_target_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MonsterHuntInfo(_message.Message):
    __slots__ = ("monster_hunt_list", "cur_level", "cur_exp", "level_award_flag", "monster_hunt_refrsh_time")
    class MonsterHuntListEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_monster_hunt_target_pb2.MonsterHuntTarget
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_monster_hunt_target_pb2.MonsterHuntTarget, _Mapping]] = ...) -> None: ...
    class LevelAwardFlagEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class MonsterHuntRefrshTimeEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    MONSTER_HUNT_LIST_FIELD_NUMBER: _ClassVar[int]
    CUR_LEVEL_FIELD_NUMBER: _ClassVar[int]
    CUR_EXP_FIELD_NUMBER: _ClassVar[int]
    LEVEL_AWARD_FLAG_FIELD_NUMBER: _ClassVar[int]
    MONSTER_HUNT_REFRSH_TIME_FIELD_NUMBER: _ClassVar[int]
    monster_hunt_list: _containers.MessageMap[int, _stru_monster_hunt_target_pb2.MonsterHuntTarget]
    cur_level: int
    cur_exp: int
    level_award_flag: _containers.ScalarMap[int, int]
    monster_hunt_refrsh_time: _containers.ScalarMap[int, int]
    def __init__(self, monster_hunt_list: _Optional[_Mapping[int, _stru_monster_hunt_target_pb2.MonsterHuntTarget]] = ..., cur_level: _Optional[int] = ..., cur_exp: _Optional[int] = ..., level_award_flag: _Optional[_Mapping[int, int]] = ..., monster_hunt_refrsh_time: _Optional[_Mapping[int, int]] = ...) -> None: ...
