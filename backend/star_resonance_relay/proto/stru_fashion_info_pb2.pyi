import stru_fashion_color_info_pb2 as _stru_fashion_color_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FashionInfo(_message.Message):
    __slots__ = ("slot", "fashion_id", "colors")
    SLOT_FIELD_NUMBER: _ClassVar[int]
    FASHION_ID_FIELD_NUMBER: _ClassVar[int]
    COLORS_FIELD_NUMBER: _ClassVar[int]
    slot: int
    fashion_id: int
    colors: _stru_fashion_color_info_pb2.FashionColorInfo
    def __init__(self, slot: _Optional[int] = ..., fashion_id: _Optional[int] = ..., colors: _Optional[_Union[_stru_fashion_color_info_pb2.FashionColorInfo, _Mapping]] = ...) -> None: ...
