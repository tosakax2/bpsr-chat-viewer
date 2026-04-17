import stru_get_photo_token_ntf_request_pb2 as _stru_get_photo_token_ntf_request_pb2
import stru_ret_avatar_token_request_pb2 as _stru_ret_avatar_token_request_pb2
import stru_review_avatar_info_ntf_request_pb2 as _stru_review_avatar_info_ntf_request_pb2
import stru_upload_photo_result_ntf_request_pb2 as _stru_upload_photo_result_ntf_request_pb2
import stru_upload_picture_result_ntf_request_pb2 as _stru_upload_picture_result_ntf_request_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PhotographNtf(_message.Message):
    __slots__ = ()
    class GetPhotoTokenNtf(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_get_photo_token_ntf_request_pb2.GetPhotoTokenNtfRequest
        def __init__(self, v_request: _Optional[_Union[_stru_get_photo_token_ntf_request_pb2.GetPhotoTokenNtfRequest, _Mapping]] = ...) -> None: ...
    class UploadPhotoResultNtf(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_upload_photo_result_ntf_request_pb2.UploadPhotoResultNtfRequest
        def __init__(self, v_request: _Optional[_Union[_stru_upload_photo_result_ntf_request_pb2.UploadPhotoResultNtfRequest, _Mapping]] = ...) -> None: ...
    class UploadPictureResultNtf(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_upload_picture_result_ntf_request_pb2.UploadPictureResultNtfRequest
        def __init__(self, v_request: _Optional[_Union[_stru_upload_picture_result_ntf_request_pb2.UploadPictureResultNtfRequest, _Mapping]] = ...) -> None: ...
    class RetAvatarToken(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_ret_avatar_token_request_pb2.RetAvatarTokenRequest
        def __init__(self, v_request: _Optional[_Union[_stru_ret_avatar_token_request_pb2.RetAvatarTokenRequest, _Mapping]] = ...) -> None: ...
    class ReviewAvatarInfoNtf(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_review_avatar_info_ntf_request_pb2.ReviewAvatarInfoNtfRequest
        def __init__(self, v_request: _Optional[_Union[_stru_review_avatar_info_ntf_request_pb2.ReviewAvatarInfoNtfRequest, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...
