from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CounterTableBase(_message.Message):
    __slots__ = ("id", "name", "time_table_id", "refresh_num", "limit")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TIME_TABLE_ID_FIELD_NUMBER: _ClassVar[int]
    REFRESH_NUM_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    time_table_id: int
    refresh_num: int
    limit: int
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., time_table_id: _Optional[int] = ..., refresh_num: _Optional[int] = ..., limit: _Optional[int] = ...) -> None: ...

class CounterTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: CounterTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[CounterTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, CounterTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, CounterTableBase]] = ...) -> None: ...
