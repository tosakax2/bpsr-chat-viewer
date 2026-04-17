import stru_notify_add_private_chat_session_request_pb2 as _stru_notify_add_private_chat_session_request_pb2
import stru_notify_be_muted_request_pb2 as _stru_notify_be_muted_request_pb2
import stru_notify_clear_chat_history_request_pb2 as _stru_notify_clear_chat_history_request_pb2
import stru_notify_newest_chit_chat_msgs_request_pb2 as _stru_notify_newest_chit_chat_msgs_request_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChitChatNtf(_message.Message):
    __slots__ = ()
    class NotifyNewestChitChatMsgs(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_notify_newest_chit_chat_msgs_request_pb2.NotifyNewestChitChatMsgsRequest
        def __init__(self, v_request: _Optional[_Union[_stru_notify_newest_chit_chat_msgs_request_pb2.NotifyNewestChitChatMsgsRequest, _Mapping]] = ...) -> None: ...
    class NotifyBeMuted(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_notify_be_muted_request_pb2.NotifyBeMutedRequest
        def __init__(self, v_request: _Optional[_Union[_stru_notify_be_muted_request_pb2.NotifyBeMutedRequest, _Mapping]] = ...) -> None: ...
    class NotifyAddPrivateChatSession(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_notify_add_private_chat_session_request_pb2.NotifyAddPrivateChatSessionRequest
        def __init__(self, v_request: _Optional[_Union[_stru_notify_add_private_chat_session_request_pb2.NotifyAddPrivateChatSessionRequest, _Mapping]] = ...) -> None: ...
    class NotifyClearChatHistory(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_notify_clear_chat_history_request_pb2.NotifyClearChatHistoryRequest
        def __init__(self, v_request: _Optional[_Union[_stru_notify_clear_chat_history_request_pb2.NotifyClearChatHistoryRequest, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...
