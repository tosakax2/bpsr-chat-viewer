import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_check_image_request_pb2 as _stru_check_image_request_pb2
import stru_create_album_reply_pb2 as _stru_create_album_reply_pb2
import stru_create_album_request_pb2 as _stru_create_album_request_pb2
import stru_del_func_photo_request_pb2 as _stru_del_func_photo_request_pb2
import stru_delete_album_reply_pb2 as _stru_delete_album_reply_pb2
import stru_delete_album_request_pb2 as _stru_delete_album_request_pb2
import stru_delete_photo_reply_pb2 as _stru_delete_photo_reply_pb2
import stru_delete_photo_request_pb2 as _stru_delete_photo_request_pb2
import stru_edit_album_name_reply_pb2 as _stru_edit_album_name_reply_pb2
import stru_edit_album_name_request_pb2 as _stru_edit_album_name_request_pb2
import stru_edit_album_right_reply_pb2 as _stru_edit_album_right_reply_pb2
import stru_edit_album_right_request_pb2 as _stru_edit_album_right_request_pb2
import stru_get_album_photos_reply_pb2 as _stru_get_album_photos_reply_pb2
import stru_get_album_photos_request_pb2 as _stru_get_album_photos_request_pb2
import stru_get_all_albums_reply_pb2 as _stru_get_all_albums_reply_pb2
import stru_get_all_albums_request_pb2 as _stru_get_all_albums_request_pb2
import stru_get_avatar_token_request_pb2 as _stru_get_avatar_token_request_pb2
import stru_get_func_photo_list_reply_pb2 as _stru_get_func_photo_list_reply_pb2
import stru_get_func_photo_list_request_pb2 as _stru_get_func_photo_list_request_pb2
import stru_get_photo_reply_pb2 as _stru_get_photo_reply_pb2
import stru_get_photo_request_pb2 as _stru_get_photo_request_pb2
import stru_get_photo_up_token_request_pb2 as _stru_get_photo_up_token_request_pb2
import stru_get_review_avatar_info_reply_pb2 as _stru_get_review_avatar_info_reply_pb2
import stru_get_review_avatar_info_request_pb2 as _stru_get_review_avatar_info_request_pb2
import stru_move_photo_to_album_reply_pb2 as _stru_move_photo_to_album_reply_pb2
import stru_move_photo_to_album_request_pb2 as _stru_move_photo_to_album_request_pb2
import stru_set_album_cover_reply_pb2 as _stru_set_album_cover_reply_pb2
import stru_set_album_cover_request_pb2 as _stru_set_album_cover_request_pb2
import stru_set_photo_scheme_name_reply_pb2 as _stru_set_photo_scheme_name_reply_pb2
import stru_set_photo_scheme_name_request_pb2 as _stru_set_photo_scheme_name_request_pb2
import stru_upload_photo_successful_reply_pb2 as _stru_upload_photo_successful_reply_pb2
import stru_upload_photo_successful_request_pb2 as _stru_upload_photo_successful_request_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Photograph(_message.Message):
    __slots__ = ()
    class GetPhotoUpToken(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_get_photo_up_token_request_pb2.GetPhotoUpTokenRequest
        def __init__(self, v_request: _Optional[_Union[_stru_get_photo_up_token_request_pb2.GetPhotoUpTokenRequest, _Mapping]] = ...) -> None: ...
    class DeletePhoto_Ret(_message.Message):
        __slots__ = ("ret",)
        RET_FIELD_NUMBER: _ClassVar[int]
        ret: _stru_delete_photo_reply_pb2.DeletePhotoReply
        def __init__(self, ret: _Optional[_Union[_stru_delete_photo_reply_pb2.DeletePhotoReply, _Mapping]] = ...) -> None: ...
    class DeletePhoto(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_delete_photo_request_pb2.DeletePhotoRequest
        def __init__(self, v_request: _Optional[_Union[_stru_delete_photo_request_pb2.DeletePhotoRequest, _Mapping]] = ...) -> None: ...
    class GetAllAlbums_Ret(_message.Message):
        __slots__ = ("ret",)
        RET_FIELD_NUMBER: _ClassVar[int]
        ret: _stru_get_all_albums_reply_pb2.GetAllAlbumsReply
        def __init__(self, ret: _Optional[_Union[_stru_get_all_albums_reply_pb2.GetAllAlbumsReply, _Mapping]] = ...) -> None: ...
    class GetAllAlbums(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_get_all_albums_request_pb2.GetAllAlbumsRequest
        def __init__(self, v_request: _Optional[_Union[_stru_get_all_albums_request_pb2.GetAllAlbumsRequest, _Mapping]] = ...) -> None: ...
    class GetAlbumPhotos_Ret(_message.Message):
        __slots__ = ("ret",)
        RET_FIELD_NUMBER: _ClassVar[int]
        ret: _stru_get_album_photos_reply_pb2.GetAlbumPhotosReply
        def __init__(self, ret: _Optional[_Union[_stru_get_album_photos_reply_pb2.GetAlbumPhotosReply, _Mapping]] = ...) -> None: ...
    class GetAlbumPhotos(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_get_album_photos_request_pb2.GetAlbumPhotosRequest
        def __init__(self, v_request: _Optional[_Union[_stru_get_album_photos_request_pb2.GetAlbumPhotosRequest, _Mapping]] = ...) -> None: ...
    class CreateAlbum_Ret(_message.Message):
        __slots__ = ("ret",)
        RET_FIELD_NUMBER: _ClassVar[int]
        ret: _stru_create_album_reply_pb2.CreateAlbumReply
        def __init__(self, ret: _Optional[_Union[_stru_create_album_reply_pb2.CreateAlbumReply, _Mapping]] = ...) -> None: ...
    class CreateAlbum(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_create_album_request_pb2.CreateAlbumRequest
        def __init__(self, v_request: _Optional[_Union[_stru_create_album_request_pb2.CreateAlbumRequest, _Mapping]] = ...) -> None: ...
    class DeleteAlbum_Ret(_message.Message):
        __slots__ = ("ret",)
        RET_FIELD_NUMBER: _ClassVar[int]
        ret: _stru_delete_album_reply_pb2.DeleteAlbumReply
        def __init__(self, ret: _Optional[_Union[_stru_delete_album_reply_pb2.DeleteAlbumReply, _Mapping]] = ...) -> None: ...
    class DeleteAlbum(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_delete_album_request_pb2.DeleteAlbumRequest
        def __init__(self, v_request: _Optional[_Union[_stru_delete_album_request_pb2.DeleteAlbumRequest, _Mapping]] = ...) -> None: ...
    class EditAlbumRight_Ret(_message.Message):
        __slots__ = ("ret",)
        RET_FIELD_NUMBER: _ClassVar[int]
        ret: _stru_edit_album_right_reply_pb2.EditAlbumRightReply
        def __init__(self, ret: _Optional[_Union[_stru_edit_album_right_reply_pb2.EditAlbumRightReply, _Mapping]] = ...) -> None: ...
    class EditAlbumRight(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_edit_album_right_request_pb2.EditAlbumRightRequest
        def __init__(self, v_request: _Optional[_Union[_stru_edit_album_right_request_pb2.EditAlbumRightRequest, _Mapping]] = ...) -> None: ...
    class EditAlbumName_Ret(_message.Message):
        __slots__ = ("ret",)
        RET_FIELD_NUMBER: _ClassVar[int]
        ret: _stru_edit_album_name_reply_pb2.EditAlbumNameReply
        def __init__(self, ret: _Optional[_Union[_stru_edit_album_name_reply_pb2.EditAlbumNameReply, _Mapping]] = ...) -> None: ...
    class EditAlbumName(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_edit_album_name_request_pb2.EditAlbumNameRequest
        def __init__(self, v_request: _Optional[_Union[_stru_edit_album_name_request_pb2.EditAlbumNameRequest, _Mapping]] = ...) -> None: ...
    class SetAlbumCover_Ret(_message.Message):
        __slots__ = ("ret",)
        RET_FIELD_NUMBER: _ClassVar[int]
        ret: _stru_set_album_cover_reply_pb2.SetAlbumCoverReply
        def __init__(self, ret: _Optional[_Union[_stru_set_album_cover_reply_pb2.SetAlbumCoverReply, _Mapping]] = ...) -> None: ...
    class SetAlbumCover(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_set_album_cover_request_pb2.SetAlbumCoverRequest
        def __init__(self, v_request: _Optional[_Union[_stru_set_album_cover_request_pb2.SetAlbumCoverRequest, _Mapping]] = ...) -> None: ...
    class MovePhotoToAlbum_Ret(_message.Message):
        __slots__ = ("ret",)
        RET_FIELD_NUMBER: _ClassVar[int]
        ret: _stru_move_photo_to_album_reply_pb2.MovePhotoToAlbumReply
        def __init__(self, ret: _Optional[_Union[_stru_move_photo_to_album_reply_pb2.MovePhotoToAlbumReply, _Mapping]] = ...) -> None: ...
    class MovePhotoToAlbum(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_move_photo_to_album_request_pb2.MovePhotoToAlbumRequest
        def __init__(self, v_request: _Optional[_Union[_stru_move_photo_to_album_request_pb2.MovePhotoToAlbumRequest, _Mapping]] = ...) -> None: ...
    class GetAvatarToken(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_get_avatar_token_request_pb2.GetAvatarTokenRequest
        def __init__(self, v_request: _Optional[_Union[_stru_get_avatar_token_request_pb2.GetAvatarTokenRequest, _Mapping]] = ...) -> None: ...
    class GetPhoto_Ret(_message.Message):
        __slots__ = ("ret",)
        RET_FIELD_NUMBER: _ClassVar[int]
        ret: _stru_get_photo_reply_pb2.GetPhotoReply
        def __init__(self, ret: _Optional[_Union[_stru_get_photo_reply_pb2.GetPhotoReply, _Mapping]] = ...) -> None: ...
    class GetPhoto(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_get_photo_request_pb2.GetPhotoRequest
        def __init__(self, v_request: _Optional[_Union[_stru_get_photo_request_pb2.GetPhotoRequest, _Mapping]] = ...) -> None: ...
    class UploadPhotoSuccessful_Ret(_message.Message):
        __slots__ = ("ret",)
        RET_FIELD_NUMBER: _ClassVar[int]
        ret: _stru_upload_photo_successful_reply_pb2.UploadPhotoSuccessfulReply
        def __init__(self, ret: _Optional[_Union[_stru_upload_photo_successful_reply_pb2.UploadPhotoSuccessfulReply, _Mapping]] = ...) -> None: ...
    class UploadPhotoSuccessful(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_upload_photo_successful_request_pb2.UploadPhotoSuccessfulRequest
        def __init__(self, v_request: _Optional[_Union[_stru_upload_photo_successful_request_pb2.UploadPhotoSuccessfulRequest, _Mapping]] = ...) -> None: ...
    class GetReviewAvatarInfo_Ret(_message.Message):
        __slots__ = ("ret",)
        RET_FIELD_NUMBER: _ClassVar[int]
        ret: _stru_get_review_avatar_info_reply_pb2.GetReviewAvatarInfoReply
        def __init__(self, ret: _Optional[_Union[_stru_get_review_avatar_info_reply_pb2.GetReviewAvatarInfoReply, _Mapping]] = ...) -> None: ...
    class GetReviewAvatarInfo(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_get_review_avatar_info_request_pb2.GetReviewAvatarInfoRequest
        def __init__(self, v_request: _Optional[_Union[_stru_get_review_avatar_info_request_pb2.GetReviewAvatarInfoRequest, _Mapping]] = ...) -> None: ...
    class GetFuncPhotoList_Ret(_message.Message):
        __slots__ = ("ret",)
        RET_FIELD_NUMBER: _ClassVar[int]
        ret: _stru_get_func_photo_list_reply_pb2.GetFuncPhotoListReply
        def __init__(self, ret: _Optional[_Union[_stru_get_func_photo_list_reply_pb2.GetFuncPhotoListReply, _Mapping]] = ...) -> None: ...
    class GetFuncPhotoList(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_get_func_photo_list_request_pb2.GetFuncPhotoListRequest
        def __init__(self, v_request: _Optional[_Union[_stru_get_func_photo_list_request_pb2.GetFuncPhotoListRequest, _Mapping]] = ...) -> None: ...
    class DelFuncPhoto_Ret(_message.Message):
        __slots__ = ("ret",)
        RET_FIELD_NUMBER: _ClassVar[int]
        ret: _enum_e_error_code_pb2.EErrorCode
        def __init__(self, ret: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
    class DelFuncPhoto(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_del_func_photo_request_pb2.DelFuncPhotoRequest
        def __init__(self, v_request: _Optional[_Union[_stru_del_func_photo_request_pb2.DelFuncPhotoRequest, _Mapping]] = ...) -> None: ...
    class SetPhotoSchemeName_Ret(_message.Message):
        __slots__ = ("ret",)
        RET_FIELD_NUMBER: _ClassVar[int]
        ret: _stru_set_photo_scheme_name_reply_pb2.SetPhotoSchemeNameReply
        def __init__(self, ret: _Optional[_Union[_stru_set_photo_scheme_name_reply_pb2.SetPhotoSchemeNameReply, _Mapping]] = ...) -> None: ...
    class SetPhotoSchemeName(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_set_photo_scheme_name_request_pb2.SetPhotoSchemeNameRequest
        def __init__(self, v_request: _Optional[_Union[_stru_set_photo_scheme_name_request_pb2.SetPhotoSchemeNameRequest, _Mapping]] = ...) -> None: ...
    class CheckImage_Ret(_message.Message):
        __slots__ = ("ret",)
        RET_FIELD_NUMBER: _ClassVar[int]
        ret: _enum_e_error_code_pb2.EErrorCode
        def __init__(self, ret: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
    class CheckImage(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_check_image_request_pb2.CheckImageRequest
        def __init__(self, v_request: _Optional[_Union[_stru_check_image_request_pb2.CheckImageRequest, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...
