import stru_transfer_param_pb2 as _stru_transfer_param_pb2
import stru_scene_line_data_pb2 as _stru_scene_line_data_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyEnterWorldRequest(_message.Message):
    __slots__ = ("AccountId", "Token", "SceneIp", "ScenePort", "Transform", "SceneLineData")
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    SCENEIP_FIELD_NUMBER: _ClassVar[int]
    SCENEPORT_FIELD_NUMBER: _ClassVar[int]
    TRANSFORM_FIELD_NUMBER: _ClassVar[int]
    SCENELINEDATA_FIELD_NUMBER: _ClassVar[int]
    AccountId: str
    Token: str
    SceneIp: str
    ScenePort: int
    Transform: _stru_transfer_param_pb2.TransferParam
    SceneLineData: _stru_scene_line_data_pb2.SceneLineData
    def __init__(self, AccountId: _Optional[str] = ..., Token: _Optional[str] = ..., SceneIp: _Optional[str] = ..., ScenePort: _Optional[int] = ..., Transform: _Optional[_Union[_stru_transfer_param_pb2.TransferParam, _Mapping]] = ..., SceneLineData: _Optional[_Union[_stru_scene_line_data_pb2.SceneLineData, _Mapping]] = ...) -> None: ...
