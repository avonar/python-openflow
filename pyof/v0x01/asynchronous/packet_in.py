"""For packets received by the datapath and sent to the controller."""

# System imports
import enum

# Third-party imports

# Local source tree imports
from pyof.v0x01.common import header as of_header
from pyof.v0x01.foundation import base
from pyof.v0x01.foundation import basic_types

# Enums


class PacketInReason(enum.Enum):
    """Reason why this packet is being sent to the controller."""

    #: No matching flow
    OFPR_NO_MATCH = 1
    #: Action explicitly output to controller
    OFPR_ACTION = 2


# Classes


class PacketIn(base.GenericMessage):
    """Packet received on port (datapath -> controller).

    Args:
        xid (int): Header's xid.
        buffer_id (int): ID assigned by datapath.
        total_len (int): Full length of frame.
        in_port (int): Port on which frame was received.
        reason (PacketInReason): The reason why the packet is being sent
        data (bytes): Ethernet frame, halfway through 32-bit word, so the IP
            header is 32-bit aligned. The amount of data is inferred from the
            length field in the header. Because of padding,
            offsetof(struct ofp_packet_in, data) ==
            sizeof(struct ofp_packet_in) - 2.
    """

    #: :class:`~.header.Header`: OpenFlow Header
    header = of_header.Header(message_type=of_header.Type.OFPT_PACKET_IN)
    buffer_id = basic_types.UBInt32()
    total_len = basic_types.UBInt16()
    in_port = basic_types.UBInt16()
    reason = basic_types.UBInt8(enum_ref=PacketInReason)
    #: Align to 32-bits.
    pad = basic_types.PAD(1)
    data = basic_types.BinaryData()

    def __init__(self, xid=None, buffer_id=None, total_len=None, in_port=None,
                 reason=None, data=b''):
        super().__init__()
        self.header.xid = xid if xid else self.header.xid
        self.buffer_id = buffer_id
        self.total_len = total_len
        self.in_port = in_port
        self.reason = reason
        self.data = data
