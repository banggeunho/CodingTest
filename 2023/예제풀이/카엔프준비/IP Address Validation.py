class Solution(object):
    def validIPAddress(self, queryIP):
        """
        :type queryIP: str
        :rtype: str
        """

        def checkV4(queryIP):
            ipSplit = queryIP.split('.')
            for ip in ipSplit:
                if len(ip) == 0 or len(ip) > 3 or ip.isdigit() == False or (ip[0] == '0' and len(ip) != 1) or int(
                        ip) > 255:
                    return 'Neither'
            return 'IPv4'

        def checkV6(queryIP):
            ipSplit = queryIP.split(':')
            for ip in ipSplit:
                if len(ip) == 0 or len(ip) > 4:
                    return 'Neither'
                for content in ip:
                    if content.lower() not in '0123456789abcdef':
                        return 'Neither'
            return 'IPv6'

        if len(queryIP.split('.')) == 4:
            return checkV4(queryIP)
        elif len(queryIP.split(':')) == 8:
            return checkV6(queryIP)
        return 'Neither'