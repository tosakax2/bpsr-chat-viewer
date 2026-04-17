import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_structure_op_pb2 as _stru_structure_op_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommunityUpdateStructureReplyOpt(_message.Message):
    __slots__ = ("err_code", "structure_op")
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    STRUCTURE_OP_FIELD_NUMBER: _ClassVar[int]
    err_code: _enum_e_error_code_pb2.EErrorCode
    structure_op: _stru_structure_op_pb2.StructureOp
    def __init__(self, err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ..., structure_op: _Optional[_Union[_stru_structure_op_pb2.StructureOp, _Mapping]] = ...) -> None: ...
