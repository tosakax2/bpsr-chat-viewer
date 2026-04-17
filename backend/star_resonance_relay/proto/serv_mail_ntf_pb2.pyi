import stru_sync_mail_info_request_pb2 as _stru_sync_mail_info_request_pb2
import stru_sync_mail_list_num_request_pb2 as _stru_sync_mail_list_num_request_pb2
import stru_sync_new_mail_request_pb2 as _stru_sync_new_mail_request_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MailNtf(_message.Message):
    __slots__ = ()
    class SyncMailInfo(_message.Message):
        __slots__ = ("request",)
        REQUEST_FIELD_NUMBER: _ClassVar[int]
        request: _stru_sync_mail_info_request_pb2.SyncMailInfoRequest
        def __init__(self, request: _Optional[_Union[_stru_sync_mail_info_request_pb2.SyncMailInfoRequest, _Mapping]] = ...) -> None: ...
    class SyncMailListNum(_message.Message):
        __slots__ = ("request",)
        REQUEST_FIELD_NUMBER: _ClassVar[int]
        request: _stru_sync_mail_list_num_request_pb2.SyncMailListNumRequest
        def __init__(self, request: _Optional[_Union[_stru_sync_mail_list_num_request_pb2.SyncMailListNumRequest, _Mapping]] = ...) -> None: ...
    class SyncNewMail(_message.Message):
        __slots__ = ("request",)
        REQUEST_FIELD_NUMBER: _ClassVar[int]
        request: _stru_sync_new_mail_request_pb2.SyncNewMailRequest
        def __init__(self, request: _Optional[_Union[_stru_sync_new_mail_request_pb2.SyncNewMailRequest, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...
