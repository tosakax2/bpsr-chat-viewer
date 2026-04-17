from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ActiveProfessionTalentRequest(_message.Message):
    __slots__ = ("profession_id", "talent_node_ids")
    PROFESSION_ID_FIELD_NUMBER: _ClassVar[int]
    TALENT_NODE_IDS_FIELD_NUMBER: _ClassVar[int]
    profession_id: int
    talent_node_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, profession_id: _Optional[int] = ..., talent_node_ids: _Optional[_Iterable[int]] = ...) -> None: ...
