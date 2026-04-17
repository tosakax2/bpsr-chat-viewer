import enum_e_assign_scene_source_type_pb2 as _enum_e_assign_scene_source_type_pb2
import stru_enter_scene_params_pb2 as _stru_enter_scene_params_pb2
import enum_e_scene_assign_type_pb2 as _enum_e_scene_assign_type_pb2
import stru_login_scene_params_pb2 as _stru_login_scene_params_pb2
import stru_scene_init_params_pb2 as _stru_scene_init_params_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AssignSceneParams(_message.Message):
    __slots__ = ("scene_id", "creator_char_id", "assign_type", "init_param", "enter_param", "login_param", "source_type")
    SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    CREATOR_CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    ASSIGN_TYPE_FIELD_NUMBER: _ClassVar[int]
    INIT_PARAM_FIELD_NUMBER: _ClassVar[int]
    ENTER_PARAM_FIELD_NUMBER: _ClassVar[int]
    LOGIN_PARAM_FIELD_NUMBER: _ClassVar[int]
    SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    scene_id: int
    creator_char_id: int
    assign_type: _enum_e_scene_assign_type_pb2.ESceneAssignType
    init_param: _stru_scene_init_params_pb2.SceneInitParams
    enter_param: _stru_enter_scene_params_pb2.EnterSceneParams
    login_param: _stru_login_scene_params_pb2.LoginSceneParams
    source_type: _enum_e_assign_scene_source_type_pb2.EAssignSceneSourceType
    def __init__(self, scene_id: _Optional[int] = ..., creator_char_id: _Optional[int] = ..., assign_type: _Optional[_Union[_enum_e_scene_assign_type_pb2.ESceneAssignType, str]] = ..., init_param: _Optional[_Union[_stru_scene_init_params_pb2.SceneInitParams, _Mapping]] = ..., enter_param: _Optional[_Union[_stru_enter_scene_params_pb2.EnterSceneParams, _Mapping]] = ..., login_param: _Optional[_Union[_stru_login_scene_params_pb2.LoginSceneParams, _Mapping]] = ..., source_type: _Optional[_Union[_enum_e_assign_scene_source_type_pb2.EAssignSceneSourceType, str]] = ...) -> None: ...
