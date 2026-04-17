import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FriendshipValueGetEventsBase(_message.Message):
    __slots__ = ("id", "event_parameter", "once_value", "day_max_value")
    ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_PARAMETER_FIELD_NUMBER: _ClassVar[int]
    ONCE_VALUE_FIELD_NUMBER: _ClassVar[int]
    DAY_MAX_VALUE_FIELD_NUMBER: _ClassVar[int]
    id: int
    event_parameter: _table_basic_pb2.int_table
    once_value: int
    day_max_value: int
    def __init__(self, id: _Optional[int] = ..., event_parameter: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., once_value: _Optional[int] = ..., day_max_value: _Optional[int] = ...) -> None: ...

class FriendshipValueGetEventsMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: FriendshipValueGetEventsBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[FriendshipValueGetEventsBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, FriendshipValueGetEventsBase]
    def __init__(self, datas: _Optional[_Mapping[int, FriendshipValueGetEventsBase]] = ...) -> None: ...
