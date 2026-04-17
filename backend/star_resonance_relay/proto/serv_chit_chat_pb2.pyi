import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_ark_share_with_tencent_request_pb2 as _stru_ark_share_with_tencent_request_pb2
import stru_create_private_chat_session_reply_pb2 as _stru_create_private_chat_session_reply_pb2
import stru_create_private_chat_session_request_pb2 as _stru_create_private_chat_session_request_pb2
import stru_delete_private_chat_session_reply_pb2 as _stru_delete_private_chat_session_reply_pb2
import stru_delete_private_chat_session_request_pb2 as _stru_delete_private_chat_session_request_pb2
import stru_get_ark_json_with_tencent_reply_pb2 as _stru_get_ark_json_with_tencent_reply_pb2
import stru_get_ark_json_with_tencent_request_pb2 as _stru_get_ark_json_with_tencent_request_pb2
import stru_get_chip_chat_records_reply_pb2 as _stru_get_chip_chat_records_reply_pb2
import stru_get_chip_chat_records_request_pb2 as _stru_get_chip_chat_records_request_pb2
import stru_get_private_chat_targets_reply_pb2 as _stru_get_private_chat_targets_reply_pb2
import stru_get_private_chat_targets_request_pb2 as _stru_get_private_chat_targets_request_pb2
import stru_get_world_chat_channel_id_reply_pb2 as _stru_get_world_chat_channel_id_reply_pb2
import stru_get_world_chat_channel_id_request_pb2 as _stru_get_world_chat_channel_id_request_pb2
import stru_private_chat_block_list_reply_pb2 as _stru_private_chat_block_list_reply_pb2
import stru_private_chat_block_list_request_pb2 as _stru_private_chat_block_list_request_pb2
import stru_private_chat_target_block_reply_pb2 as _stru_private_chat_target_block_reply_pb2
import stru_private_chat_target_block_request_pb2 as _stru_private_chat_target_block_request_pb2
import stru_private_chat_target_top_reply_pb2 as _stru_private_chat_target_top_reply_pb2
import stru_private_chat_target_top_request_pb2 as _stru_private_chat_target_top_request_pb2
import stru_query_chat_mute_reply_pb2 as _stru_query_chat_mute_reply_pb2
import stru_query_chat_mute_request_pb2 as _stru_query_chat_mute_request_pb2
import stru_send_chit_chat_msg_reply_pb2 as _stru_send_chit_chat_msg_reply_pb2
import stru_send_chit_chat_msg_request_pb2 as _stru_send_chit_chat_msg_request_pb2
import stru_set_private_chat_has_read_reply_pb2 as _stru_set_private_chat_has_read_reply_pb2
import stru_set_private_chat_has_read_request_pb2 as _stru_set_private_chat_has_read_request_pb2
import stru_set_world_chat_channel_id_reply_pb2 as _stru_set_world_chat_channel_id_reply_pb2
import stru_set_world_chat_channel_id_request_pb2 as _stru_set_world_chat_channel_id_request_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChitChat(_message.Message):
    __slots__ = ()
    class SendChitChatMsg_Ret(_message.Message):
        __slots__ = ("ret",)
        RET_FIELD_NUMBER: _ClassVar[int]
        ret: _stru_send_chit_chat_msg_reply_pb2.SendChitChatMsgReply
        def __init__(self, ret: _Optional[_Union[_stru_send_chit_chat_msg_reply_pb2.SendChitChatMsgReply, _Mapping]] = ...) -> None: ...
    class SendChitChatMsg(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_send_chit_chat_msg_request_pb2.SendChitChatMsgRequest
        def __init__(self, v_request: _Optional[_Union[_stru_send_chit_chat_msg_request_pb2.SendChitChatMsgRequest, _Mapping]] = ...) -> None: ...
    class GetChipChatRecords_Ret(_message.Message):
        __slots__ = ("ret",)
        RET_FIELD_NUMBER: _ClassVar[int]
        ret: _stru_get_chip_chat_records_reply_pb2.GetChipChatRecordsReply
        def __init__(self, ret: _Optional[_Union[_stru_get_chip_chat_records_reply_pb2.GetChipChatRecordsReply, _Mapping]] = ...) -> None: ...
    class GetChipChatRecords(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_get_chip_chat_records_request_pb2.GetChipChatRecordsRequest
        def __init__(self, v_request: _Optional[_Union[_stru_get_chip_chat_records_request_pb2.GetChipChatRecordsRequest, _Mapping]] = ...) -> None: ...
    class GetPrivateChatTargets_Ret(_message.Message):
        __slots__ = ("ret",)
        RET_FIELD_NUMBER: _ClassVar[int]
        ret: _stru_get_private_chat_targets_reply_pb2.GetPrivateChatTargetsReply
        def __init__(self, ret: _Optional[_Union[_stru_get_private_chat_targets_reply_pb2.GetPrivateChatTargetsReply, _Mapping]] = ...) -> None: ...
    class GetPrivateChatTargets(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_get_private_chat_targets_request_pb2.GetPrivateChatTargetsRequest
        def __init__(self, v_request: _Optional[_Union[_stru_get_private_chat_targets_request_pb2.GetPrivateChatTargetsRequest, _Mapping]] = ...) -> None: ...
    class CreatePrivateChatSession_Ret(_message.Message):
        __slots__ = ("ret",)
        RET_FIELD_NUMBER: _ClassVar[int]
        ret: _stru_create_private_chat_session_reply_pb2.CreatePrivateChatSessionReply
        def __init__(self, ret: _Optional[_Union[_stru_create_private_chat_session_reply_pb2.CreatePrivateChatSessionReply, _Mapping]] = ...) -> None: ...
    class CreatePrivateChatSession(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_create_private_chat_session_request_pb2.CreatePrivateChatSessionRequest
        def __init__(self, v_request: _Optional[_Union[_stru_create_private_chat_session_request_pb2.CreatePrivateChatSessionRequest, _Mapping]] = ...) -> None: ...
    class DeletePrivateChatSession_Ret(_message.Message):
        __slots__ = ("ret",)
        RET_FIELD_NUMBER: _ClassVar[int]
        ret: _stru_delete_private_chat_session_reply_pb2.DeletePrivateChatSessionReply
        def __init__(self, ret: _Optional[_Union[_stru_delete_private_chat_session_reply_pb2.DeletePrivateChatSessionReply, _Mapping]] = ...) -> None: ...
    class DeletePrivateChatSession(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_delete_private_chat_session_request_pb2.DeletePrivateChatSessionRequest
        def __init__(self, v_request: _Optional[_Union[_stru_delete_private_chat_session_request_pb2.DeletePrivateChatSessionRequest, _Mapping]] = ...) -> None: ...
    class SetPrivateChatHasRead_Ret(_message.Message):
        __slots__ = ("ret",)
        RET_FIELD_NUMBER: _ClassVar[int]
        ret: _stru_set_private_chat_has_read_reply_pb2.SetPrivateChatHasReadReply
        def __init__(self, ret: _Optional[_Union[_stru_set_private_chat_has_read_reply_pb2.SetPrivateChatHasReadReply, _Mapping]] = ...) -> None: ...
    class SetPrivateChatHasRead(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_set_private_chat_has_read_request_pb2.SetPrivateChatHasReadRequest
        def __init__(self, v_request: _Optional[_Union[_stru_set_private_chat_has_read_request_pb2.SetPrivateChatHasReadRequest, _Mapping]] = ...) -> None: ...
    class PrivateChatTargetTop_Ret(_message.Message):
        __slots__ = ("ret",)
        RET_FIELD_NUMBER: _ClassVar[int]
        ret: _stru_private_chat_target_top_reply_pb2.PrivateChatTargetTopReply
        def __init__(self, ret: _Optional[_Union[_stru_private_chat_target_top_reply_pb2.PrivateChatTargetTopReply, _Mapping]] = ...) -> None: ...
    class PrivateChatTargetTop(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_private_chat_target_top_request_pb2.PrivateChatTargetTopRequest
        def __init__(self, v_request: _Optional[_Union[_stru_private_chat_target_top_request_pb2.PrivateChatTargetTopRequest, _Mapping]] = ...) -> None: ...
    class PrivateChatTargetBlock_Ret(_message.Message):
        __slots__ = ("ret",)
        RET_FIELD_NUMBER: _ClassVar[int]
        ret: _stru_private_chat_target_block_reply_pb2.PrivateChatTargetBlockReply
        def __init__(self, ret: _Optional[_Union[_stru_private_chat_target_block_reply_pb2.PrivateChatTargetBlockReply, _Mapping]] = ...) -> None: ...
    class PrivateChatTargetBlock(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_private_chat_target_block_request_pb2.PrivateChatTargetBlockRequest
        def __init__(self, v_request: _Optional[_Union[_stru_private_chat_target_block_request_pb2.PrivateChatTargetBlockRequest, _Mapping]] = ...) -> None: ...
    class PrivateChatBlockList_Ret(_message.Message):
        __slots__ = ("ret",)
        RET_FIELD_NUMBER: _ClassVar[int]
        ret: _stru_private_chat_block_list_reply_pb2.PrivateChatBlockListReply
        def __init__(self, ret: _Optional[_Union[_stru_private_chat_block_list_reply_pb2.PrivateChatBlockListReply, _Mapping]] = ...) -> None: ...
    class PrivateChatBlockList(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_private_chat_block_list_request_pb2.PrivateChatBlockListRequest
        def __init__(self, v_request: _Optional[_Union[_stru_private_chat_block_list_request_pb2.PrivateChatBlockListRequest, _Mapping]] = ...) -> None: ...
    class SetWorldChatChannelId_Ret(_message.Message):
        __slots__ = ("ret",)
        RET_FIELD_NUMBER: _ClassVar[int]
        ret: _stru_set_world_chat_channel_id_reply_pb2.SetWorldChatChannelIdReply
        def __init__(self, ret: _Optional[_Union[_stru_set_world_chat_channel_id_reply_pb2.SetWorldChatChannelIdReply, _Mapping]] = ...) -> None: ...
    class SetWorldChatChannelId(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_set_world_chat_channel_id_request_pb2.SetWorldChatChannelIdRequest
        def __init__(self, v_request: _Optional[_Union[_stru_set_world_chat_channel_id_request_pb2.SetWorldChatChannelIdRequest, _Mapping]] = ...) -> None: ...
    class GetWorldChatChannelId_Ret(_message.Message):
        __slots__ = ("ret",)
        RET_FIELD_NUMBER: _ClassVar[int]
        ret: _stru_get_world_chat_channel_id_reply_pb2.GetWorldChatChannelIdReply
        def __init__(self, ret: _Optional[_Union[_stru_get_world_chat_channel_id_reply_pb2.GetWorldChatChannelIdReply, _Mapping]] = ...) -> None: ...
    class GetWorldChatChannelId(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_get_world_chat_channel_id_request_pb2.GetWorldChatChannelIdRequest
        def __init__(self, v_request: _Optional[_Union[_stru_get_world_chat_channel_id_request_pb2.GetWorldChatChannelIdRequest, _Mapping]] = ...) -> None: ...
    class QueryChatMute_Ret(_message.Message):
        __slots__ = ("ret",)
        RET_FIELD_NUMBER: _ClassVar[int]
        ret: _stru_query_chat_mute_reply_pb2.QueryChatMuteReply
        def __init__(self, ret: _Optional[_Union[_stru_query_chat_mute_reply_pb2.QueryChatMuteReply, _Mapping]] = ...) -> None: ...
    class QueryChatMute(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_query_chat_mute_request_pb2.QueryChatMuteRequest
        def __init__(self, v_request: _Optional[_Union[_stru_query_chat_mute_request_pb2.QueryChatMuteRequest, _Mapping]] = ...) -> None: ...
    class ArkShareWithTencent_Ret(_message.Message):
        __slots__ = ("ret",)
        RET_FIELD_NUMBER: _ClassVar[int]
        ret: _enum_e_error_code_pb2.EErrorCode
        def __init__(self, ret: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
    class ArkShareWithTencent(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_ark_share_with_tencent_request_pb2.ArkShareWithTencentRequest
        def __init__(self, v_request: _Optional[_Union[_stru_ark_share_with_tencent_request_pb2.ArkShareWithTencentRequest, _Mapping]] = ...) -> None: ...
    class GetArkJsonWithTencent_Ret(_message.Message):
        __slots__ = ("ret",)
        RET_FIELD_NUMBER: _ClassVar[int]
        ret: _stru_get_ark_json_with_tencent_reply_pb2.GetArkJsonWithTencentReply
        def __init__(self, ret: _Optional[_Union[_stru_get_ark_json_with_tencent_reply_pb2.GetArkJsonWithTencentReply, _Mapping]] = ...) -> None: ...
    class GetArkJsonWithTencent(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_get_ark_json_with_tencent_request_pb2.GetArkJsonWithTencentRequest
        def __init__(self, v_request: _Optional[_Union[_stru_get_ark_json_with_tencent_request_pb2.GetArkJsonWithTencentRequest, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...
