import stru_community_warehouse_grid_pb2 as _stru_community_warehouse_grid_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyHomelandWarehouseGridChangeRequest(_message.Message):
    __slots__ = ("item_infos",)
    ITEM_INFOS_FIELD_NUMBER: _ClassVar[int]
    item_infos: _containers.RepeatedCompositeFieldContainer[_stru_community_warehouse_grid_pb2.CommunityWarehouseGrid]
    def __init__(self, item_infos: _Optional[_Iterable[_Union[_stru_community_warehouse_grid_pb2.CommunityWarehouseGrid, _Mapping]]] = ...) -> None: ...
