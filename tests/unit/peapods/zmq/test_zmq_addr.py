import pytest

from jina import __windows__
from jina.peapods.zmq import Zmqlet


@pytest.mark.parametrize('host', ['pi@192.0.0.1', '192.0.0.1'])
def test_get_ctrl_addr(host):
    assert Zmqlet.get_ctrl_address(host, 56789, False)[0] == 'tcp://192.0.0.1:56789'


@pytest.mark.parametrize('host', ['pi@192.0.0.1', '192.0.0.1'])
def test_get_ctrl_addr_ipc(host):
    assert (
        Zmqlet.get_ctrl_address(host, 56789, True)[0].startswith('ipc') != __windows__
    )
