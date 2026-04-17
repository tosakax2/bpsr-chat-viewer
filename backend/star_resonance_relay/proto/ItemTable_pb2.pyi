import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ItemTableBase(_message.Message):
    __slots__ = ("id", "name", "icon", "type", "group_id", "quality", "sort_id", "description", "sex_limit", "overlap", "time_type", "time_limit", "drop_model", "correlation_id", "is_special_display", "special_display_type", "quick_use")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    QUALITY_FIELD_NUMBER: _ClassVar[int]
    SORT_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SEX_LIMIT_FIELD_NUMBER: _ClassVar[int]
    OVERLAP_FIELD_NUMBER: _ClassVar[int]
    TIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIME_LIMIT_FIELD_NUMBER: _ClassVar[int]
    DROP_MODEL_FIELD_NUMBER: _ClassVar[int]
    CORRELATION_ID_FIELD_NUMBER: _ClassVar[int]
    IS_SPECIAL_DISPLAY_FIELD_NUMBER: _ClassVar[int]
    SPECIAL_DISPLAY_TYPE_FIELD_NUMBER: _ClassVar[int]
    QUICK_USE_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: _table_basic_pb2.mlstring
    icon: str
    type: int
    group_id: int
    quality: int
    sort_id: int
    description: _table_basic_pb2.mlstring
    sex_limit: int
    overlap: int
    time_type: int
    time_limit: str
    drop_model: int
    correlation_id: int
    is_special_display: bool
    special_display_type: int
    quick_use: int
    def __init__(self, id: _Optional[int] = ..., name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., icon: _Optional[str] = ..., type: _Optional[int] = ..., group_id: _Optional[int] = ..., quality: _Optional[int] = ..., sort_id: _Optional[int] = ..., description: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., sex_limit: _Optional[int] = ..., overlap: _Optional[int] = ..., time_type: _Optional[int] = ..., time_limit: _Optional[str] = ..., drop_model: _Optional[int] = ..., correlation_id: _Optional[int] = ..., is_special_display: bool = ..., special_display_type: _Optional[int] = ..., quick_use: _Optional[int] = ...) -> None: ...

class ItemTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ItemTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ItemTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, ItemTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, ItemTableBase]] = ...) -> None: ...
