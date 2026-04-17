import enum_e_user_transfer_type_pb2 as _enum_e_user_transfer_type_pb2
import stru_position_param_pb2 as _stru_position_param_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TransferParam(_message.Message):
    __slots__ = ("scene_id", "transfer_type", "position_param", "change_flag", "is_server_switch", "visual_layer_config_id", "scene_guid", "connect_guid", "sub_scene_uuid", "is_revive")
    SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_TYPE_FIELD_NUMBER: _ClassVar[int]
    POSITION_PARAM_FIELD_NUMBER: _ClassVar[int]
    CHANGE_FLAG_FIELD_NUMBER: _ClassVar[int]
    IS_SERVER_SWITCH_FIELD_NUMBER: _ClassVar[int]
    VISUAL_LAYER_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    SCENE_GUID_FIELD_NUMBER: _ClassVar[int]
    CONNECT_GUID_FIELD_NUMBER: _ClassVar[int]
    SUB_SCENE_UUID_FIELD_NUMBER: _ClassVar[int]
    IS_REVIVE_FIELD_NUMBER: _ClassVar[int]
    scene_id: int
    transfer_type: _enum_e_user_transfer_type_pb2.EUserTransferType
    position_param: _stru_position_param_pb2.PositionParam
    change_flag: int
    is_server_switch: bool
    visual_layer_config_id: int
    scene_guid: str
    connect_guid: str
    sub_scene_uuid: int
    is_revive: bool
    def __init__(self, scene_id: _Optional[int] = ..., transfer_type: _Optional[_Union[_enum_e_user_transfer_type_pb2.EUserTransferType, str]] = ..., position_param: _Optional[_Union[_stru_position_param_pb2.PositionParam, _Mapping]] = ..., change_flag: _Optional[int] = ..., is_server_switch: bool = ..., visual_layer_config_id: _Optional[int] = ..., scene_guid: _Optional[str] = ..., connect_guid: _Optional[str] = ..., sub_scene_uuid: _Optional[int] = ..., is_revive: bool = ...) -> None: ...
