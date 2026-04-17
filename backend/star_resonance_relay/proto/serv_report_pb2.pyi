import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_report_upload_request_pb2 as _stru_report_upload_request_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Report(_message.Message):
    __slots__ = ()
    class ReportUpload_Ret(_message.Message):
        __slots__ = ("ret",)
        RET_FIELD_NUMBER: _ClassVar[int]
        ret: _enum_e_error_code_pb2.EErrorCode
        def __init__(self, ret: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
    class ReportUpload(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_report_upload_request_pb2.ReportUploadRequest
        def __init__(self, v_request: _Optional[_Union[_stru_report_upload_request_pb2.ReportUploadRequest, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...
