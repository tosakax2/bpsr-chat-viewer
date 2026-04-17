import stru_server_state_object_interaction_param_pb2 as _stru_server_state_object_interaction_param_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ScenePersonalObject(_message.Message):
    __slots__ = ("personal_obj_data",)
    class PersonalObjDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_server_state_object_interaction_param_pb2.ServerStateObjectInteractionParam
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_server_state_object_interaction_param_pb2.ServerStateObjectInteractionParam, _Mapping]] = ...) -> None: ...
    PERSONAL_OBJ_DATA_FIELD_NUMBER: _ClassVar[int]
    personal_obj_data: _containers.MessageMap[int, _stru_server_state_object_interaction_param_pb2.ServerStateObjectInteractionParam]
    def __init__(self, personal_obj_data: _Optional[_Mapping[int, _stru_server_state_object_interaction_param_pb2.ServerStateObjectInteractionParam]] = ...) -> None: ...
