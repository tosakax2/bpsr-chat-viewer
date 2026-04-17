import stru_dungeon_target_data_pb2 as _stru_dungeon_target_data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonTarget(_message.Message):
    __slots__ = ("target_data",)
    class TargetDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_dungeon_target_data_pb2.DungeonTargetData
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_dungeon_target_data_pb2.DungeonTargetData, _Mapping]] = ...) -> None: ...
    TARGET_DATA_FIELD_NUMBER: _ClassVar[int]
    target_data: _containers.MessageMap[int, _stru_dungeon_target_data_pb2.DungeonTargetData]
    def __init__(self, target_data: _Optional[_Mapping[int, _stru_dungeon_target_data_pb2.DungeonTargetData]] = ...) -> None: ...
