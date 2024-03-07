import argparse

class IPv4Address:
    def __init__(self, ipv4_address): 
        self.ip_address = ipv4_address
    
    def get_broadcast_address(self, subnet_mask): 
        # Convert IP address and subnet mask to lists of integers
        ip_octets = [int(octet) for octet in self.ip_address.split('.')]
        subnet_octets = [int(octet) for octet in subnet_mask.split('.')]
        # Calculate the network address using bitwise AND operation
        network_octets = [ip_octets[i] & subnet_octets[i] for i in range(4)]
        # Calculate the broadcast address using bitwise OR operation with inverted subnet mask
        inverted_subnet_octets = [255 - subnet_octet for subnet_octet in subnet_octets]
        broadcast_octets = [network_octets[i] | inverted_subnet_octets[i] for i in range(4)]
        # Join octets to form the broadcast address
        broadcast_address = '.'.join(map(str, broadcast_octets))
        return broadcast_address

    def classify_ip_address(self):
        # Convert IP address to a list of integers
        ip_octets = [int(octet) for octet in self.ip_address.split('.')]
        # Classify based on the first octet
        ip_class = None
        if 1 <= ip_octets[0] <= 126:
            ip_class = 'A'
        elif 128 <= ip_octets[0] <= 191:
            ip_class = 'B'
        elif 192 <= ip_octets[0] <= 223:
            ip_class = 'C'
        elif 224 <= ip_octets[0] <= 239:
            ip_class = 'D'
        elif 240 <= ip_octets[0] <= 255:
            ip_class = 'E'
        # Check if the IP address is private
        is_private = False
        if ip_class in ['A', 'B', 'C']:
            private_ranges = [
                (10, 0, 0, 0, 10, 255, 255, 255),  # Class A private range
                (172, 16, 0, 0, 172, 31, 255, 255),  # Class B private range
                (192, 168, 0, 0, 192, 168, 255, 255)  # Class C private range
            ]
            for private_range in private_ranges:
                if (
                    private_range[0] <= ip_octets[0] <= private_range[4] and
                    private_range[1] <= ip_octets[1] <= private_range[5] and
                    private_range[2] <= ip_octets[2] <= private_range[6] and
                    private_range[3] <= ip_octets[3] <= private_range[7]
                ):
                    is_private = True
                    break
        return {
            'IP Class': ip_class,
            'IP Type': 'Private' if is_private else 'Public'
        }

    def subnet_mask_to_cidr(self, subnet_mask):
        # Convert the subnet mask to a binary string
        binary_subnet_mask = ''.join(format(int(octet), '08b') for octet in subnet_mask.split('.'))
        # Count the number of consecutive '1' bits
        cidr_notation = binary_subnet_mask.count('1')
        # Return cidr_notation
        return cidr_notation
    
    def get_subnet_network_address(self, subnet_mask, cidr):
        # Classify IP address
        classification = self.classify_ip_address()
        # Convert IP address and subnet mask to lists of integers
        ip_octets = [int(octet) for octet in self.ip_address.split('.')]
        subnet_octets = [int(octet) for octet in subnet_mask.split('.')]
        # Perform bitwise AND operation for each octet
        network_octets = [ip_octets[i] & subnet_octets[i] for i in range(4)]
        # Join octets to form the network address
        network_address = '.'.join(map(str, network_octets))
        # Calculate broadcast network
        broadcast_address = self.get_broadcast_address(subnet_mask)
        # Calculate binary 
        binary_ip_address = ''.join(format(octet, '08b') for octet in ip_octets)
        binary_subnet_mask = ''.join(format(octet, '08b') for octet in subnet_octets)
        binary_network_address = ''.join(format(octet, '08b') for octet in network_octets)
        # Return network_address
        print(f"\nIPv4 Address: \t\t {self.ip_address}")
        print(f"IP Class: \t\t {classification['IP Class']}")
        print(f"IP Type: \t\t {classification['IP Type']}")
        print(f"CIDR Notation: \t\t /{cidr}")
        print(f"Subnet Mask: \t\t {subnet_mask}")
        print(f"Network Address: \t {network_address}")
        print(f"Broadcast Address: \t {broadcast_address}\n")
        
        print(f"Binary IPv4 Address: \t {binary_ip_address}")
        print(f"Binary Subnet Mask: \t {binary_subnet_mask}")
        print(f"Binary Network Address:  {binary_network_address}")

    def cidr_to_subnet_mask(self, cidr):
        # Calculate the subnet mask using bitwise left shift
        subnet_mask = (2 ** 32 - 1) << (32 - int(cidr))
        # Convert the subnet mask to octets
        subnet_octets = [(subnet_mask >> i) & 255 for i in (24, 16, 8, 0)]
        # Join octets to form the subnet mask
        subnet_mask_str = '.'.join(map(str, subnet_octets))
        # Return subnet_mask_str
        return subnet_mask_str

    def get_cidr_network_address(self, subnet_mask_str, cidr):
        # Classify IP address
        classification = self.classify_ip_address()
        # Convert IP address and subnet mask to lists of integers
        ip_octets = [int(octet) for octet in self.ip_address.split('.')]
        subnet_octets = [int(octet) for octet in subnet_mask_str.split('.')]
        # Perform bitwise AND operation for each octet
        network_octets = [ip_octets[i] & subnet_octets[i] for i in range(4)]
        # Join octets to form the network address
        network_address = '.'.join(map(str, network_octets))
        # Calculate binary 
        binary_ip_address = ''.join(format(octet, '08b') for octet in ip_octets)
        binary_subnet_mask = ''.join(format(octet, '08b') for octet in subnet_octets)
        binary_network_address = ''.join(format(octet, '08b') for octet in network_octets)
        # Calculate broadcast network
        broadcast_address = self.get_broadcast_address(subnet_mask_str)
        # Return network_address
        print(f"\nIPv4 Address: \t\t {self.ip_address}")
        print(f"IP Class: \t\t {classification['IP Class']}")
        print(f"IP Type: \t\t {classification['IP Type']}")
        print(f"CIDR Notation: \t\t /{cidr}")
        print(f"Subnet Mask: \t\t {subnet_mask_str}")
        print(f"Network Address: \t {network_address}")
        print(f"Broadcast Address: \t {broadcast_address}\n")
        
        print(f"Binary IPv4 Address: \t {binary_ip_address}")
        print(f"Binary Subnet Mask: \t {binary_subnet_mask}")
        print(f"Binary Network Address:  {binary_network_address}")

    def main(self, cidr, subnet_mask):
        if subnet_mask and cidr:
            print("Error: Provide either --subnet or --cidr, not both.")
        elif subnet_mask:
            cidr = self.subnet_mask_to_cidr(subnet_mask)
            self.get_subnet_network_address(subnet_mask, cidr)
        elif cidr:
            subnet_mask = self.cidr_to_subnet_mask(cidr)
            self.get_cidr_network_address(subnet_mask, cidr)
        else:
            print("Error: Provide either --subnet or --cidr.")
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find Network Address from IP Address")  
    parser.add_argument("ip_address", type=str, help="IPv4 Address (e.g., 175.8.110.9)")
    parser.add_argument("-c", "--cidr", type=str, help="CIDR notation of subnet address (e.g., 24)")
    parser.add_argument("-s", "--subnet_mask", type=str, help="Subnet address (e.g., 255.255.255.0)")
    
    args = parser.parse_args()
    
    ipaddress = IPv4Address(args.ip_address)
    ipaddress.main(args.cidr, args.subnet_mask)
