import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StaticInteractiveClassBase(_message.Message):
    __slots__ = ("id", "interation_template", "player_action_start", "player_action_loop", "player_action_end", "exit_type")
    ID_FIELD_NUMBER: _ClassVar[int]
    INTERATION_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    PLAYER_ACTION_START_FIELD_NUMBER: _ClassVar[int]
    PLAYER_ACTION_LOOP_FIELD_NUMBER: _ClassVar[int]
    PLAYER_ACTION_END_FIELD_NUMBER: _ClassVar[int]
    EXIT_TYPE_FIELD_NUMBER: _ClassVar[int]
    id: int
    interation_template: int
    player_action_start: _table_basic_pb2.string_array
    player_action_loop: _table_basic_pb2.string_array
    player_action_end: _table_basic_pb2.string_array
    exit_type: int
    def __init__(self, id: _Optional[int] = ..., interation_template: _Optional[int] = ..., player_action_start: _Optional[_Union[_table_basic_pb2.string_array, _Mapping]] = ..., player_action_loop: _Optional[_Union[_table_basic_pb2.string_array, _Mapping]] = ..., player_action_end: _Optional[_Union[_table_basic_pb2.string_array, _Mapping]] = ..., exit_type: _Optional[int] = ...) -> None: ...

class StaticInteractiveClassMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: StaticInteractiveClassBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[StaticInteractiveClassBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, StaticInteractiveClassBase]
    def __init__(self, datas: _Optional[_Mapping[int, StaticInteractiveClassBase]] = ...) -> None: ...
