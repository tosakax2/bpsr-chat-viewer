from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RecastEquipRequest(_message.Message):
    __slots__ = ("uuid", "consume_uuid", "item_config_id")
    UUID_FIELD_NUMBER: _ClassVar[int]
    CONSUME_UUID_FIELD_NUMBER: _ClassVar[int]
    ITEM_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    uuid: int
    consume_uuid: _containers.RepeatedScalarFieldContainer[int]
    item_config_id: int
    def __init__(self, uuid: _Optional[int] = ..., consume_uuid: _Optional[_Iterable[int]] = ..., item_config_id: _Optional[int] = ...) -> None: ...
