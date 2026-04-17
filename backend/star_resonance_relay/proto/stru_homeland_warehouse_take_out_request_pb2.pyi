from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HomelandWarehouseTakeOutRequest(_message.Message):
    __slots__ = ("grid_pos", "item_cfg_id", "item_num", "owner_char_id")
    GRID_POS_FIELD_NUMBER: _ClassVar[int]
    ITEM_CFG_ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_NUM_FIELD_NUMBER: _ClassVar[int]
    OWNER_CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    grid_pos: int
    item_cfg_id: int
    item_num: int
    owner_char_id: int
    def __init__(self, grid_pos: _Optional[int] = ..., item_cfg_id: _Optional[int] = ..., item_num: _Optional[int] = ..., owner_char_id: _Optional[int] = ...) -> None: ...
