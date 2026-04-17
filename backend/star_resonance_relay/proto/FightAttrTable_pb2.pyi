import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FightAttrTableBase(_message.Message):
    __slots__ = ("id", "enum_name", "name", "type", "is_class", "is_sync_me", "is_sync_aoi", "attr_lower_limit", "attr_upper_limit", "level", "attr_final", "attr_total", "attr_add", "attr_ex_add", "attr_per", "attr_ex_per", "attr_num_type", "official_name", "tip_template", "attr_des", "buff_show_attr_hud", "attr_icon")
    ID_FIELD_NUMBER: _ClassVar[int]
    ENUM_NAME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_CLASS_FIELD_NUMBER: _ClassVar[int]
    IS_SYNC_ME_FIELD_NUMBER: _ClassVar[int]
    IS_SYNC_AOI_FIELD_NUMBER: _ClassVar[int]
    ATTR_LOWER_LIMIT_FIELD_NUMBER: _ClassVar[int]
    ATTR_UPPER_LIMIT_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    ATTR_FINAL_FIELD_NUMBER: _ClassVar[int]
    ATTR_TOTAL_FIELD_NUMBER: _ClassVar[int]
    ATTR_ADD_FIELD_NUMBER: _ClassVar[int]
    ATTR_EX_ADD_FIELD_NUMBER: _ClassVar[int]
    ATTR_PER_FIELD_NUMBER: _ClassVar[int]
    ATTR_EX_PER_FIELD_NUMBER: _ClassVar[int]
    ATTR_NUM_TYPE_FIELD_NUMBER: _ClassVar[int]
    OFFICIAL_NAME_FIELD_NUMBER: _ClassVar[int]
    TIP_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    ATTR_DES_FIELD_NUMBER: _ClassVar[int]
    BUFF_SHOW_ATTR_HUD_FIELD_NUMBER: _ClassVar[int]
    ATTR_ICON_FIELD_NUMBER: _ClassVar[int]
    id: int
    enum_name: str
    name: str
    type: str
    is_class: bool
    is_sync_me: bool
    is_sync_aoi: bool
    attr_lower_limit: int
    attr_upper_limit: int
    level: int
    attr_final: int
    attr_total: int
    attr_add: int
    attr_ex_add: int
    attr_per: int
    attr_ex_per: int
    attr_num_type: int
    official_name: _table_basic_pb2.mlstring
    tip_template: _table_basic_pb2.mlstring
    attr_des: _table_basic_pb2.mlstring
    buff_show_attr_hud: int
    attr_icon: _table_basic_pb2.string_array
    def __init__(self, id: _Optional[int] = ..., enum_name: _Optional[str] = ..., name: _Optional[str] = ..., type: _Optional[str] = ..., is_class: bool = ..., is_sync_me: bool = ..., is_sync_aoi: bool = ..., attr_lower_limit: _Optional[int] = ..., attr_upper_limit: _Optional[int] = ..., level: _Optional[int] = ..., attr_final: _Optional[int] = ..., attr_total: _Optional[int] = ..., attr_add: _Optional[int] = ..., attr_ex_add: _Optional[int] = ..., attr_per: _Optional[int] = ..., attr_ex_per: _Optional[int] = ..., attr_num_type: _Optional[int] = ..., official_name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., tip_template: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., attr_des: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., buff_show_attr_hud: _Optional[int] = ..., attr_icon: _Optional[_Union[_table_basic_pb2.string_array, _Mapping]] = ...) -> None: ...

class FightAttrTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: FightAttrTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[FightAttrTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, FightAttrTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, FightAttrTableBase]] = ...) -> None: ...
