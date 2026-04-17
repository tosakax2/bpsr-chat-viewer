import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TalentPoolTableBase(_message.Message):
    __slots__ = ("id", "des", "sect_icon", "main_talent_id", "secondary_talent", "passive_talent", "talent_position", "recommend_talent", "school_des", "recommend_dimension", "school_icon", "player_school_icon", "fantasy_solution_list", "strategy_page")
    ID_FIELD_NUMBER: _ClassVar[int]
    DES_FIELD_NUMBER: _ClassVar[int]
    SECT_ICON_FIELD_NUMBER: _ClassVar[int]
    MAIN_TALENT_ID_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_TALENT_FIELD_NUMBER: _ClassVar[int]
    PASSIVE_TALENT_FIELD_NUMBER: _ClassVar[int]
    TALENT_POSITION_FIELD_NUMBER: _ClassVar[int]
    RECOMMEND_TALENT_FIELD_NUMBER: _ClassVar[int]
    SCHOOL_DES_FIELD_NUMBER: _ClassVar[int]
    RECOMMEND_DIMENSION_FIELD_NUMBER: _ClassVar[int]
    SCHOOL_ICON_FIELD_NUMBER: _ClassVar[int]
    PLAYER_SCHOOL_ICON_FIELD_NUMBER: _ClassVar[int]
    FANTASY_SOLUTION_LIST_FIELD_NUMBER: _ClassVar[int]
    STRATEGY_PAGE_FIELD_NUMBER: _ClassVar[int]
    id: int
    des: str
    sect_icon: str
    main_talent_id: int
    secondary_talent: _table_basic_pb2.int_array
    passive_talent: _table_basic_pb2.int_array
    talent_position: _table_basic_pb2.int_table
    recommend_talent: _table_basic_pb2.int_array
    school_des: _table_basic_pb2.mlstring
    recommend_dimension: _table_basic_pb2.mlstring
    school_icon: _table_basic_pb2.mlstring
    player_school_icon: _table_basic_pb2.mlstring
    fantasy_solution_list: _table_basic_pb2.int_array
    strategy_page: int
    def __init__(self, id: _Optional[int] = ..., des: _Optional[str] = ..., sect_icon: _Optional[str] = ..., main_talent_id: _Optional[int] = ..., secondary_talent: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., passive_talent: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., talent_position: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., recommend_talent: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., school_des: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., recommend_dimension: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., school_icon: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., player_school_icon: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., fantasy_solution_list: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., strategy_page: _Optional[int] = ...) -> None: ...

class TalentPoolTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: TalentPoolTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[TalentPoolTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, TalentPoolTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, TalentPoolTableBase]] = ...) -> None: ...
