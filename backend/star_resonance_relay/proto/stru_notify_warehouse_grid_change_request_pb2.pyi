import stru_warehouse_grid_pb2 as _stru_warehouse_grid_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyWarehouseGridChangeRequest(_message.Message):
    __slots__ = ("warehouse_grid", "take_out_char_id", "deposit_char_id")
    WAREHOUSE_GRID_FIELD_NUMBER: _ClassVar[int]
    TAKE_OUT_CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    DEPOSIT_CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    warehouse_grid: _stru_warehouse_grid_pb2.WarehouseGrid
    take_out_char_id: int
    deposit_char_id: int
    def __init__(self, warehouse_grid: _Optional[_Union[_stru_warehouse_grid_pb2.WarehouseGrid, _Mapping]] = ..., take_out_char_id: _Optional[int] = ..., deposit_char_id: _Optional[int] = ...) -> None: ...
