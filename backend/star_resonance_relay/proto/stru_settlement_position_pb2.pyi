import stru_position_pb2 as _stru_position_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SettlementPosition(_message.Message):
    __slots__ = ("pos", "rotate")
    POS_FIELD_NUMBER: _ClassVar[int]
    ROTATE_FIELD_NUMBER: _ClassVar[int]
    pos: _stru_position_pb2.Position
    rotate: _stru_position_pb2.Position
    def __init__(self, pos: _Optional[_Union[_stru_position_pb2.Position, _Mapping]] = ..., rotate: _Optional[_Union[_stru_position_pb2.Position, _Mapping]] = ...) -> None: ...
