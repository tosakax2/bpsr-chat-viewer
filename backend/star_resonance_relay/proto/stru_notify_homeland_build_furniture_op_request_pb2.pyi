import stru_notify_build_furniture_op_pb2 as _stru_notify_build_furniture_op_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyHomelandBuildFurnitureOpRequest(_message.Message):
    __slots__ = ("community_id", "homeland_id", "is_outer", "scene_guid", "build_furniture_infos")
    COMMUNITY_ID_FIELD_NUMBER: _ClassVar[int]
    HOMELAND_ID_FIELD_NUMBER: _ClassVar[int]
    IS_OUTER_FIELD_NUMBER: _ClassVar[int]
    SCENE_GUID_FIELD_NUMBER: _ClassVar[int]
    BUILD_FURNITURE_INFOS_FIELD_NUMBER: _ClassVar[int]
    community_id: int
    homeland_id: int
    is_outer: bool
    scene_guid: str
    build_furniture_infos: _containers.RepeatedCompositeFieldContainer[_stru_notify_build_furniture_op_pb2.NotifyBuildFurnitureOp]
    def __init__(self, community_id: _Optional[int] = ..., homeland_id: _Optional[int] = ..., is_outer: bool = ..., scene_guid: _Optional[str] = ..., build_furniture_infos: _Optional[_Iterable[_Union[_stru_notify_build_furniture_op_pb2.NotifyBuildFurnitureOp, _Mapping]]] = ...) -> None: ...
