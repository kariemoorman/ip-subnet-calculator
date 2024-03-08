# IP-Subnet-Calculator

<p align='center'>
  <img src='https://github.com/kariemoorman/IP-Subnet-Calculator/blob/main/ipv4networkaddress.png' alt='ipv4-net'>
</p>

<br>

![GitHub last commit](https://img.shields.io/github/last-commit/kariemoorman/IP-Subnet-Calculator)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/kariemoorman/IP-Subnet-Calculator)
![GitHub stars](https://img.shields.io/github/stars/kariemoorman/IP-Subnet-Calculator?style=social)

---

### 🛡️ About

IP Subnet Calculator returns a variety of information regarding Internet Protocol version 4 (IPv4) networks (e.g., IP class and type, CIDR notation, subnet mask, network address and broadcast address) and Internet Protocol version 6 (IPv6) networks (e.g., IP type, CIDR notation, network address), along with binary notation.

---

### 🚀 Installation & Use

#### Python Package Requirements

```
argparse, re
```

#### Installation 

- Clone or download .zip of `ip-subnet-calculator` python package.
```
git clone https://github.com/jestlandia/IP-Subnet-Calculator.git
```

- Create a virtual environment inside the `IP-Subnet-Calculator` directory, and activate virtual environment.
```
cd ip-subnet-calculator && python -m venv .venv && source .venv/bin/activate;
```

- Install package dependencies. 
```
pip install regex argparse;
```

#### Use 
- Execute `ip-subnet-calculator` program.
```
######----- IPv4 Address -----######

python ipv4address.py <ipv4_address> --cidr <int>
python ipv4address.py <ipv4_address> --subnet_mask <subnet_address>


######----- IPv6 Address -----######

python ipv6address.py <ipv6_address> --cidr <int>
```

---

### 🌟 Example Use Cases 

### IPv4 
- #### IPv4 Address with Subnet Mask Flag
```
## Input Values:

ipv4_address = "192.168.110.10"
subnet_mask = "255.255.248.0"
```
```
## Python Command:

python ipv4address.py 192.168.110.10 -s 255.255.248.0
```
```
## Intended Output:

IPv4 Address: 192.168.110.10
IP Class: C
IP Type: Private
CIDR Notation: /21
Subnet Mask: 255.255.248.0
Network Address: 192.168.104.0
Broadcast Address: 192.168.111.255

Binary IPv4 Address:     11000000.10101000.01101110.00001010
Binary Subnet Mask:      11111111.11111111.11111000.00000000
Binary Network Address:  11000000.10101000.01101000.00000000
```

- #### IPv4 Address with CIDR Flag
```
## Input Values:

ipv4_address = "175.8.110.9"
cidr_notation = "21"
```
```
## Python Command:

python ipv4address.py 175.8.110.9 -c 21
```
```
## Intended Output:

IPv4 Address: 175.8.110.9
IP Class: B
IP Type: Public
CIDR Notation: /21
Subnet Mask: 255.255.248.0
Network Address: 175.8.104.0
Broadcast Address: 175.8.111.255

Binary IPv4 Address:     10101111.00001000.01101110.00001001
Binary Subnet Mask:      11111111.11111111.11111000.00000000
Binary Network Address:  10101111.00001000.01101000.00000000
```

### IPv6 

- #### IPv6 Address & CIDR Flag
```
## Input Values:

ipv6_address = "2001:0db8:2231:aaec:0000:0000:4a4a:2100"
cidr_notation = "64"
```

```
## Python Command:

python ipv6address.py 2001:0db8:2231:aaec:0000:0000:4a4a:2100 --cidr 64
```
```
## Intended Output:

IPv6 Address: 2001:0db8:2231:aaec:0000:0000:4a4a:2100
IP Type: Public
CIDR Notation: /64
Network Address: 2001:0db8:2231:aaec:0000

Binary IPv6 Address: 0010.0000.0000.0001:0000.1101.1011.1000:0010.0010.0011.0001:1010.1010.1110.1100:0000.0000.0000.0000:0000.0000.0000.0000:0100.1010.0100.1010:0010.0001.0000.0000
Binary Subnet Mask: 1111.1111.1111.1111:1111.1111.1111.1111:1111.1111.1111.1111:1111.1111.1111.1111:1111.1111.1111.1111:1111.1111.1111.1111:1111.1111.1111.1111:1111.1111.1111.1111:0000.0000.0000.0000:0000.0000.0000.0000:0000.0000.0000.0000:0000.0000.0000.0000
Binary Network Address: 0010.0000.0000.0001:0000.1101.1011.1000:0010.0010.0011.0001:1010.1010.1110.1100:0000.0000.0000.0000
```
