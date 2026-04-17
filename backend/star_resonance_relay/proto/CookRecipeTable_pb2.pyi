import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CookRecipeTableBase(_message.Message):
    __slots__ = ("id", "recipe_name", "consumable_id", "bad_dish_id", "bad_dish_name", "bad_dish_condition", "unlock_condition")
    ID_FIELD_NUMBER: _ClassVar[int]
    RECIPE_NAME_FIELD_NUMBER: _ClassVar[int]
    CONSUMABLE_ID_FIELD_NUMBER: _ClassVar[int]
    BAD_DISH_ID_FIELD_NUMBER: _ClassVar[int]
    BAD_DISH_NAME_FIELD_NUMBER: _ClassVar[int]
    BAD_DISH_CONDITION_FIELD_NUMBER: _ClassVar[int]
    UNLOCK_CONDITION_FIELD_NUMBER: _ClassVar[int]
    id: int
    recipe_name: _table_basic_pb2.mlstring
    consumable_id: _table_basic_pb2.int_table
    bad_dish_id: int
    bad_dish_name: _table_basic_pb2.mlstring
    bad_dish_condition: int
    unlock_condition: int
    def __init__(self, id: _Optional[int] = ..., recipe_name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., consumable_id: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., bad_dish_id: _Optional[int] = ..., bad_dish_name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., bad_dish_condition: _Optional[int] = ..., unlock_condition: _Optional[int] = ...) -> None: ...

class CookRecipeTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: CookRecipeTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[CookRecipeTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, CookRecipeTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, CookRecipeTableBase]] = ...) -> None: ...
