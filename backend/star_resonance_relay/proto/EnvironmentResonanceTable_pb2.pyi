import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EnvironmentResonanceTableBase(_message.Message):
    __slots__ = ("id", "name", "desc", "pivot_id", "button", "skill", "position", "scene_tag", "time", "trigger_buff_ids", "slot_type")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESC_FIELD_NUMBER: _ClassVar[int]
    PIVOT_ID_FIELD_NUMBER: _ClassVar[int]
    BUTTON_FIELD_NUMBER: _ClassVar[int]
    SKILL_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    SCENE_TAG_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_BUFF_IDS_FIELD_NUMBER: _ClassVar[int]
    SLOT_TYPE_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: _table_basic_pb2.mlstring
    desc: _table_basic_pb2.mlstring
    pivot_id: int
    button: _table_basic_pb2.mlstring
    skill: _table_basic_pb2.int_array
    position: int
    scene_tag: int
    time: int
    trigger_buff_ids: _table_basic_pb2.int_array
    slot_type: int
    def __init__(self, id: _Optional[int] = ..., name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., desc: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., pivot_id: _Optional[int] = ..., button: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., skill: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., position: _Optional[int] = ..., scene_tag: _Optional[int] = ..., time: _Optional[int] = ..., trigger_buff_ids: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., slot_type: _Optional[int] = ...) -> None: ...

class EnvironmentResonanceTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: EnvironmentResonanceTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[EnvironmentResonanceTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, EnvironmentResonanceTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, EnvironmentResonanceTableBase]] = ...) -> None: ...
