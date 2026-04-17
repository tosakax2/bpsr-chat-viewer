import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HelpLibraryTableBase(_message.Message):
    __slots__ = ("sort_id", "id", "type", "type_group", "main_title", "help_group", "group_name", "title", "content", "res", "sequence", "duration_time", "event_type", "param", "button", "function_id")
    SORT_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TYPE_GROUP_FIELD_NUMBER: _ClassVar[int]
    MAIN_TITLE_FIELD_NUMBER: _ClassVar[int]
    HELP_GROUP_FIELD_NUMBER: _ClassVar[int]
    GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    RES_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    DURATION_TIME_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PARAM_FIELD_NUMBER: _ClassVar[int]
    BUTTON_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_ID_FIELD_NUMBER: _ClassVar[int]
    sort_id: int
    id: int
    type: int
    type_group: int
    main_title: _table_basic_pb2.mlstring
    help_group: int
    group_name: _table_basic_pb2.mlstring
    title: _table_basic_pb2.mlstring
    content: _table_basic_pb2.mlstring_array
    res: _table_basic_pb2.string_array
    sequence: int
    duration_time: int
    event_type: int
    param: str
    button: _table_basic_pb2.mlstring
    function_id: int
    def __init__(self, sort_id: _Optional[int] = ..., id: _Optional[int] = ..., type: _Optional[int] = ..., type_group: _Optional[int] = ..., main_title: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., help_group: _Optional[int] = ..., group_name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., title: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., content: _Optional[_Union[_table_basic_pb2.mlstring_array, _Mapping]] = ..., res: _Optional[_Union[_table_basic_pb2.string_array, _Mapping]] = ..., sequence: _Optional[int] = ..., duration_time: _Optional[int] = ..., event_type: _Optional[int] = ..., param: _Optional[str] = ..., button: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., function_id: _Optional[int] = ...) -> None: ...

class HelpLibraryTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: HelpLibraryTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[HelpLibraryTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, HelpLibraryTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, HelpLibraryTableBase]] = ...) -> None: ...
