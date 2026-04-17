import stru_monster_target_info_pb2 as _stru_monster_target_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MonsterHuntTarget(_message.Message):
    __slots__ = ("monster_id", "target_info_list")
    class TargetInfoListEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_monster_target_info_pb2.MonsterTargetInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_monster_target_info_pb2.MonsterTargetInfo, _Mapping]] = ...) -> None: ...
    MONSTER_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_INFO_LIST_FIELD_NUMBER: _ClassVar[int]
    monster_id: int
    target_info_list: _containers.MessageMap[int, _stru_monster_target_info_pb2.MonsterTargetInfo]
    def __init__(self, monster_id: _Optional[int] = ..., target_info_list: _Optional[_Mapping[int, _stru_monster_target_info_pb2.MonsterTargetInfo]] = ...) -> None: ...
