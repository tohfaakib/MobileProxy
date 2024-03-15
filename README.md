# Huawei USB Stick Modem IP Configuration Tool

## Purpose

This tool is designed for configuring the IP address of Huawei USB Stick Modems. It is particularly useful when using multiple Huawei USB stick modems on the same device to avoid IP address conflicts. This script changes the modem's LAN IP address range, allowing each modem to operate on a different subnet.

## Tested Devices

This script has been tested with the following Huawei USB Stick Modems:

- Huawei E3131
- Huawei E3372
- Huawei E3531


## Usage

To use the script, run it from the command line or an IDE. The script will prompt you for the current IP address and the new IP address range you wish to set for your modem. The default current IP address is `192.168.8.1`. If you wish to use the default, simply press Enter.


## Customization

Depending on the modem model and firmware version, you might need to adjust the payload. You can find the necessary details by accessing the modem's API endpoints through a web browser and inspecting the network tab in the developer tools.

## Notes

- Ensure your computer is directly connected to the modem you wish to configure.
- Use this script responsibly and only on devices you own or are authorized to manage.
- If you set authorization you should adjust the script accordingly.
- Based on device model you might need to adjust the payloads and headers. You can find those in browser's dev tool.

## Disclaimer

This tool is provided as-is without any warranty. The author is not responsible for any damage or loss resulting from the use of this script. Use it at your own risk.

## Credit

Made this python script with some adjustament from a javascript code I found here, https://mobileproxy.space/en/pages/configuring-the-e3372h-320-modem-to-work-with-mobile-proxies.html
