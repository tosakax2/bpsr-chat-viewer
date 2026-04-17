import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CocktailRecipeTableBase(_message.Message):
    __slots__ = ("id", "name", "recipe_text", "introduction_text", "recipe", "model", "is_visible")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RECIPE_TEXT_FIELD_NUMBER: _ClassVar[int]
    INTRODUCTION_TEXT_FIELD_NUMBER: _ClassVar[int]
    RECIPE_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    IS_VISIBLE_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: _table_basic_pb2.mlstring
    recipe_text: _table_basic_pb2.mlstring
    introduction_text: _table_basic_pb2.mlstring
    recipe: _table_basic_pb2.int_table
    model: str
    is_visible: bool
    def __init__(self, id: _Optional[int] = ..., name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., recipe_text: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., introduction_text: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., recipe: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., model: _Optional[str] = ..., is_visible: bool = ...) -> None: ...

class CocktailRecipeTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: CocktailRecipeTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[CocktailRecipeTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, CocktailRecipeTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, CocktailRecipeTableBase]] = ...) -> None: ...
