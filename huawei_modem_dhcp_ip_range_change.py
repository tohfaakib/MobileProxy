import requests
from bs4 import BeautifulSoup


def change_ip_address():
    a = input("Current IP address value? >192.168.?.1 (default:192.168.8.1): ") or '8'
    sModemIp = f"192.168.{a}.1"
    b = input("New ip address range value? 192.168.?.1: ") or '1'

    sXmlData = f'''<?xml version="1.0" encoding="UTF-8"?>
<request>
<DhcpIPAddress>192.168.{b}.1</DhcpIPAddress>
<DhcpLanNetmask>255.255.255.0</DhcpLanNetmask>
<DhcpStatus>1</DhcpStatus>
<DhcpStartIPAddress>192.168.{b}.100</DhcpStartIPAddress>
<DhcpEndIPAddress>192.168.{b}.200</DhcpEndIPAddress>
<DhcpLeaseTime>86400</DhcpLeaseTime>
<DnsStatus>1</DnsStatus>
<PrimaryDns>192.168.{b}.1</PrimaryDns>
<SecondaryDns>192.168.{b}.1</SecondaryDns>
</request>'''

    ses_tok_response = requests.get(f"http://{sModemIp}/api/webserver/SesTokInfo")
    if ses_tok_response.status_code == 200:
        ses_tok_soup = BeautifulSoup(ses_tok_response.content, 'lxml')
        ses_info = ses_tok_soup.find("sesinfo").text
        tok_info = ses_tok_soup.find("tokinfo").text

        print(ses_info)
        print(tok_info)

        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "__RequestVerificationToken": tok_info,
            "Cookie": ses_info,
            "Host": "192.168.8.1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 14541.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        }

        dhcp_settings_response = requests.post(f"http://{sModemIp}/api/dhcp/settings", headers=headers, data=sXmlData)
        print(dhcp_settings_response.text)
        if dhcp_settings_response.status_code == 200:
            print("Finished the change. Your device will now show up under the newly applied settings")
        else:
            print("Failed to change IP settings.")


if __name__ == "__main__":
    change_ip_address()
