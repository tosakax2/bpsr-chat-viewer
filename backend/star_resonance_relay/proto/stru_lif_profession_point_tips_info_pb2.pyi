import enum_e_item_get_opt_src_pb2 as _enum_e_item_get_opt_src_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LifProfessionPointTipsInfo(_message.Message):
    __slots__ = ("get_life_point_type", "life_profession_id", "point_count")
    GET_LIFE_POINT_TYPE_FIELD_NUMBER: _ClassVar[int]
    LIFE_PROFESSION_ID_FIELD_NUMBER: _ClassVar[int]
    POINT_COUNT_FIELD_NUMBER: _ClassVar[int]
    get_life_point_type: _enum_e_item_get_opt_src_pb2.EItemGetOptSrc
    life_profession_id: int
    point_count: int
    def __init__(self, get_life_point_type: _Optional[_Union[_enum_e_item_get_opt_src_pb2.EItemGetOptSrc, str]] = ..., life_profession_id: _Optional[int] = ..., point_count: _Optional[int] = ...) -> None: ...
