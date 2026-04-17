import stru_scene_data_pb2 as _stru_scene_data_pb2
import stru_transfer_info_pb2 as _stru_transfer_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SceneInfo(_message.Message):
    __slots__ = ("data", "server_id", "scene_id", "host", "changemap", "old_scene_id", "old_scene_sub_type", "scene_sub_type", "transfer_info")
    DATA_FIELD_NUMBER: _ClassVar[int]
    SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    HOST_FIELD_NUMBER: _ClassVar[int]
    CHANGEMAP_FIELD_NUMBER: _ClassVar[int]
    OLD_SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    OLD_SCENE_SUB_TYPE_FIELD_NUMBER: _ClassVar[int]
    SCENE_SUB_TYPE_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_INFO_FIELD_NUMBER: _ClassVar[int]
    data: _stru_scene_data_pb2.SceneData
    server_id: int
    scene_id: int
    host: str
    changemap: bool
    old_scene_id: int
    old_scene_sub_type: int
    scene_sub_type: int
    transfer_info: _stru_transfer_info_pb2.TransferInfo
    def __init__(self, data: _Optional[_Union[_stru_scene_data_pb2.SceneData, _Mapping]] = ..., server_id: _Optional[int] = ..., scene_id: _Optional[int] = ..., host: _Optional[str] = ..., changemap: bool = ..., old_scene_id: _Optional[int] = ..., old_scene_sub_type: _Optional[int] = ..., scene_sub_type: _Optional[int] = ..., transfer_info: _Optional[_Union[_stru_transfer_info_pb2.TransferInfo, _Mapping]] = ...) -> None: ...
