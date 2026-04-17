import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MaterialPriorityTableBase(_message.Message):
    __slots__ = ("id", "name", "material_file_path", "material_priority", "material_type")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MATERIAL_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    MATERIAL_PRIORITY_FIELD_NUMBER: _ClassVar[int]
    MATERIAL_TYPE_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    material_file_path: _table_basic_pb2.string_array
    material_priority: int
    material_type: int
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., material_file_path: _Optional[_Union[_table_basic_pb2.string_array, _Mapping]] = ..., material_priority: _Optional[int] = ..., material_type: _Optional[int] = ...) -> None: ...

class MaterialPriorityTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: MaterialPriorityTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[MaterialPriorityTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, MaterialPriorityTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, MaterialPriorityTableBase]] = ...) -> None: ...
