import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AwardAttrFixRatioTableBase(_message.Message):
    __slots__ = ("id", "attr_id", "type", "item_type", "item_params")
    ID_FIELD_NUMBER: _ClassVar[int]
    ATTR_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ITEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    ITEM_PARAMS_FIELD_NUMBER: _ClassVar[int]
    id: int
    attr_id: int
    type: int
    item_type: int
    item_params: _table_basic_pb2.int_table
    def __init__(self, id: _Optional[int] = ..., attr_id: _Optional[int] = ..., type: _Optional[int] = ..., item_type: _Optional[int] = ..., item_params: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ...) -> None: ...

class AwardAttrFixRatioTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: AwardAttrFixRatioTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[AwardAttrFixRatioTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, AwardAttrFixRatioTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, AwardAttrFixRatioTableBase]] = ...) -> None: ...
