import stru_union_base_data_pb2 as _stru_union_base_data_pb2
import stru_user_summary_data_pb2 as _stru_user_summary_data_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UnionListData(_message.Message):
    __slots__ = ("base_info", "is_req", "president_info", "auto_pass")
    BASE_INFO_FIELD_NUMBER: _ClassVar[int]
    IS_REQ_FIELD_NUMBER: _ClassVar[int]
    PRESIDENT_INFO_FIELD_NUMBER: _ClassVar[int]
    AUTO_PASS_FIELD_NUMBER: _ClassVar[int]
    base_info: _stru_union_base_data_pb2.UnionBaseData
    is_req: bool
    president_info: _stru_user_summary_data_pb2.UserSummaryData
    auto_pass: bool
    def __init__(self, base_info: _Optional[_Union[_stru_union_base_data_pb2.UnionBaseData, _Mapping]] = ..., is_req: bool = ..., president_info: _Optional[_Union[_stru_user_summary_data_pb2.UserSummaryData, _Mapping]] = ..., auto_pass: bool = ...) -> None: ...
