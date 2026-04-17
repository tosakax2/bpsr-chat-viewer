import enum_monster_target_award_pb2 as _enum_monster_target_award_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MonsterTargetInfo(_message.Message):
    __slots__ = ("id", "target_uuid", "target_type", "target_num", "award_flag")
    ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_UUID_FIELD_NUMBER: _ClassVar[int]
    TARGET_TYPE_FIELD_NUMBER: _ClassVar[int]
    TARGET_NUM_FIELD_NUMBER: _ClassVar[int]
    AWARD_FLAG_FIELD_NUMBER: _ClassVar[int]
    id: int
    target_uuid: int
    target_type: int
    target_num: int
    award_flag: _enum_monster_target_award_pb2.MonsterTargetAward
    def __init__(self, id: _Optional[int] = ..., target_uuid: _Optional[int] = ..., target_type: _Optional[int] = ..., target_num: _Optional[int] = ..., award_flag: _Optional[_Union[_enum_monster_target_award_pb2.MonsterTargetAward, str]] = ...) -> None: ...
