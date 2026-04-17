import stru_transfer_param_pb2 as _stru_transfer_param_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EnterSceneParams(_message.Message):
    __slots__ = ("change_scene_type", "scene_id", "scene_guid", "transfer_param", "enter_scene_params")
    CHANGE_SCENE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    SCENE_GUID_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_PARAM_FIELD_NUMBER: _ClassVar[int]
    ENTER_SCENE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    change_scene_type: int
    scene_id: int
    scene_guid: str
    transfer_param: _stru_transfer_param_pb2.TransferParam
    enter_scene_params: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    def __init__(self, change_scene_type: _Optional[int] = ..., scene_id: _Optional[int] = ..., scene_guid: _Optional[str] = ..., transfer_param: _Optional[_Union[_stru_transfer_param_pb2.TransferParam, _Mapping]] = ..., enter_scene_params: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ...) -> None: ...
