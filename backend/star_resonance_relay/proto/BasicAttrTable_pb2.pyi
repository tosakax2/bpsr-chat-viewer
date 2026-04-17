import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BasicAttrTableBase(_message.Message):
    __slots__ = ("id", "basic0", "grow_min0", "grow_times0", "basic2", "grow_min2", "grow_times2", "basic3", "grow_min3", "grow_times3", "basic4", "grow_min4", "grow_times4")
    ID_FIELD_NUMBER: _ClassVar[int]
    BASIC0_FIELD_NUMBER: _ClassVar[int]
    GROW_MIN0_FIELD_NUMBER: _ClassVar[int]
    GROW_TIMES0_FIELD_NUMBER: _ClassVar[int]
    BASIC2_FIELD_NUMBER: _ClassVar[int]
    GROW_MIN2_FIELD_NUMBER: _ClassVar[int]
    GROW_TIMES2_FIELD_NUMBER: _ClassVar[int]
    BASIC3_FIELD_NUMBER: _ClassVar[int]
    GROW_MIN3_FIELD_NUMBER: _ClassVar[int]
    GROW_TIMES3_FIELD_NUMBER: _ClassVar[int]
    BASIC4_FIELD_NUMBER: _ClassVar[int]
    GROW_MIN4_FIELD_NUMBER: _ClassVar[int]
    GROW_TIMES4_FIELD_NUMBER: _ClassVar[int]
    id: int
    basic0: int
    grow_min0: _table_basic_pb2.int_table
    grow_times0: _table_basic_pb2.int_array
    basic2: int
    grow_min2: _table_basic_pb2.int_table
    grow_times2: _table_basic_pb2.int_array
    basic3: int
    grow_min3: _table_basic_pb2.int_table
    grow_times3: _table_basic_pb2.int_array
    basic4: int
    grow_min4: _table_basic_pb2.int_table
    grow_times4: _table_basic_pb2.int_array
    def __init__(self, id: _Optional[int] = ..., basic0: _Optional[int] = ..., grow_min0: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., grow_times0: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., basic2: _Optional[int] = ..., grow_min2: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., grow_times2: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., basic3: _Optional[int] = ..., grow_min3: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., grow_times3: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., basic4: _Optional[int] = ..., grow_min4: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., grow_times4: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ...) -> None: ...

class BasicAttrTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: BasicAttrTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[BasicAttrTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, BasicAttrTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, BasicAttrTableBase]] = ...) -> None: ...
