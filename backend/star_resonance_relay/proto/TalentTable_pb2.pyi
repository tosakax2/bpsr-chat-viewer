import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TalentTableBase(_message.Message):
    __slots__ = ("id", "talent_id", "des", "talent_name", "talent_icon", "talent_type", "talent_level", "talent_effect", "buff_value_key", "buff_par", "unlock", "pre_talent", "unlock_consume", "bd_tag_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    TALENT_ID_FIELD_NUMBER: _ClassVar[int]
    DES_FIELD_NUMBER: _ClassVar[int]
    TALENT_NAME_FIELD_NUMBER: _ClassVar[int]
    TALENT_ICON_FIELD_NUMBER: _ClassVar[int]
    TALENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    TALENT_LEVEL_FIELD_NUMBER: _ClassVar[int]
    TALENT_EFFECT_FIELD_NUMBER: _ClassVar[int]
    BUFF_VALUE_KEY_FIELD_NUMBER: _ClassVar[int]
    BUFF_PAR_FIELD_NUMBER: _ClassVar[int]
    UNLOCK_FIELD_NUMBER: _ClassVar[int]
    PRE_TALENT_FIELD_NUMBER: _ClassVar[int]
    UNLOCK_CONSUME_FIELD_NUMBER: _ClassVar[int]
    BD_TAG_ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    talent_id: int
    des: str
    talent_name: _table_basic_pb2.mlstring
    talent_icon: str
    talent_type: int
    talent_level: int
    talent_effect: _table_basic_pb2.int_table
    buff_value_key: _table_basic_pb2.string_table
    buff_par: _table_basic_pb2.int_table
    unlock: _table_basic_pb2.int_table
    pre_talent: _table_basic_pb2.int_table
    unlock_consume: _table_basic_pb2.int_table
    bd_tag_id: int
    def __init__(self, id: _Optional[int] = ..., talent_id: _Optional[int] = ..., des: _Optional[str] = ..., talent_name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., talent_icon: _Optional[str] = ..., talent_type: _Optional[int] = ..., talent_level: _Optional[int] = ..., talent_effect: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., buff_value_key: _Optional[_Union[_table_basic_pb2.string_table, _Mapping]] = ..., buff_par: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., unlock: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., pre_talent: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., unlock_consume: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., bd_tag_id: _Optional[int] = ...) -> None: ...

class TalentTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: TalentTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[TalentTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, TalentTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, TalentTableBase]] = ...) -> None: ...
