import enum_e_equip_enchant_type_pb2 as _enum_e_equip_enchant_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EquipEnchantRequest(_message.Message):
    __slots__ = ("equip_uuid", "enchant_item_config_id", "enchant_type")
    EQUIP_UUID_FIELD_NUMBER: _ClassVar[int]
    ENCHANT_ITEM_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    ENCHANT_TYPE_FIELD_NUMBER: _ClassVar[int]
    equip_uuid: int
    enchant_item_config_id: int
    enchant_type: _enum_e_equip_enchant_type_pb2.EEquipEnchantType
    def __init__(self, equip_uuid: _Optional[int] = ..., enchant_item_config_id: _Optional[int] = ..., enchant_type: _Optional[_Union[_enum_e_equip_enchant_type_pb2.EEquipEnchantType, str]] = ...) -> None: ...
