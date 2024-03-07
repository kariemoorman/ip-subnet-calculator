import argparse
import re


class IPv6Address:
    def __init__(self, ipv6_address, cidr):
        if not self.is_valid_ipv6_address(ipv6_address):
            raise ValueError("Invalid IPv6 address format.")
        else:
            self.ip_address = ipv6_address
        if not self.is_valid_cidr(cidr):
            raise ValueError("Invalid CIDR format.")
        else:
            self.cidr = cidr
            
    @staticmethod
    def is_valid_ipv6_address(ipv6_address):
        # Regular expression for validating IPv6 addresses
        ipv6_pattern = re.compile(r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$')
        if not ipv6_pattern.match(ipv6_address):
            return False
        return True

    @staticmethod
    def is_valid_cidr(cidr_notation):
        try:
            cidr_value = int(cidr_notation)
            return 0 <= cidr_value <= 64
        except (ValueError, TypeError):
            return False

    def subnet_mask_to_segments(self):
        # Convert IPv6 subnet mask to a list of hexadecimal segments
        return ["ffff"] * (int(self.cidr) // 16) + [format(2 ** (16 - int(self.cidr) % 16), 'x')]
    
    def ipv6_to_hex(self):
        # Split the IPv6 address into its segments
        segments = self.ip_address.split(':')
        # Convert each segment to its hexadecimal form
        hex_segments = [format(int(seg, 16), '04x') for seg in segments]
        # Join the hexadecimal segments to form the complete IPv6 address
        hex_ipv6_address = ':'.join(hex_segments)
        return hex_ipv6_address

    def ipv6_to_binary(self):
        # Split the IPv6 address into its segments
        segments = self.ip_address.split(':')
        # Convert each segment to its binary form
        binary_segments = [format(int(seg, 16), '016b') for seg in segments]
        # Join the binary segments to form the complete IPv6 address
        binary_ipv6_address = ':'.join('.'.join([binary_seg[i:i+4] for i in range(0, len(binary_seg), 4)]) for binary_seg in binary_segments)
        return binary_ipv6_address
    
    def cidr_to_subnet_mask(self):
        # Calculate the subnet mask using bitwise left shift
        subnet_mask = (2 ** 128 - 1) << (128 - int(self.cidr))
        # Convert the subnet mask to hex and split into segments
        subnet_mask_hex = format(subnet_mask, '032x')
        segments = [subnet_mask_hex[i:i+4] for i in range(0, len(subnet_mask_hex), 4)]
        # Join segments to form the IPv6 subnet mask
        ipv6_subnet_mask = ':'.join(segments)
        return ipv6_subnet_mask
    
    def cidr_to_subnet_mask_binary(self):
        # Convert CIDR to subnet mask
        subnet_mask = self.cidr_to_subnet_mask()
        # Split the IPv6 subnet mask into its segments
        segments = subnet_mask.split(':')
        # Convert each segment to its binary form
        binary_segments = [format(int(seg, 16), '016b') for seg in segments]
        # Join the binary segments to form the complete IPv6 subnet mask
        binary_subnet_mask = ':'.join('.'.join([binary_seg[i:i+4] for i in range(0, len(binary_seg), 4)]) for binary_seg in binary_segments)
        return binary_subnet_mask
    
    def classify_ipv6(self):
        # Check if the IPv6 address is link-local or unique local
        if self.ip_address.startswith("fe80:"):
            return "Link-local"
        elif self.ip_address.startswith("fc00:") or self.ip_address.startswith("fd00:"):
            return "Unique local"
        else:
            return "Public"
    
    def network_to_binary(self, network_address):
        # Split the IPv6 address into its segments
        segments = network_address.split(':')
        # Convert each segment to its binary form
        binary_segments = [format(int(seg, 16), '016b') for seg in segments]
        # Join the binary segments to form the complete IPv6 address
        binary_network_address = ':'.join('.'.join([binary_seg[i:i+4] for i in range(0, len(binary_seg), 4)]) for binary_seg in binary_segments)
        return binary_network_address
    
    def get_subnet_network_address(self):
        # Classify IPv6 address as local or private
        classification = self.classify_ipv6()
        # Convert IPv6 address and subnet mask to lists of integers
        ip_segments = self.ip_address.split(':')
        subnet_segments = self.subnet_mask_to_segments()
        # Perform bitwise AND operation for each segment
        network_segments = [int(ip, 16) & int(subnet, 16) for ip, subnet in zip(ip_segments, subnet_segments)]
        # Join segments to form the network address
        network_address = ':'.join(format(segment, '04x') for segment in network_segments)
        # Transform ipv6 to hex 
        ipv6_binary = self.ipv6_to_binary()
        subnet_binary = self.cidr_to_subnet_mask_binary()
        network_binary = self.network_to_binary(network_address)
        
        print(f"\nIPv6 Address: {self.ip_address}")
        print(f"IP Type: {classification}")
        print(f"CIDR Notation: /{self.cidr}")
        print(f"Network Address: {network_address}\n")
        print(f"Binary IPv6 Address: {ipv6_binary}")
        print(f"Binary Subnet Mask: {subnet_binary}")
        print(f"Binary Network Address: {network_binary}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find Network Address from IPv6 Address")  
    parser.add_argument("ipv6_address", type=str, help="IPv6 Address (e.g., 2001:db8:85a3::8a2e:370:7334)")
    parser.add_argument("-c", "--cidr", type=str, default=64, help="CIDR notation of subnet address (e.g., 24)")
    
    args = parser.parse_args()
    
    ip_address = IPv6Address(args.ipv6_address, args.cidr)
    ip_address.get_subnet_network_address()
