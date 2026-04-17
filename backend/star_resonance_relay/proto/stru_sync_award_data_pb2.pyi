import stru_level_up_award_pb2 as _stru_level_up_award_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SyncAwardData(_message.Message):
    __slots__ = ("level_up_award_infos",)
    class LevelUpAwardInfosEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_level_up_award_pb2.LevelUpAward
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_level_up_award_pb2.LevelUpAward, _Mapping]] = ...) -> None: ...
    LEVEL_UP_AWARD_INFOS_FIELD_NUMBER: _ClassVar[int]
    level_up_award_infos: _containers.MessageMap[int, _stru_level_up_award_pb2.LevelUpAward]
    def __init__(self, level_up_award_infos: _Optional[_Mapping[int, _stru_level_up_award_pb2.LevelUpAward]] = ...) -> None: ...
