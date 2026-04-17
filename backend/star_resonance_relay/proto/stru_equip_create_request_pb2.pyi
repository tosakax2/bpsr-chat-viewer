from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class EquipCreateRequest(_message.Message):
    __slots__ = ("equip_config_id", "consume_equip_uuid", "function_id")
    EQUIP_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    CONSUME_EQUIP_UUID_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_ID_FIELD_NUMBER: _ClassVar[int]
    equip_config_id: int
    consume_equip_uuid: int
    function_id: int
    def __init__(self, equip_config_id: _Optional[int] = ..., consume_equip_uuid: _Optional[int] = ..., function_id: _Optional[int] = ...) -> None: ...
