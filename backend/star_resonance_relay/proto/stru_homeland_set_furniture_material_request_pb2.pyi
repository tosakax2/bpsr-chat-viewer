from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HomelandSetFurnitureMaterialRequest(_message.Message):
    __slots__ = ("structure_uuid", "material_id", "is_outer")
    STRUCTURE_UUID_FIELD_NUMBER: _ClassVar[int]
    MATERIAL_ID_FIELD_NUMBER: _ClassVar[int]
    IS_OUTER_FIELD_NUMBER: _ClassVar[int]
    structure_uuid: int
    material_id: int
    is_outer: bool
    def __init__(self, structure_uuid: _Optional[int] = ..., material_id: _Optional[int] = ..., is_outer: bool = ...) -> None: ...
