import stru_structure_op_pb2 as _stru_structure_op_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateStructureRequest(_message.Message):
    __slots__ = ("home_id", "ops")
    HOME_ID_FIELD_NUMBER: _ClassVar[int]
    OPS_FIELD_NUMBER: _ClassVar[int]
    home_id: int
    ops: _containers.RepeatedCompositeFieldContainer[_stru_structure_op_pb2.StructureOp]
    def __init__(self, home_id: _Optional[int] = ..., ops: _Optional[_Iterable[_Union[_stru_structure_op_pb2.StructureOp, _Mapping]]] = ...) -> None: ...
