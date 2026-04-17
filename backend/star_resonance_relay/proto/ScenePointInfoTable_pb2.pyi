import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ScenePointInfoTableBase(_message.Message):
    __slots__ = ("u_id", "group_id", "position", "rotation", "cam_position", "cam_rotation", "random_radius", "camera_id", "random_inner_radius")
    U_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    ROTATION_FIELD_NUMBER: _ClassVar[int]
    CAM_POSITION_FIELD_NUMBER: _ClassVar[int]
    CAM_ROTATION_FIELD_NUMBER: _ClassVar[int]
    RANDOM_RADIUS_FIELD_NUMBER: _ClassVar[int]
    CAMERA_ID_FIELD_NUMBER: _ClassVar[int]
    RANDOM_INNER_RADIUS_FIELD_NUMBER: _ClassVar[int]
    u_id: int
    group_id: int
    position: _table_basic_pb2.number_array
    rotation: float
    cam_position: _table_basic_pb2.number_array
    cam_rotation: float
    random_radius: float
    camera_id: int
    random_inner_radius: float
    def __init__(self, u_id: _Optional[int] = ..., group_id: _Optional[int] = ..., position: _Optional[_Union[_table_basic_pb2.number_array, _Mapping]] = ..., rotation: _Optional[float] = ..., cam_position: _Optional[_Union[_table_basic_pb2.number_array, _Mapping]] = ..., cam_rotation: _Optional[float] = ..., random_radius: _Optional[float] = ..., camera_id: _Optional[int] = ..., random_inner_radius: _Optional[float] = ...) -> None: ...

class ScenePointInfoTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ScenePointInfoTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ScenePointInfoTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, ScenePointInfoTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, ScenePointInfoTableBase]] = ...) -> None: ...
