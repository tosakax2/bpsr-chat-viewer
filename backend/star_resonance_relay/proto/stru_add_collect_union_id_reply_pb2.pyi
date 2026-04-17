import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_union_list_data_pb2 as _stru_union_list_data_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AddCollectUnionIdReply(_message.Message):
    __slots__ = ("brief_union_ifo", "err_code")
    BRIEF_UNION_IFO_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    brief_union_ifo: _stru_union_list_data_pb2.UnionListData
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, brief_union_ifo: _Optional[_Union[_stru_union_list_data_pb2.UnionListData, _Mapping]] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
