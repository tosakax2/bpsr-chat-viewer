import stru_dungeon_enter_count_pb2 as _stru_dungeon_enter_count_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonEnterLimit(_message.Message):
    __slots__ = ("enter_count",)
    class EnterCountEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_dungeon_enter_count_pb2.DungeonEnterCount
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_dungeon_enter_count_pb2.DungeonEnterCount, _Mapping]] = ...) -> None: ...
    ENTER_COUNT_FIELD_NUMBER: _ClassVar[int]
    enter_count: _containers.MessageMap[int, _stru_dungeon_enter_count_pb2.DungeonEnterCount]
    def __init__(self, enter_count: _Optional[_Mapping[int, _stru_dungeon_enter_count_pb2.DungeonEnterCount]] = ...) -> None: ...
