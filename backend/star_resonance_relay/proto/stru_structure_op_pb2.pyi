import stru_structure_pb2 as _stru_structure_pb2
import enum_structure_op_type_pb2 as _enum_structure_op_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StructureOp(_message.Message):
    __slots__ = ("op_type", "structure")
    OP_TYPE_FIELD_NUMBER: _ClassVar[int]
    STRUCTURE_FIELD_NUMBER: _ClassVar[int]
    op_type: _enum_structure_op_type_pb2.StructureOpType
    structure: _stru_structure_pb2.Structure
    def __init__(self, op_type: _Optional[_Union[_enum_structure_op_type_pb2.StructureOpType, str]] = ..., structure: _Optional[_Union[_stru_structure_pb2.Structure, _Mapping]] = ...) -> None: ...
