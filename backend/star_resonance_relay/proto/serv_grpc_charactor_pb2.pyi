import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_cancel_delete_char_reply_pb2 as _stru_cancel_delete_char_reply_pb2
import stru_cancel_delete_char_request_pb2 as _stru_cancel_delete_char_request_pb2
import stru_create_char_reply_pb2 as _stru_create_char_reply_pb2
import stru_create_char_request_pb2 as _stru_create_char_request_pb2
import stru_delete_char_reply_pb2 as _stru_delete_char_reply_pb2
import stru_delete_char_request_pb2 as _stru_delete_char_request_pb2
import stru_exit_game_request_pb2 as _stru_exit_game_request_pb2
import stru_get_face_data_url_reply_pb2 as _stru_get_face_data_url_reply_pb2
import stru_get_face_data_url_request_pb2 as _stru_get_face_data_url_request_pb2
import stru_get_face_up_token_request_pb2 as _stru_get_face_up_token_request_pb2
import stru_get_face_upload_data_reply_pb2 as _stru_get_face_upload_data_reply_pb2
import stru_get_face_upload_data_request_pb2 as _stru_get_face_upload_data_request_pb2
import stru_login_reply_pb2 as _stru_login_reply_pb2
import stru_login_request_pb2 as _stru_login_request_pb2
import stru_privilege_activate_reply_pb2 as _stru_privilege_activate_reply_pb2
import stru_privilege_activate_request_pb2 as _stru_privilege_activate_request_pb2
import stru_reconnect_reply_pb2 as _stru_reconnect_reply_pb2
import stru_reconnect_request_pb2 as _stru_reconnect_request_pb2
import stru_report_m_sdk_request_pb2 as _stru_report_m_sdk_request_pb2
import stru_select_char_reply_pb2 as _stru_select_char_reply_pb2
import stru_select_char_request_pb2 as _stru_select_char_request_pb2
import stru_sync_language_request_pb2 as _stru_sync_language_request_pb2
import stru_take_award_by_cd_key_request_pb2 as _stru_take_award_by_cd_key_request_pb2
import stru_upload_face_success_request_pb2 as _stru_upload_face_success_request_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GrpcCharactor(_message.Message):
    __slots__ = ()
    class Login_Ret(_message.Message):
        __slots__ = ("ret",)
        RET_FIELD_NUMBER: _ClassVar[int]
        ret: _stru_login_reply_pb2.LoginReply
        def __init__(self, ret: _Optional[_Union[_stru_login_reply_pb2.LoginReply, _Mapping]] = ...) -> None: ...
    class Login(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_login_request_pb2.LoginRequest
        def __init__(self, v_request: _Optional[_Union[_stru_login_request_pb2.LoginRequest, _Mapping]] = ...) -> None: ...
    class CreateChar_Ret(_message.Message):
        __slots__ = ("ret",)
        RET_FIELD_NUMBER: _ClassVar[int]
        ret: _stru_create_char_reply_pb2.CreateCharReply
        def __init__(self, ret: _Optional[_Union[_stru_create_char_reply_pb2.CreateCharReply, _Mapping]] = ...) -> None: ...
    class CreateChar(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_create_char_request_pb2.CreateCharRequest
        def __init__(self, v_request: _Optional[_Union[_stru_create_char_request_pb2.CreateCharRequest, _Mapping]] = ...) -> None: ...
    class SelectChar_Ret(_message.Message):
        __slots__ = ("ret",)
        RET_FIELD_NUMBER: _ClassVar[int]
        ret: _stru_select_char_reply_pb2.SelectCharReply
        def __init__(self, ret: _Optional[_Union[_stru_select_char_reply_pb2.SelectCharReply, _Mapping]] = ...) -> None: ...
    class SelectChar(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_select_char_request_pb2.SelectCharRequest
        def __init__(self, v_request: _Optional[_Union[_stru_select_char_request_pb2.SelectCharRequest, _Mapping]] = ...) -> None: ...
    class DeleteChar_Ret(_message.Message):
        __slots__ = ("ret",)
        RET_FIELD_NUMBER: _ClassVar[int]
        ret: _stru_delete_char_reply_pb2.DeleteCharReply
        def __init__(self, ret: _Optional[_Union[_stru_delete_char_reply_pb2.DeleteCharReply, _Mapping]] = ...) -> None: ...
    class DeleteChar(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_delete_char_request_pb2.DeleteCharRequest
        def __init__(self, v_request: _Optional[_Union[_stru_delete_char_request_pb2.DeleteCharRequest, _Mapping]] = ...) -> None: ...
    class Reconnect_Ret(_message.Message):
        __slots__ = ("ret",)
        RET_FIELD_NUMBER: _ClassVar[int]
        ret: _stru_reconnect_reply_pb2.ReconnectReply
        def __init__(self, ret: _Optional[_Union[_stru_reconnect_reply_pb2.ReconnectReply, _Mapping]] = ...) -> None: ...
    class Reconnect(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_reconnect_request_pb2.ReconnectRequest
        def __init__(self, v_request: _Optional[_Union[_stru_reconnect_request_pb2.ReconnectRequest, _Mapping]] = ...) -> None: ...
    class ExitGame(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_exit_game_request_pb2.ExitGameRequest
        def __init__(self, v_request: _Optional[_Union[_stru_exit_game_request_pb2.ExitGameRequest, _Mapping]] = ...) -> None: ...
    class ReportMSdk_Ret(_message.Message):
        __slots__ = ("ret",)
        RET_FIELD_NUMBER: _ClassVar[int]
        ret: _enum_e_error_code_pb2.EErrorCode
        def __init__(self, ret: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
    class ReportMSdk(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_report_m_sdk_request_pb2.ReportMSdkRequest
        def __init__(self, v_request: _Optional[_Union[_stru_report_m_sdk_request_pb2.ReportMSdkRequest, _Mapping]] = ...) -> None: ...
    class GetFaceUpToken(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_get_face_up_token_request_pb2.GetFaceUpTokenRequest
        def __init__(self, v_request: _Optional[_Union[_stru_get_face_up_token_request_pb2.GetFaceUpTokenRequest, _Mapping]] = ...) -> None: ...
    class UploadFaceSuccess_Ret(_message.Message):
        __slots__ = ("ret",)
        RET_FIELD_NUMBER: _ClassVar[int]
        ret: _enum_e_error_code_pb2.EErrorCode
        def __init__(self, ret: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
    class UploadFaceSuccess(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_upload_face_success_request_pb2.UploadFaceSuccessRequest
        def __init__(self, v_request: _Optional[_Union[_stru_upload_face_success_request_pb2.UploadFaceSuccessRequest, _Mapping]] = ...) -> None: ...
    class GetFaceUploadData_Ret(_message.Message):
        __slots__ = ("ret",)
        RET_FIELD_NUMBER: _ClassVar[int]
        ret: _stru_get_face_upload_data_reply_pb2.GetFaceUploadDataReply
        def __init__(self, ret: _Optional[_Union[_stru_get_face_upload_data_reply_pb2.GetFaceUploadDataReply, _Mapping]] = ...) -> None: ...
    class GetFaceUploadData(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_get_face_upload_data_request_pb2.GetFaceUploadDataRequest
        def __init__(self, v_request: _Optional[_Union[_stru_get_face_upload_data_request_pb2.GetFaceUploadDataRequest, _Mapping]] = ...) -> None: ...
    class GetFaceDataUrl_Ret(_message.Message):
        __slots__ = ("ret",)
        RET_FIELD_NUMBER: _ClassVar[int]
        ret: _stru_get_face_data_url_reply_pb2.GetFaceDataUrlReply
        def __init__(self, ret: _Optional[_Union[_stru_get_face_data_url_reply_pb2.GetFaceDataUrlReply, _Mapping]] = ...) -> None: ...
    class GetFaceDataUrl(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_get_face_data_url_request_pb2.GetFaceDataUrlRequest
        def __init__(self, v_request: _Optional[_Union[_stru_get_face_data_url_request_pb2.GetFaceDataUrlRequest, _Mapping]] = ...) -> None: ...
    class CancelDeleteChar_Ret(_message.Message):
        __slots__ = ("ret",)
        RET_FIELD_NUMBER: _ClassVar[int]
        ret: _stru_cancel_delete_char_reply_pb2.CancelDeleteCharReply
        def __init__(self, ret: _Optional[_Union[_stru_cancel_delete_char_reply_pb2.CancelDeleteCharReply, _Mapping]] = ...) -> None: ...
    class CancelDeleteChar(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_cancel_delete_char_request_pb2.CancelDeleteCharRequest
        def __init__(self, v_request: _Optional[_Union[_stru_cancel_delete_char_request_pb2.CancelDeleteCharRequest, _Mapping]] = ...) -> None: ...
    class PrivilegeActivate_Ret(_message.Message):
        __slots__ = ("ret",)
        RET_FIELD_NUMBER: _ClassVar[int]
        ret: _stru_privilege_activate_reply_pb2.PrivilegeActivateReply
        def __init__(self, ret: _Optional[_Union[_stru_privilege_activate_reply_pb2.PrivilegeActivateReply, _Mapping]] = ...) -> None: ...
    class PrivilegeActivate(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_privilege_activate_request_pb2.PrivilegeActivateRequest
        def __init__(self, v_request: _Optional[_Union[_stru_privilege_activate_request_pb2.PrivilegeActivateRequest, _Mapping]] = ...) -> None: ...
    class TakeAwardByCdKey_Ret(_message.Message):
        __slots__ = ("ret",)
        RET_FIELD_NUMBER: _ClassVar[int]
        ret: _enum_e_error_code_pb2.EErrorCode
        def __init__(self, ret: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
    class TakeAwardByCdKey(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_take_award_by_cd_key_request_pb2.TakeAwardByCdKeyRequest
        def __init__(self, v_request: _Optional[_Union[_stru_take_award_by_cd_key_request_pb2.TakeAwardByCdKeyRequest, _Mapping]] = ...) -> None: ...
    class SyncLanguage(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_sync_language_request_pb2.SyncLanguageRequest
        def __init__(self, v_request: _Optional[_Union[_stru_sync_language_request_pb2.SyncLanguageRequest, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...
