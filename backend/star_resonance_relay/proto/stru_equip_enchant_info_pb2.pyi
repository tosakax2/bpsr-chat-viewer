import enum_e_equip_enchant_type_pb2 as _enum_e_equip_enchant_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EquipEnchantInfo(_message.Message):
    __slots__ = ("enchant_item_type_id", "enchant_level", "enchant_type")
    ENCHANT_ITEM_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    ENCHANT_LEVEL_FIELD_NUMBER: _ClassVar[int]
    ENCHANT_TYPE_FIELD_NUMBER: _ClassVar[int]
    enchant_item_type_id: int
    enchant_level: int
    enchant_type: _enum_e_equip_enchant_type_pb2.EEquipEnchantType
    def __init__(self, enchant_item_type_id: _Optional[int] = ..., enchant_level: _Optional[int] = ..., enchant_type: _Optional[_Union[_enum_e_equip_enchant_type_pb2.EEquipEnchantType, str]] = ...) -> None: ...
