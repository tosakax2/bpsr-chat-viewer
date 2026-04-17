import stru_change_avatar_reply_pb2 as _stru_change_avatar_reply_pb2
import stru_change_avatar_request_pb2 as _stru_change_avatar_request_pb2
import stru_get_social_data_reply_pb2 as _stru_get_social_data_reply_pb2
import stru_get_social_data_request_pb2 as _stru_get_social_data_request_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Social(_message.Message):
    __slots__ = ()
    class GetSocialData_Ret(_message.Message):
        __slots__ = ("ret",)
        RET_FIELD_NUMBER: _ClassVar[int]
        ret: _stru_get_social_data_reply_pb2.GetSocialDataReply
        def __init__(self, ret: _Optional[_Union[_stru_get_social_data_reply_pb2.GetSocialDataReply, _Mapping]] = ...) -> None: ...
    class GetSocialData(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_get_social_data_request_pb2.GetSocialDataRequest
        def __init__(self, v_request: _Optional[_Union[_stru_get_social_data_request_pb2.GetSocialDataRequest, _Mapping]] = ...) -> None: ...
    class ChangeAvatar_Ret(_message.Message):
        __slots__ = ("ret",)
        RET_FIELD_NUMBER: _ClassVar[int]
        ret: _stru_change_avatar_reply_pb2.ChangeAvatarReply
        def __init__(self, ret: _Optional[_Union[_stru_change_avatar_reply_pb2.ChangeAvatarReply, _Mapping]] = ...) -> None: ...
    class ChangeAvatar(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_change_avatar_request_pb2.ChangeAvatarRequest
        def __init__(self, v_request: _Optional[_Union[_stru_change_avatar_request_pb2.ChangeAvatarRequest, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...
