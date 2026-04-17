import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TrapTableBase(_message.Message):
    __slots__ = ("id", "name", "skill_id", "buff_ids", "trigger_range", "attribute_id", "model_id", "life_info", "tags")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    BUFF_IDS_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_RANGE_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    LIFE_INFO_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    skill_id: int
    buff_ids: _table_basic_pb2.int_array
    trigger_range: float
    attribute_id: int
    model_id: int
    life_info: _table_basic_pb2.int_array
    tags: _table_basic_pb2.int_array
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., skill_id: _Optional[int] = ..., buff_ids: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., trigger_range: _Optional[float] = ..., attribute_id: _Optional[int] = ..., model_id: _Optional[int] = ..., life_info: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., tags: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ...) -> None: ...

class TrapTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: TrapTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[TrapTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, TrapTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, TrapTableBase]] = ...) -> None: ...
