import enum_e_show_piece_type_pb2 as _enum_e_show_piece_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ShowPiecePair(_message.Message):
    __slots__ = ("piece_type", "piece_id")
    PIECE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PIECE_ID_FIELD_NUMBER: _ClassVar[int]
    piece_type: _enum_e_show_piece_type_pb2.EShowPieceType
    piece_id: int
    def __init__(self, piece_type: _Optional[_Union[_enum_e_show_piece_type_pb2.EShowPieceType, str]] = ..., piece_id: _Optional[int] = ...) -> None: ...
