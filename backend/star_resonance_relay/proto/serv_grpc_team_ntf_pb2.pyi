import stru_notice_team_dissolve_request_pb2 as _stru_notice_team_dissolve_request_pb2
import stru_notice_update_team_info_request_pb2 as _stru_notice_update_team_info_request_pb2
import stru_notice_update_team_member_info_request_pb2 as _stru_notice_update_team_member_info_request_pb2
import stru_notify_apply_be_leader_request_pb2 as _stru_notify_apply_be_leader_request_pb2
import stru_notify_apply_join_request_pb2 as _stru_notify_apply_join_request_pb2
import stru_notify_be_transfer_leader_request_pb2 as _stru_notify_be_transfer_leader_request_pb2
import stru_notify_char_abort_match_request_pb2 as _stru_notify_char_abort_match_request_pb2
import stru_notify_char_match_result_request_pb2 as _stru_notify_char_match_result_request_pb2
import stru_notify_invitation_request_pb2 as _stru_notify_invitation_request_pb2
import stru_notify_invite_join_dungeons_request_pb2 as _stru_notify_invite_join_dungeons_request_pb2
import stru_notify_join_team_request_pb2 as _stru_notify_join_team_request_pb2
import stru_notify_leader_apply_list_size_request_pb2 as _stru_notify_leader_apply_list_size_request_pb2
import stru_notify_leave_team_request_pb2 as _stru_notify_leave_team_request_pb2
import stru_notify_refuse_be_transfer_leader_request_pb2 as _stru_notify_refuse_be_transfer_leader_request_pb2
import stru_notify_refuse_invite_request_pb2 as _stru_notify_refuse_invite_request_pb2
import stru_notify_reject_applicant_request_pb2 as _stru_notify_reject_applicant_request_pb2
import stru_notify_team_activity_state_request_pb2 as _stru_notify_team_activity_state_request_pb2
import stru_notify_team_change_member_type_request_pb2 as _stru_notify_team_change_member_type_request_pb2
import stru_notify_team_enter_err_request_pb2 as _stru_notify_team_enter_err_request_pb2
import stru_notify_team_group_update_request_pb2 as _stru_notify_team_group_update_request_pb2
import stru_notify_team_match_result_request_pb2 as _stru_notify_team_match_result_request_pb2
import stru_notify_team_mem_be_call_request_pb2 as _stru_notify_team_mem_be_call_request_pb2
import stru_notify_team_mem_be_call_result_request_pb2 as _stru_notify_team_mem_be_call_result_request_pb2
import stru_notify_team_mem_microphone_status_change_request_pb2 as _stru_notify_team_mem_microphone_status_change_request_pb2
import stru_notify_team_mem_voice_id_change_request_pb2 as _stru_notify_team_mem_voice_id_change_request_pb2
import stru_notify_team_mems_speak_status_change_request_pb2 as _stru_notify_team_mems_speak_status_change_request_pb2
import stru_team_activity_list_result_request_pb2 as _stru_team_activity_list_result_request_pb2
import stru_team_activity_result_request_pb2 as _stru_team_activity_result_request_pb2
import stru_team_activity_vote_result_request_pb2 as _stru_team_activity_vote_result_request_pb2
import stru_update_team_mem_be_call_request_pb2 as _stru_update_team_mem_be_call_request_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GrpcTeamNtf(_message.Message):
    __slots__ = ()
    class NoticeUpdateTeamInfo(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_notice_update_team_info_request_pb2.NoticeUpdateTeamInfoRequest
        def __init__(self, v_request: _Optional[_Union[_stru_notice_update_team_info_request_pb2.NoticeUpdateTeamInfoRequest, _Mapping]] = ...) -> None: ...
    class NoticeUpdateTeamMemberInfo(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_notice_update_team_member_info_request_pb2.NoticeUpdateTeamMemberInfoRequest
        def __init__(self, v_request: _Optional[_Union[_stru_notice_update_team_member_info_request_pb2.NoticeUpdateTeamMemberInfoRequest, _Mapping]] = ...) -> None: ...
    class NotifyJoinTeam(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_notify_join_team_request_pb2.NotifyJoinTeamRequest
        def __init__(self, v_request: _Optional[_Union[_stru_notify_join_team_request_pb2.NotifyJoinTeamRequest, _Mapping]] = ...) -> None: ...
    class NotifyLeaveTeam(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_notify_leave_team_request_pb2.NotifyLeaveTeamRequest
        def __init__(self, v_request: _Optional[_Union[_stru_notify_leave_team_request_pb2.NotifyLeaveTeamRequest, _Mapping]] = ...) -> None: ...
    class NotifyApplyJoin(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_notify_apply_join_request_pb2.NotifyApplyJoinRequest
        def __init__(self, v_request: _Optional[_Union[_stru_notify_apply_join_request_pb2.NotifyApplyJoinRequest, _Mapping]] = ...) -> None: ...
    class NotifyInvitation(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_notify_invitation_request_pb2.NotifyInvitationRequest
        def __init__(self, v_request: _Optional[_Union[_stru_notify_invitation_request_pb2.NotifyInvitationRequest, _Mapping]] = ...) -> None: ...
    class NotifyRefuseInvite(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_notify_refuse_invite_request_pb2.NotifyRefuseInviteRequest
        def __init__(self, v_request: _Optional[_Union[_stru_notify_refuse_invite_request_pb2.NotifyRefuseInviteRequest, _Mapping]] = ...) -> None: ...
    class NotifyLeaderApplyListSize(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_notify_leader_apply_list_size_request_pb2.NotifyLeaderApplyListSizeRequest
        def __init__(self, v_request: _Optional[_Union[_stru_notify_leader_apply_list_size_request_pb2.NotifyLeaderApplyListSizeRequest, _Mapping]] = ...) -> None: ...
    class NotifyApplyBeLeader(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_notify_apply_be_leader_request_pb2.NotifyApplyBeLeaderRequest
        def __init__(self, v_request: _Optional[_Union[_stru_notify_apply_be_leader_request_pb2.NotifyApplyBeLeaderRequest, _Mapping]] = ...) -> None: ...
    class NotifyRejectApplicant(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_notify_reject_applicant_request_pb2.NotifyRejectApplicantRequest
        def __init__(self, v_request: _Optional[_Union[_stru_notify_reject_applicant_request_pb2.NotifyRejectApplicantRequest, _Mapping]] = ...) -> None: ...
    class NotifyBeTransferLeader(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_notify_be_transfer_leader_request_pb2.NotifyBeTransferLeaderRequest
        def __init__(self, v_request: _Optional[_Union[_stru_notify_be_transfer_leader_request_pb2.NotifyBeTransferLeaderRequest, _Mapping]] = ...) -> None: ...
    class NotifyRefuseBeTransferLeader(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_notify_refuse_be_transfer_leader_request_pb2.NotifyRefuseBeTransferLeaderRequest
        def __init__(self, v_request: _Optional[_Union[_stru_notify_refuse_be_transfer_leader_request_pb2.NotifyRefuseBeTransferLeaderRequest, _Mapping]] = ...) -> None: ...
    class NoticeTeamDissolve(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_notice_team_dissolve_request_pb2.NoticeTeamDissolveRequest
        def __init__(self, v_request: _Optional[_Union[_stru_notice_team_dissolve_request_pb2.NoticeTeamDissolveRequest, _Mapping]] = ...) -> None: ...
    class NotifyTeamActivityState(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_notify_team_activity_state_request_pb2.NotifyTeamActivityStateRequest
        def __init__(self, v_request: _Optional[_Union[_stru_notify_team_activity_state_request_pb2.NotifyTeamActivityStateRequest, _Mapping]] = ...) -> None: ...
    class TeamActivityResult(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_team_activity_result_request_pb2.TeamActivityResultRequest
        def __init__(self, v_request: _Optional[_Union[_stru_team_activity_result_request_pb2.TeamActivityResultRequest, _Mapping]] = ...) -> None: ...
    class TeamActivityListResult(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_team_activity_list_result_request_pb2.TeamActivityListResultRequest
        def __init__(self, v_request: _Optional[_Union[_stru_team_activity_list_result_request_pb2.TeamActivityListResultRequest, _Mapping]] = ...) -> None: ...
    class TeamActivityVoteResult(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_team_activity_vote_result_request_pb2.TeamActivityVoteResultRequest
        def __init__(self, v_request: _Optional[_Union[_stru_team_activity_vote_result_request_pb2.TeamActivityVoteResultRequest, _Mapping]] = ...) -> None: ...
    class NotifyCharMatchResult(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_notify_char_match_result_request_pb2.NotifyCharMatchResultRequest
        def __init__(self, v_request: _Optional[_Union[_stru_notify_char_match_result_request_pb2.NotifyCharMatchResultRequest, _Mapping]] = ...) -> None: ...
    class NotifyTeamMatchResult(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_notify_team_match_result_request_pb2.NotifyTeamMatchResultRequest
        def __init__(self, v_request: _Optional[_Union[_stru_notify_team_match_result_request_pb2.NotifyTeamMatchResultRequest, _Mapping]] = ...) -> None: ...
    class NotifyCharAbortMatch(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_notify_char_abort_match_request_pb2.NotifyCharAbortMatchRequest
        def __init__(self, v_request: _Optional[_Union[_stru_notify_char_abort_match_request_pb2.NotifyCharAbortMatchRequest, _Mapping]] = ...) -> None: ...
    class UpdateTeamMemBeCall(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_update_team_mem_be_call_request_pb2.UpdateTeamMemBeCallRequest
        def __init__(self, v_request: _Optional[_Union[_stru_update_team_mem_be_call_request_pb2.UpdateTeamMemBeCallRequest, _Mapping]] = ...) -> None: ...
    class NotifyTeamMemBeCall(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_notify_team_mem_be_call_request_pb2.NotifyTeamMemBeCallRequest
        def __init__(self, v_request: _Optional[_Union[_stru_notify_team_mem_be_call_request_pb2.NotifyTeamMemBeCallRequest, _Mapping]] = ...) -> None: ...
    class NotifyTeamMemBeCallResult(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_notify_team_mem_be_call_result_request_pb2.NotifyTeamMemBeCallResultRequest
        def __init__(self, v_request: _Optional[_Union[_stru_notify_team_mem_be_call_result_request_pb2.NotifyTeamMemBeCallResultRequest, _Mapping]] = ...) -> None: ...
    class NotifyTeamEnterErr(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_notify_team_enter_err_request_pb2.NotifyTeamEnterErrRequest
        def __init__(self, v_request: _Optional[_Union[_stru_notify_team_enter_err_request_pb2.NotifyTeamEnterErrRequest, _Mapping]] = ...) -> None: ...
    class NotifyTeamMemMicrophoneStatusChange(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_notify_team_mem_microphone_status_change_request_pb2.NotifyTeamMemMicrophoneStatusChangeRequest
        def __init__(self, v_request: _Optional[_Union[_stru_notify_team_mem_microphone_status_change_request_pb2.NotifyTeamMemMicrophoneStatusChangeRequest, _Mapping]] = ...) -> None: ...
    class NotifyTeamMemsSpeakStatusChange(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_notify_team_mems_speak_status_change_request_pb2.NotifyTeamMemsSpeakStatusChangeRequest
        def __init__(self, v_request: _Optional[_Union[_stru_notify_team_mems_speak_status_change_request_pb2.NotifyTeamMemsSpeakStatusChangeRequest, _Mapping]] = ...) -> None: ...
    class NotifyTeamMemVoiceIdChange(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_notify_team_mem_voice_id_change_request_pb2.NotifyTeamMemVoiceIdChangeRequest
        def __init__(self, v_request: _Optional[_Union[_stru_notify_team_mem_voice_id_change_request_pb2.NotifyTeamMemVoiceIdChangeRequest, _Mapping]] = ...) -> None: ...
    class NotifyTeamChangeMemberType(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_notify_team_change_member_type_request_pb2.NotifyTeamChangeMemberTypeRequest
        def __init__(self, v_request: _Optional[_Union[_stru_notify_team_change_member_type_request_pb2.NotifyTeamChangeMemberTypeRequest, _Mapping]] = ...) -> None: ...
    class NotifyTeamGroupUpdate(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_notify_team_group_update_request_pb2.NotifyTeamGroupUpdateRequest
        def __init__(self, v_request: _Optional[_Union[_stru_notify_team_group_update_request_pb2.NotifyTeamGroupUpdateRequest, _Mapping]] = ...) -> None: ...
    class NotifyInviteJoinDungeons(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_notify_invite_join_dungeons_request_pb2.NotifyInviteJoinDungeonsRequest
        def __init__(self, v_request: _Optional[_Union[_stru_notify_invite_join_dungeons_request_pb2.NotifyInviteJoinDungeonsRequest, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...
