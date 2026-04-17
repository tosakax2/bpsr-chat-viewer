from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class WarehouseData(_message.Message):
    __slots__ = ("warehouse_id",)
    WAREHOUSE_ID_FIELD_NUMBER: _ClassVar[int]
    warehouse_id: int
    def __init__(self, warehouse_id: _Optional[int] = ...) -> None: ...
