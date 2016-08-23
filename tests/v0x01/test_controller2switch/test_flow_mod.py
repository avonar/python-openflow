"""Flow modification (add/delete) message tests."""
import unittest

from pyof.v0x01.common.flow_match import Match
from pyof.v0x01.controller2switch.flow_mod import FlowMod, FlowModCommand
from tests.test_struct import TestStruct


class TestFlowAdd(TestStruct):
    """Flow addition message tests (also those in :class:`.TestDump`)."""

    @classmethod
    def setUpClass(cls):
        """Configure raw file and its object in parent class (TestDump)."""
        super().setUpClass()
        super().set_raw_dump_file('v0x01', 'ofpt_flow_add')
        kwargs = _get_flowmod_kwargs(FlowModCommand.OFPFC_ADD)
        super().set_raw_dump_object(FlowMod, **kwargs)
        super().set_minimum_size(72)

    @unittest.skip('Need to recover dump contents.')
    def test_pack(self):
        pass

    @unittest.skip('Need to recover dump contents.')
    def test_unpack(self):
        pass


class TestFlowDelete(TestStruct):
    """Flow deletion message tests (also those in :class:`.TestDump`)."""

    @classmethod
    def setUpClass(cls):
        """Configure raw file and its object in parent class (TestDump)."""
        super().setUpClass()
        super().set_raw_dump_file('v0x01', 'ofpt_flow_delete')
        kwargs = _get_flowmod_kwargs(FlowModCommand.OFPFC_DELETE)
        super().set_raw_dump_object(FlowMod, **kwargs)
        # No need to test minimum size again.


def _get_flowmod_kwargs(command):
    """Return parameters for FlowMod object."""
    return {'xid': 4,
            'command': command,
            'match': _get_match(),
            'cookie': 0,
            'idle_timeout': 0,
            'hard_timeout': 0,
            'priority': 32768,
            'buffer_id': 4294967295,
            'out_port': 65535,
            'flags': 0}


def _get_match():
    """Return a Match object."""
    return Match(wildcards=0x000000000010001f,
                 in_port=0,
                 dl_src='00:00:00:00:00:00',
                 dl_dst='00:00:00:00:00:00',
                 dl_vlan=0,
                 dl_vlan_pcp=0,
                 dl_type=0,
                 nw_tos=0,
                 nw_proto=0,
                 nw_src=0,
                 nw_dst=0,
                 tp_src=0,
                 tp_dst=0)
