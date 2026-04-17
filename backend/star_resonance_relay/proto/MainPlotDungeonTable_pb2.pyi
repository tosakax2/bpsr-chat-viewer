from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MainPlotDungeonTableBase(_message.Message):
    __slots__ = ("dungeon_id", "background", "red_dot_index")
    DUNGEON_ID_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_FIELD_NUMBER: _ClassVar[int]
    RED_DOT_INDEX_FIELD_NUMBER: _ClassVar[int]
    dungeon_id: int
    background: str
    red_dot_index: int
    def __init__(self, dungeon_id: _Optional[int] = ..., background: _Optional[str] = ..., red_dot_index: _Optional[int] = ...) -> None: ...

class MainPlotDungeonTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: MainPlotDungeonTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[MainPlotDungeonTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, MainPlotDungeonTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, MainPlotDungeonTableBase]] = ...) -> None: ...
