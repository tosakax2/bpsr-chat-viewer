import stru_show_piece_pair_pb2 as _stru_show_piece_pair_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ShowPieceAttr(_message.Message):
    __slots__ = ("piece_info", "begin_time", "end_time")
    PIECE_INFO_FIELD_NUMBER: _ClassVar[int]
    BEGIN_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    piece_info: _stru_show_piece_pair_pb2.ShowPiecePair
    begin_time: int
    end_time: int
    def __init__(self, piece_info: _Optional[_Union[_stru_show_piece_pair_pb2.ShowPiecePair, _Mapping]] = ..., begin_time: _Optional[int] = ..., end_time: _Optional[int] = ...) -> None: ...
