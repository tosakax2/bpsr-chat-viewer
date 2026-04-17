import stru_show_piece_id_list_pb2 as _stru_show_piece_id_list_pb2
import stru_show_piece_pair_pb2 as _stru_show_piece_pair_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ShowPieceData(_message.Message):
    __slots__ = ("often_use_type_list", "unlock_type_list", "roulette_pos_piece_info")
    class OftenUseTypeListEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_show_piece_id_list_pb2.ShowPieceIdList
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_show_piece_id_list_pb2.ShowPieceIdList, _Mapping]] = ...) -> None: ...
    class UnlockTypeListEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_show_piece_id_list_pb2.ShowPieceIdList
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_show_piece_id_list_pb2.ShowPieceIdList, _Mapping]] = ...) -> None: ...
    class RoulettePosPieceInfoEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_show_piece_pair_pb2.ShowPiecePair
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_show_piece_pair_pb2.ShowPiecePair, _Mapping]] = ...) -> None: ...
    OFTEN_USE_TYPE_LIST_FIELD_NUMBER: _ClassVar[int]
    UNLOCK_TYPE_LIST_FIELD_NUMBER: _ClassVar[int]
    ROULETTE_POS_PIECE_INFO_FIELD_NUMBER: _ClassVar[int]
    often_use_type_list: _containers.MessageMap[int, _stru_show_piece_id_list_pb2.ShowPieceIdList]
    unlock_type_list: _containers.MessageMap[int, _stru_show_piece_id_list_pb2.ShowPieceIdList]
    roulette_pos_piece_info: _containers.MessageMap[int, _stru_show_piece_pair_pb2.ShowPiecePair]
    def __init__(self, often_use_type_list: _Optional[_Mapping[int, _stru_show_piece_id_list_pb2.ShowPieceIdList]] = ..., unlock_type_list: _Optional[_Mapping[int, _stru_show_piece_id_list_pb2.ShowPieceIdList]] = ..., roulette_pos_piece_info: _Optional[_Mapping[int, _stru_show_piece_pair_pb2.ShowPiecePair]] = ...) -> None: ...
