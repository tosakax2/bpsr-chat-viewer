import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VoxelExportTableBase(_message.Message):
    __slots__ = ("id", "name", "scene_file_path", "cube_position", "collider_size", "has_terrain", "terrain_file_path")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SCENE_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    CUBE_POSITION_FIELD_NUMBER: _ClassVar[int]
    COLLIDER_SIZE_FIELD_NUMBER: _ClassVar[int]
    HAS_TERRAIN_FIELD_NUMBER: _ClassVar[int]
    TERRAIN_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    scene_file_path: str
    cube_position: _table_basic_pb2.number_array
    collider_size: _table_basic_pb2.number_array
    has_terrain: bool
    terrain_file_path: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., scene_file_path: _Optional[str] = ..., cube_position: _Optional[_Union[_table_basic_pb2.number_array, _Mapping]] = ..., collider_size: _Optional[_Union[_table_basic_pb2.number_array, _Mapping]] = ..., has_terrain: bool = ..., terrain_file_path: _Optional[str] = ...) -> None: ...

class VoxelExportTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: VoxelExportTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[VoxelExportTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, VoxelExportTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, VoxelExportTableBase]] = ...) -> None: ...
