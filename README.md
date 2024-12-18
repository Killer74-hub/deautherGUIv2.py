WiFi Network Scanner and Deauthenticator for 2.4GHz and 5GHz

This tool is a simple WiFi network scanner and deauthentication tool built using Python along with airodump-ng/aireplay-ng tools. It uses tkinter for the graphical user interface (GUI) to allow users to scan for WiFi networks and perform deauthentication attacks on selected or all networks.

Features:

Scan Wi-Fi Networks: Continuously scans for available Wi-Fi networks and displays the information (BSSID, ESSID, Channel, Signal Strength) in a list.

Deauthenticate Networks: Deauthenticates selected networks or all networks in range.

Channel Hopping: Scans and attacks networks across multiple channels.

Easy-to-use GUI: Simple interface to interact with Wi-Fi network scanning and deauthentication tools.

Requirements:

To use this tool, you need the following installed:

    Python 3.x

    airodump-ng, aireplay-ng (part of the Aircrack-ng suite)

    tkinter (for the GUI)

    iw (for channel switching)

    Ensure that your wireless adapter supports monitor mode and is compatible with the Aircrack-ng suite.

Setup Instructions:

    Install Dependencies (Aircrack-ng, Python3, and Tkinter)

On Ubuntu/Debian-based systems, run the following commands:

    sudo apt update
    sudo apt install aircrack-ng python3 python3-tk iw

Clone the Repository:

    git clone https://github.com/Killer74-hub/deautherGUIv2.py/
    cd deautherGUIv2

Put Your Device Into Monitor Mode:

    sudo airmon-ng check kill
    sudo airmon-ng start (DEVICE)

Run the Script:

    sudo python3 script.py

Note: Make sure to run the script with sudo as it requires elevated privileges to interact with the wireless interface and use tools like airodump-ng and aireplay-ng.

After the scan, disable monitor mode:

    sudo airmon-ng stop (DEVICE)
    
And Start the NetworkManager:

    sudo systemctl start NetworkManager

Usage:

START Scan: Starts scanning for available Wi-Fi networks.

STOP Scan: Stops the ongoing Wi-Fi network scan.

Deauth Selected: Deauthenticates the selected Wi-Fi network(s).

Deauth All: Deauthenticates all available networks in range.

Stop Deauth: Stops the ongoing deauthentication process.
Note: The "Stop Deauth" button currently does not fully stop the deauthentication process due to limitations in how the aireplay-ng process is handled in the background. A fix for this issue is needed for proper termination of running processes.

Known Issues:

Stop Deauth Button: The "Stop Deauth" button does not fully stop the deauthentication process. This is because of how aireplay-ng processes are managed in the background. A fix for this issue is planned for a future update.

License:

No License. This Project is Opensource and can be edited by anyone. I would appreciate help.

Disclaimer:

This tool is intended for educational purposes only. Using this tool to interfere with networks that you do not own or do not have explicit permission to test is illegal in many countries. Please ensure you have permission before using it.
