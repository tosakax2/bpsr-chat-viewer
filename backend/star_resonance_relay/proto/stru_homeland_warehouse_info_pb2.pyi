import stru_community_warehouse_grid_pb2 as _stru_community_warehouse_grid_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HomelandWarehouseInfo(_message.Message):
    __slots__ = ("warehouse_grids",)
    class WarehouseGridsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_community_warehouse_grid_pb2.CommunityWarehouseGrid
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_community_warehouse_grid_pb2.CommunityWarehouseGrid, _Mapping]] = ...) -> None: ...
    WAREHOUSE_GRIDS_FIELD_NUMBER: _ClassVar[int]
    warehouse_grids: _containers.MessageMap[int, _stru_community_warehouse_grid_pb2.CommunityWarehouseGrid]
    def __init__(self, warehouse_grids: _Optional[_Mapping[int, _stru_community_warehouse_grid_pb2.CommunityWarehouseGrid]] = ...) -> None: ...
