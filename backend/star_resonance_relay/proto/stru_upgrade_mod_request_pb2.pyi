from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UpgradeModRequest(_message.Message):
    __slots__ = ("mod_uuid", "part_effect_config_id")
    MOD_UUID_FIELD_NUMBER: _ClassVar[int]
    PART_EFFECT_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    mod_uuid: int
    part_effect_config_id: int
    def __init__(self, mod_uuid: _Optional[int] = ..., part_effect_config_id: _Optional[int] = ...) -> None: ...
