import stru_delete_mail_reply_pb2 as _stru_delete_mail_reply_pb2
import stru_delete_mail_request_pb2 as _stru_delete_mail_request_pb2
import stru_get_mail_uuid_list_reply_pb2 as _stru_get_mail_uuid_list_reply_pb2
import stru_get_mail_uuid_list_request_pb2 as _stru_get_mail_uuid_list_request_pb2
import stru_read_mail_reply_pb2 as _stru_read_mail_reply_pb2
import stru_read_mail_request_pb2 as _stru_read_mail_request_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Mail(_message.Message):
    __slots__ = ()
    class ReadMail_Ret(_message.Message):
        __slots__ = ("ret",)
        RET_FIELD_NUMBER: _ClassVar[int]
        ret: _stru_read_mail_reply_pb2.ReadMailReply
        def __init__(self, ret: _Optional[_Union[_stru_read_mail_reply_pb2.ReadMailReply, _Mapping]] = ...) -> None: ...
    class ReadMail(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_read_mail_request_pb2.ReadMailRequest
        def __init__(self, v_request: _Optional[_Union[_stru_read_mail_request_pb2.ReadMailRequest, _Mapping]] = ...) -> None: ...
    class DeleteMail_Ret(_message.Message):
        __slots__ = ("ret",)
        RET_FIELD_NUMBER: _ClassVar[int]
        ret: _stru_delete_mail_reply_pb2.DeleteMailReply
        def __init__(self, ret: _Optional[_Union[_stru_delete_mail_reply_pb2.DeleteMailReply, _Mapping]] = ...) -> None: ...
    class DeleteMail(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_delete_mail_request_pb2.DeleteMailRequest
        def __init__(self, v_request: _Optional[_Union[_stru_delete_mail_request_pb2.DeleteMailRequest, _Mapping]] = ...) -> None: ...
    class GetMailUuidList_Ret(_message.Message):
        __slots__ = ("ret",)
        RET_FIELD_NUMBER: _ClassVar[int]
        ret: _stru_get_mail_uuid_list_reply_pb2.GetMailUuidListReply
        def __init__(self, ret: _Optional[_Union[_stru_get_mail_uuid_list_reply_pb2.GetMailUuidListReply, _Mapping]] = ...) -> None: ...
    class GetMailUuidList(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_get_mail_uuid_list_request_pb2.GetMailUuidListRequest
        def __init__(self, v_request: _Optional[_Union[_stru_get_mail_uuid_list_request_pb2.GetMailUuidListRequest, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...
