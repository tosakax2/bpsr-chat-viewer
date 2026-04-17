import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BDTAGLinkTableBase(_message.Message):
    __slots__ = ("id", "note", "note_type", "find_type", "find_body", "find_conditions", "target_para", "skill_level_type", "target_node_type")
    ID_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    NOTE_TYPE_FIELD_NUMBER: _ClassVar[int]
    FIND_TYPE_FIELD_NUMBER: _ClassVar[int]
    FIND_BODY_FIELD_NUMBER: _ClassVar[int]
    FIND_CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    TARGET_PARA_FIELD_NUMBER: _ClassVar[int]
    SKILL_LEVEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    TARGET_NODE_TYPE_FIELD_NUMBER: _ClassVar[int]
    id: int
    note: str
    note_type: int
    find_type: int
    find_body: str
    find_conditions: _table_basic_pb2.string_table
    target_para: str
    skill_level_type: int
    target_node_type: int
    def __init__(self, id: _Optional[int] = ..., note: _Optional[str] = ..., note_type: _Optional[int] = ..., find_type: _Optional[int] = ..., find_body: _Optional[str] = ..., find_conditions: _Optional[_Union[_table_basic_pb2.string_table, _Mapping]] = ..., target_para: _Optional[str] = ..., skill_level_type: _Optional[int] = ..., target_node_type: _Optional[int] = ...) -> None: ...

class BDTAGLinkTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: BDTAGLinkTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[BDTAGLinkTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, BDTAGLinkTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, BDTAGLinkTableBase]] = ...) -> None: ...
