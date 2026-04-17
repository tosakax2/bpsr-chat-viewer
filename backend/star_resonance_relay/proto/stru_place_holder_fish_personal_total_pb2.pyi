from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PlaceHolderFishPersonalTotal(_message.Message):
    __slots__ = ("total", "myth_total", "sum_fish_type", "sum_sea_life_type", "sum_trash_type", "most_fish_id", "favour_zero", "user_name", "union_name", "is_newbie", "fish_lv", "is_backflow")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    MYTH_TOTAL_FIELD_NUMBER: _ClassVar[int]
    SUM_FISH_TYPE_FIELD_NUMBER: _ClassVar[int]
    SUM_SEA_LIFE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SUM_TRASH_TYPE_FIELD_NUMBER: _ClassVar[int]
    MOST_FISH_ID_FIELD_NUMBER: _ClassVar[int]
    FAVOUR_ZERO_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    UNION_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_NEWBIE_FIELD_NUMBER: _ClassVar[int]
    FISH_LV_FIELD_NUMBER: _ClassVar[int]
    IS_BACKFLOW_FIELD_NUMBER: _ClassVar[int]
    total: int
    myth_total: int
    sum_fish_type: int
    sum_sea_life_type: int
    sum_trash_type: int
    most_fish_id: int
    favour_zero: int
    user_name: str
    union_name: str
    is_newbie: bool
    fish_lv: int
    is_backflow: bool
    def __init__(self, total: _Optional[int] = ..., myth_total: _Optional[int] = ..., sum_fish_type: _Optional[int] = ..., sum_sea_life_type: _Optional[int] = ..., sum_trash_type: _Optional[int] = ..., most_fish_id: _Optional[int] = ..., favour_zero: _Optional[int] = ..., user_name: _Optional[str] = ..., union_name: _Optional[str] = ..., is_newbie: bool = ..., fish_lv: _Optional[int] = ..., is_backflow: bool = ...) -> None: ...
