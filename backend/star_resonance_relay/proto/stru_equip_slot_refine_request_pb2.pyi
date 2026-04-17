import stru_equip_slot_refine_item_cost_pb2 as _stru_equip_slot_refine_item_cost_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EquipSlotRefineRequest(_message.Message):
    __slots__ = ("slot_id", "item_cost_list")
    SLOT_ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_COST_LIST_FIELD_NUMBER: _ClassVar[int]
    slot_id: int
    item_cost_list: _containers.RepeatedCompositeFieldContainer[_stru_equip_slot_refine_item_cost_pb2.EquipSlotRefineItemCost]
    def __init__(self, slot_id: _Optional[int] = ..., item_cost_list: _Optional[_Iterable[_Union[_stru_equip_slot_refine_item_cost_pb2.EquipSlotRefineItemCost, _Mapping]]] = ...) -> None: ...
