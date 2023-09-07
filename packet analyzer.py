import socket
import struct
import textwrap

def main():
    # Create a raw socket to capture packets
    sniffer_socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

    try:
        while True:
            # Capture a packet (you can also specify a buffer size)
            raw_packet, addr = sniffer_socket.recvfrom(65535)

            # Unpack the Ethernet frame (14 bytes for the header)
            dest_mac, src_mac, eth_proto, data = unpack_ethernet_frame(raw_packet[:14])
            print("Ethernet Frame:")
            print(f"Destination MAC: {dest_mac}, Source MAC: {src_mac}, Protocol: {eth_proto}")

            # Check if the packet is an IP packet (Ethernet Protocol 0x0800)
            if eth_proto == 0x0800:
                # Unpack the IP header (20 bytes for the header)
                version, header_length, ttl, proto, src_ip, dest_ip, ip_data = unpack_ip_header(data)
                print("IP Packet:")
                print(f"Version: {version}, Header Length: {header_length}, TTL: {ttl}, Protocol: {proto}")
                print(f"Source IP: {src_ip}, Destination IP: {dest_ip}")

                # Check if the packet is a TCP packet (IP Protocol 6)
                if proto == 6:
                    # Unpack the TCP header (20 bytes for the header)
                    src_port, dest_port, sequence, acknowledgment, offset_reserved_flags, tcp_data = unpack_tcp_header(ip_data)
                    print("TCP Segment:")
                    print(f"Source Port: {src_port}, Destination Port: {dest_port}")
                    print(f"Sequence Number: {sequence}, Acknowledgment Number: {acknowledgment}")
                    print(f"Flags: {offset_reserved_flags}")

                    # Display the actual data in the packet
                    print("Data:")
                    print(format_multi_line(tcp_data))

    except KeyboardInterrupt:
        print("Sniffer stopped by user.")
        sniffer_socket.close()

def unpack_ethernet_frame(data):
    dest_mac, src_mac, proto = struct.unpack('! 6s 6s H', data)
    return get_mac_addr(dest_mac), get_mac_addr(src_mac), socket.htons(proto), data[14:]

def get_mac_addr(bytes_addr):
    # Convert a MAC address from a bytes representation to a readable string
    bytes_str = map("{:02x}".format, bytes_addr)
    return ":".join(bytes_str).upper()

def unpack_ip_header(data):
    version_header_length = data[0]
    version = version_header_length >> 4
    header_length = (version_header_length & 15) * 4
    ttl, proto, src_ip, dest_ip = struct.unpack('! 8x B B 2x 4s 4s', data[:20])
    return version, header_length, ttl, proto, get_ip_addr(src_ip), get_ip_addr(dest_ip), data[header_length:]

def get_ip_addr(bytes_addr):
    # Convert an IP address from a bytes representation to a readable string
    return ".".join(map(str, bytes_addr))

def unpack_tcp_header(data):
    src_port, dest_port, sequence, acknowledgment, offset_reserved_flags = struct.unpack('! H H L L H', data[:14])
    return src_port, dest_port, sequence, acknowledgment, offset_reserved_flags, data[14:]

def format_multi_line(data, indent=0):
    # Insert newline characters every 16 bytes for readability
    return "\n".join(textwrap.wrap(data.hex(), 16))

if __name__ == "__main__":
    main()
