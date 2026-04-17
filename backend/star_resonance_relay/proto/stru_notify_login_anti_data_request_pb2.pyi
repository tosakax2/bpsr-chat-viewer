import stru_tss_account_info_proto_pb2 as _stru_tss_account_info_proto_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyLoginAntiDataRequest(_message.Message):
    __slots__ = ("tss_info",)
    TSS_INFO_FIELD_NUMBER: _ClassVar[int]
    tss_info: _stru_tss_account_info_proto_pb2.TssAccountInfoProto
    def __init__(self, tss_info: _Optional[_Union[_stru_tss_account_info_proto_pb2.TssAccountInfoProto, _Mapping]] = ...) -> None: ...
