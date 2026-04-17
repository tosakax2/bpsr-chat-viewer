import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_scene_line_data_pb2 as _stru_scene_line_data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReqSceneLineInfoReply(_message.Message):
    __slots__ = ("line_infos", "err_code")
    LINE_INFOS_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    line_infos: _containers.RepeatedCompositeFieldContainer[_stru_scene_line_data_pb2.SceneLineData]
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, line_infos: _Optional[_Iterable[_Union[_stru_scene_line_data_pb2.SceneLineData, _Mapping]]] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
