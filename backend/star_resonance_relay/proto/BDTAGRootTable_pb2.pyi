import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BDTAGRootTableBase(_message.Message):
    __slots__ = ("id", "name", "root_type", "root_type_id", "skill_level", "tag_path")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ROOT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ROOT_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    SKILL_LEVEL_FIELD_NUMBER: _ClassVar[int]
    TAG_PATH_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    root_type: int
    root_type_id: int
    skill_level: int
    tag_path: _table_basic_pb2.string_array
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., root_type: _Optional[int] = ..., root_type_id: _Optional[int] = ..., skill_level: _Optional[int] = ..., tag_path: _Optional[_Union[_table_basic_pb2.string_array, _Mapping]] = ...) -> None: ...

class BDTAGRootTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: BDTAGRootTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[BDTAGRootTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, BDTAGRootTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, BDTAGRootTableBase]] = ...) -> None: ...
