import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RecipeTableBase(_message.Message):
    __slots__ = ("id", "name", "recipe_text", "recipe_icon", "recipe_type")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RECIPE_TEXT_FIELD_NUMBER: _ClassVar[int]
    RECIPE_ICON_FIELD_NUMBER: _ClassVar[int]
    RECIPE_TYPE_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: _table_basic_pb2.mlstring
    recipe_text: _table_basic_pb2.mlstring
    recipe_icon: str
    recipe_type: int
    def __init__(self, id: _Optional[int] = ..., name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., recipe_text: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., recipe_icon: _Optional[str] = ..., recipe_type: _Optional[int] = ...) -> None: ...

class RecipeTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: RecipeTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[RecipeTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, RecipeTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, RecipeTableBase]] = ...) -> None: ...
