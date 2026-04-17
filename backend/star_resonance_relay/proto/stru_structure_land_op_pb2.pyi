import enum_structure_op_type_pb2 as _enum_structure_op_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StructureLandOp(_message.Message):
    __slots__ = ("op_type", "uuid")
    OP_TYPE_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    op_type: _enum_structure_op_type_pb2.StructureOpType
    uuid: int
    def __init__(self, op_type: _Optional[_Union[_enum_structure_op_type_pb2.StructureOpType, str]] = ..., uuid: _Optional[int] = ...) -> None: ...
