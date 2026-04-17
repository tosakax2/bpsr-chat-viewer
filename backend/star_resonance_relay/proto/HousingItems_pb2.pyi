import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HousingItemsBase(_message.Message):
    __slots__ = ("id", "sort_id", "name", "icon", "type", "quality", "res")
    ID_FIELD_NUMBER: _ClassVar[int]
    SORT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    QUALITY_FIELD_NUMBER: _ClassVar[int]
    RES_FIELD_NUMBER: _ClassVar[int]
    id: int
    sort_id: int
    name: _table_basic_pb2.mlstring
    icon: str
    type: int
    quality: int
    res: str
    def __init__(self, id: _Optional[int] = ..., sort_id: _Optional[int] = ..., name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., icon: _Optional[str] = ..., type: _Optional[int] = ..., quality: _Optional[int] = ..., res: _Optional[str] = ...) -> None: ...

class HousingItemsMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: HousingItemsBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[HousingItemsBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, HousingItemsBase]
    def __init__(self, datas: _Optional[_Mapping[int, HousingItemsBase]] = ...) -> None: ...
