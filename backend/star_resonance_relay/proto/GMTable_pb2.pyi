import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GMTableBase(_message.Message):
    __slots__ = ("id", "gm_group", "type", "command", "parameter_or_content", "optional_parameter", "parameter_check", "button_show", "command_or_parameter_remark", "au_to_close")
    ID_FIELD_NUMBER: _ClassVar[int]
    GM_GROUP_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_OR_CONTENT_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_PARAMETER_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_CHECK_FIELD_NUMBER: _ClassVar[int]
    BUTTON_SHOW_FIELD_NUMBER: _ClassVar[int]
    COMMAND_OR_PARAMETER_REMARK_FIELD_NUMBER: _ClassVar[int]
    AU_TO_CLOSE_FIELD_NUMBER: _ClassVar[int]
    id: int
    gm_group: int
    type: int
    command: str
    parameter_or_content: _table_basic_pb2.string_array
    optional_parameter: _table_basic_pb2.string_array
    parameter_check: _table_basic_pb2.string_array
    button_show: _table_basic_pb2.mlstring
    command_or_parameter_remark: _table_basic_pb2.mlstring_array
    au_to_close: bool
    def __init__(self, id: _Optional[int] = ..., gm_group: _Optional[int] = ..., type: _Optional[int] = ..., command: _Optional[str] = ..., parameter_or_content: _Optional[_Union[_table_basic_pb2.string_array, _Mapping]] = ..., optional_parameter: _Optional[_Union[_table_basic_pb2.string_array, _Mapping]] = ..., parameter_check: _Optional[_Union[_table_basic_pb2.string_array, _Mapping]] = ..., button_show: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., command_or_parameter_remark: _Optional[_Union[_table_basic_pb2.mlstring_array, _Mapping]] = ..., au_to_close: bool = ...) -> None: ...

class GMTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: GMTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[GMTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, GMTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, GMTableBase]] = ...) -> None: ...
