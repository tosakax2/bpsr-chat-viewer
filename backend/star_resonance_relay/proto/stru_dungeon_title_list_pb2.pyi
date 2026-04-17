import stru_dungeon_title_info_pb2 as _stru_dungeon_title_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonTitleList(_message.Message):
    __slots__ = ("title_info",)
    class TitleInfoEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_dungeon_title_info_pb2.DungeonTitleInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_dungeon_title_info_pb2.DungeonTitleInfo, _Mapping]] = ...) -> None: ...
    TITLE_INFO_FIELD_NUMBER: _ClassVar[int]
    title_info: _containers.MessageMap[int, _stru_dungeon_title_info_pb2.DungeonTitleInfo]
    def __init__(self, title_info: _Optional[_Mapping[int, _stru_dungeon_title_info_pb2.DungeonTitleInfo]] = ...) -> None: ...
