# IP-Subnet-Calculator

<br>

![GitHub last commit](https://img.shields.io/github/last-commit/kariemoorman/IP-Subnet-Calculator)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/kariemoorman/IP-Subnet-Calculator)
![GitHub stars](https://img.shields.io/github/stars/kariemoorman/IP-Subnet-Calculator?style=social)

---

### 🛡️ About

IP Subnet Calculator returns a variety of information regarding Internet Protocol version 4 (IPv4) networks (e.g., IP class and type, CIDR notation, subnet mask, network address and broadcast address). 

---

### 🌟 Examples 

### IPv4 
- #### IPv4 Address & Subnet Mask 

```
## Input Values
## ipv4_address = "192.168.110.10"
## subnet_mask = "255.255.248.0"

## Python Command: 
python ipv4address.py 192.168.110.10 -s 255.255.248.0

## Intended Output: 
IPv4 Address: 192.168.110.10
IP Class: C
IP Type: Private
CIDR Notation: /21
Subnet Mask: 255.255.248.0
Network Address: 192.168.104.0
Broadcast Address: 192.168.111.255
```

- #### IPv4 Address & CIDR

```
## Input Values
## ipv4_address = "175.8.110.9"
## cidr_notation = "21"

# Python Command: 
python ipv4address.py 175.8.110.9 -c 21

IPv4 Address: 175.8.110.9
IP Class: B
IP Type: Public
CIDR Notation: /21
Subnet Mask: 255.255.248.0
Network Address: 175.8.104.0
Broadcast Address: 175.8.111.255
```
