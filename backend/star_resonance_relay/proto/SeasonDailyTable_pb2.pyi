from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SeasonDailyTableBase(_message.Message):
    __slots__ = ("id", "season", "day", "daily_equip_level", "grow_range_add")
    ID_FIELD_NUMBER: _ClassVar[int]
    SEASON_FIELD_NUMBER: _ClassVar[int]
    DAY_FIELD_NUMBER: _ClassVar[int]
    DAILY_EQUIP_LEVEL_FIELD_NUMBER: _ClassVar[int]
    GROW_RANGE_ADD_FIELD_NUMBER: _ClassVar[int]
    id: int
    season: int
    day: int
    daily_equip_level: int
    grow_range_add: int
    def __init__(self, id: _Optional[int] = ..., season: _Optional[int] = ..., day: _Optional[int] = ..., daily_equip_level: _Optional[int] = ..., grow_range_add: _Optional[int] = ...) -> None: ...

class SeasonDailyTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: SeasonDailyTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[SeasonDailyTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, SeasonDailyTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, SeasonDailyTableBase]] = ...) -> None: ...
