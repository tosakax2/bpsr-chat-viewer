import stru_editor_u_i_position_pb2 as _stru_editor_u_i_position_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetPersonalZoneUIPositionRequest(_message.Message):
    __slots__ = ("ui_position",)
    UI_POSITION_FIELD_NUMBER: _ClassVar[int]
    ui_position: _containers.RepeatedCompositeFieldContainer[_stru_editor_u_i_position_pb2.EditorUIPosition]
    def __init__(self, ui_position: _Optional[_Iterable[_Union[_stru_editor_u_i_position_pb2.EditorUIPosition, _Mapping]]] = ...) -> None: ...
