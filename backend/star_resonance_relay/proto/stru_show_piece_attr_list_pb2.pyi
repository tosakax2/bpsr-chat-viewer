import stru_show_piece_attr_pb2 as _stru_show_piece_attr_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ShowPieceAttrList(_message.Message):
    __slots__ = ("show_piece_attrs",)
    SHOW_PIECE_ATTRS_FIELD_NUMBER: _ClassVar[int]
    show_piece_attrs: _containers.RepeatedCompositeFieldContainer[_stru_show_piece_attr_pb2.ShowPieceAttr]
    def __init__(self, show_piece_attrs: _Optional[_Iterable[_Union[_stru_show_piece_attr_pb2.ShowPieceAttr, _Mapping]]] = ...) -> None: ...
