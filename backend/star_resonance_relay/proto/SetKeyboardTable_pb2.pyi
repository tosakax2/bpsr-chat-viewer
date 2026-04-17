import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetKeyboardTableBase(_message.Message):
    __slots__ = ("id", "action_ids", "map_category_id", "set_des", "keyboard_des", "function_id", "sort", "show_switch", "go_back")
    ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_IDS_FIELD_NUMBER: _ClassVar[int]
    MAP_CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    SET_DES_FIELD_NUMBER: _ClassVar[int]
    KEYBOARD_DES_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_ID_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    SHOW_SWITCH_FIELD_NUMBER: _ClassVar[int]
    GO_BACK_FIELD_NUMBER: _ClassVar[int]
    id: int
    action_ids: _table_basic_pb2.int_array
    map_category_id: int
    set_des: _table_basic_pb2.mlstring
    keyboard_des: int
    function_id: int
    sort: int
    show_switch: int
    go_back: str
    def __init__(self, id: _Optional[int] = ..., action_ids: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., map_category_id: _Optional[int] = ..., set_des: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., keyboard_des: _Optional[int] = ..., function_id: _Optional[int] = ..., sort: _Optional[int] = ..., show_switch: _Optional[int] = ..., go_back: _Optional[str] = ...) -> None: ...

class SetKeyboardTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: SetKeyboardTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[SetKeyboardTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, SetKeyboardTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, SetKeyboardTableBase]] = ...) -> None: ...
