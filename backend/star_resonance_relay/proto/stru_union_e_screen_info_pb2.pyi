import stru_photo_graph_show_pb2 as _stru_photo_graph_show_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UnionEScreenInfo(_message.Message):
    __slots__ = ("e_screen_id", "photo_graphs")
    E_SCREEN_ID_FIELD_NUMBER: _ClassVar[int]
    PHOTO_GRAPHS_FIELD_NUMBER: _ClassVar[int]
    e_screen_id: int
    photo_graphs: _containers.RepeatedCompositeFieldContainer[_stru_photo_graph_show_pb2.PhotoGraphShow]
    def __init__(self, e_screen_id: _Optional[int] = ..., photo_graphs: _Optional[_Iterable[_Union[_stru_photo_graph_show_pb2.PhotoGraphShow, _Mapping]]] = ...) -> None: ...
