"""Widgets to monitor network status."""

import human_readable
import psutil

from rsysmon.widgets import Information


def get_network_address(nic: str) -> str:
    """Return network address of nic."""
    addr = psutil.net_if_addrs()[nic][0].address
    return f"{nic}: {addr}"


def get_network_io() -> str:
    """Return network I/O statistics."""
    stats = psutil.net_io_counters()
    rx = human_readable.file_size(stats.bytes_recv, binary=True)
    rx_packets = human_readable.int_word(stats.packets_recv)
    tx = human_readable.file_size(stats.bytes_sent, binary=True)
    tx_packets = human_readable.int_word(stats.packets_sent)
    return f"Rx: {rx} ({rx_packets} packets)\nTx: {tx} ({tx_packets} packets)"


class NetworkAddress(Information):
    """Display network address of nic."""

    def __init__(self, nic: str) -> None:
        """Initialise parent Information with address function for nic."""
        super().__init__(lambda: get_network_address(nic))


class NetworkIO(Information):
    """Display I/O statistics of network."""

    def __init__(self) -> None:
        """Initialise parent Information with network I/O."""
        super().__init__(get_network_io)
