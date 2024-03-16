import re

class validIPv4Address:
    def __init__(self, ipaddress_list):
        self.iplist = ipaddress_list
        
    def validate_ip(self):
        ipv4_pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
        results = []
        for ip in self.iplist:
            if re.match(ipv4_pattern, ip):
                results.append(ip)
            else:
                results.append(-1)
        return results

    def classify_ip(self, ipaddress_list):
        results = []
        for ip in ipaddress_list:
            num = str(ip).split('.')
            first = int(num[0])
            if first >= 0 and first < 128:
                results.append(1)
            elif first >= 128 and first < 192:
                results.append(2)
            elif first >=192 and first < 224:
                results.append(3)
            elif first >=224 and first < 240:
                results.append(4)
            elif first >=240 and first < 256:
                results.append(5)
            else: 
                results.append(-1)
        return results
            

    def validate_and_classify_ip(self):
        valid = self.validate_ip()
        results = self.classify_ip(valid)
        return results


# ip_address_list = ["212.0.0.0", "133.0.1.1", "127.233.258.1", "4.4.4", "5.66.222.90", "224.99.44.1", "240.3.2.2"]

# ipclassify = validIPv4Address(ip_address_list)
# ipclassify.validate_and_classify_ip()

# Output: [3, 2, -1, -1, 1, 4, 5]

