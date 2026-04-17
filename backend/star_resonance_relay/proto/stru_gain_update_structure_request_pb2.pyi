import stru_structure_land_op_pb2 as _stru_structure_land_op_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GainUpdateStructureRequest(_message.Message):
    __slots__ = ("home_id", "op")
    HOME_ID_FIELD_NUMBER: _ClassVar[int]
    OP_FIELD_NUMBER: _ClassVar[int]
    home_id: int
    op: _stru_structure_land_op_pb2.StructureLandOp
    def __init__(self, home_id: _Optional[int] = ..., op: _Optional[_Union[_stru_structure_land_op_pb2.StructureLandOp, _Mapping]] = ...) -> None: ...
