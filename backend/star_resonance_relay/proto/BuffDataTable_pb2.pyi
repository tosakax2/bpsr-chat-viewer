import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BuffDataTableBase(_message.Message):
    __slots__ = ("buff_id", "action_array", "effect_array", "material_array", "w_wise_array")
    BUFF_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_ARRAY_FIELD_NUMBER: _ClassVar[int]
    EFFECT_ARRAY_FIELD_NUMBER: _ClassVar[int]
    MATERIAL_ARRAY_FIELD_NUMBER: _ClassVar[int]
    W_WISE_ARRAY_FIELD_NUMBER: _ClassVar[int]
    buff_id: int
    action_array: _table_basic_pb2.int64_array
    effect_array: _table_basic_pb2.int64_array
    material_array: _table_basic_pb2.int64_array
    w_wise_array: _table_basic_pb2.int64_array
    def __init__(self, buff_id: _Optional[int] = ..., action_array: _Optional[_Union[_table_basic_pb2.int64_array, _Mapping]] = ..., effect_array: _Optional[_Union[_table_basic_pb2.int64_array, _Mapping]] = ..., material_array: _Optional[_Union[_table_basic_pb2.int64_array, _Mapping]] = ..., w_wise_array: _Optional[_Union[_table_basic_pb2.int64_array, _Mapping]] = ...) -> None: ...

class BuffDataTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: BuffDataTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[BuffDataTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, BuffDataTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, BuffDataTableBase]] = ...) -> None: ...
