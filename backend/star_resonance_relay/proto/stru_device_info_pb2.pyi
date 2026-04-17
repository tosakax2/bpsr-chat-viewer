from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceInfo(_message.Message):
    __slots__ = ("client_version", "system_software", "system_hardware", "telecom_oper", "network", "screen_width", "screen_hight", "density", "channel", "cpu_hardware", "memory", "gl_render", "g_l_version", "device_id", "v_client_ip", "v_client_ipv6", "ANDROID_OAID", "IOS_CAID", "platform_user_tag", "mac", "user_agent", "OLD_CAID")
    CLIENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_SOFTWARE_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_HARDWARE_FIELD_NUMBER: _ClassVar[int]
    TELECOM_OPER_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    SCREEN_WIDTH_FIELD_NUMBER: _ClassVar[int]
    SCREEN_HIGHT_FIELD_NUMBER: _ClassVar[int]
    DENSITY_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    CPU_HARDWARE_FIELD_NUMBER: _ClassVar[int]
    MEMORY_FIELD_NUMBER: _ClassVar[int]
    GL_RENDER_FIELD_NUMBER: _ClassVar[int]
    G_L_VERSION_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    V_CLIENT_IP_FIELD_NUMBER: _ClassVar[int]
    V_CLIENT_IPV6_FIELD_NUMBER: _ClassVar[int]
    ANDROID_OAID_FIELD_NUMBER: _ClassVar[int]
    IOS_CAID_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_USER_TAG_FIELD_NUMBER: _ClassVar[int]
    MAC_FIELD_NUMBER: _ClassVar[int]
    USER_AGENT_FIELD_NUMBER: _ClassVar[int]
    OLD_CAID_FIELD_NUMBER: _ClassVar[int]
    client_version: str
    system_software: str
    system_hardware: str
    telecom_oper: str
    network: str
    screen_width: int
    screen_hight: int
    density: float
    channel: str
    cpu_hardware: str
    memory: int
    gl_render: str
    g_l_version: str
    device_id: str
    v_client_ip: str
    v_client_ipv6: str
    ANDROID_OAID: str
    IOS_CAID: str
    platform_user_tag: str
    mac: str
    user_agent: str
    OLD_CAID: str
    def __init__(self, client_version: _Optional[str] = ..., system_software: _Optional[str] = ..., system_hardware: _Optional[str] = ..., telecom_oper: _Optional[str] = ..., network: _Optional[str] = ..., screen_width: _Optional[int] = ..., screen_hight: _Optional[int] = ..., density: _Optional[float] = ..., channel: _Optional[str] = ..., cpu_hardware: _Optional[str] = ..., memory: _Optional[int] = ..., gl_render: _Optional[str] = ..., g_l_version: _Optional[str] = ..., device_id: _Optional[str] = ..., v_client_ip: _Optional[str] = ..., v_client_ipv6: _Optional[str] = ..., ANDROID_OAID: _Optional[str] = ..., IOS_CAID: _Optional[str] = ..., platform_user_tag: _Optional[str] = ..., mac: _Optional[str] = ..., user_agent: _Optional[str] = ..., OLD_CAID: _Optional[str] = ...) -> None: ...
