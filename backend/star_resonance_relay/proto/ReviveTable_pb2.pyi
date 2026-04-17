import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReviveTableBase(_message.Message):
    __slots__ = ("id", "name", "type", "consume", "count_down", "before_buff_id", "wait_time", "is_boss_can_revive")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CONSUME_FIELD_NUMBER: _ClassVar[int]
    COUNT_DOWN_FIELD_NUMBER: _ClassVar[int]
    BEFORE_BUFF_ID_FIELD_NUMBER: _ClassVar[int]
    WAIT_TIME_FIELD_NUMBER: _ClassVar[int]
    IS_BOSS_CAN_REVIVE_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: _table_basic_pb2.mlstring
    type: int
    consume: _table_basic_pb2.int_array
    count_down: int
    before_buff_id: _table_basic_pb2.int_array
    wait_time: int
    is_boss_can_revive: int
    def __init__(self, id: _Optional[int] = ..., name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., type: _Optional[int] = ..., consume: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., count_down: _Optional[int] = ..., before_buff_id: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., wait_time: _Optional[int] = ..., is_boss_can_revive: _Optional[int] = ...) -> None: ...

class ReviveTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ReviveTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ReviveTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, ReviveTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, ReviveTableBase]] = ...) -> None: ...
