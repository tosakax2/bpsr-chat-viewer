import stru_warehouse_grid_pb2 as _stru_warehouse_grid_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WarehouseInfo(_message.Message):
    __slots__ = ("warehouse_id", "president_id", "mem_id_list", "warehouse_grids")
    WAREHOUSE_ID_FIELD_NUMBER: _ClassVar[int]
    PRESIDENT_ID_FIELD_NUMBER: _ClassVar[int]
    MEM_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_GRIDS_FIELD_NUMBER: _ClassVar[int]
    warehouse_id: int
    president_id: int
    mem_id_list: _containers.RepeatedScalarFieldContainer[int]
    warehouse_grids: _containers.RepeatedCompositeFieldContainer[_stru_warehouse_grid_pb2.WarehouseGrid]
    def __init__(self, warehouse_id: _Optional[int] = ..., president_id: _Optional[int] = ..., mem_id_list: _Optional[_Iterable[int]] = ..., warehouse_grids: _Optional[_Iterable[_Union[_stru_warehouse_grid_pb2.WarehouseGrid, _Mapping]]] = ...) -> None: ...
