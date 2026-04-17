import stru_gasha_record_item_info_pb2 as _stru_gasha_record_item_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GashaRecord(_message.Message):
    __slots__ = ("char_id_pool", "pool_id", "gasha_record_info", "first_timestamp")
    CHAR_ID_POOL_FIELD_NUMBER: _ClassVar[int]
    POOL_ID_FIELD_NUMBER: _ClassVar[int]
    GASHA_RECORD_INFO_FIELD_NUMBER: _ClassVar[int]
    FIRST_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    char_id_pool: str
    pool_id: int
    gasha_record_info: _containers.RepeatedCompositeFieldContainer[_stru_gasha_record_item_info_pb2.GashaRecordItemInfo]
    first_timestamp: int
    def __init__(self, char_id_pool: _Optional[str] = ..., pool_id: _Optional[int] = ..., gasha_record_info: _Optional[_Iterable[_Union[_stru_gasha_record_item_info_pb2.GashaRecordItemInfo, _Mapping]]] = ..., first_timestamp: _Optional[int] = ...) -> None: ...
