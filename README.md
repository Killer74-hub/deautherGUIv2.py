WiFi Network Scanner and Deauthenticator

THIS SCRIPT REQUIRES ROOT/SUDO

This is a simple WiFi network scanner and deauthentication tool built using Python and airodump-ng/aireplay-ng tools. The script uses tkinter for the graphical user interface (GUI) to allow users to scan for WiFi networks and perform deauthentication attacks on selected or all networks.
Features:

    Scan Wi-Fi Networks: Continuously scans for available Wi-Fi networks and displays the information (BSSID, ESSID, Channel, Signal Strength) in a list.
    Deauthenticate Networks: Deauthenticate selected networks or all networks in the range.
    Channel Hopping: Scans and attacks networks across multiple channels.
    Easy-to-use GUI: Provides a simple interface to interact with the Wi-Fi network scanning and deauthentication tools.

Requirements:

To use this tool, you need to have the following installed:

    Python 3.x
    airodump-ng, aireplay-ng (part of the Aircrack-ng suite)
    tkinter for the GUI
    iw (for channel switching)

Ensure that your wireless adapter supports monitor mode and is compatible with the Aircrack-ng suite.
Setup Instructions:

    Install dependencies (Aircrack-ng, Python3, and Tkinter).

    On Ubuntu/Debian-based systems:

sudo apt update
sudo apt install aircrack-ng python3 python3-tk iw

Clone the repository:

git clone https://github.com/Killer74-hub/deautherGUIv2.py/
cd deautherGUIv2
Put your Device into monitor mode:
sudo airmon-ng check kill
sudo airmon-ng start (DEVICE)


Run the script:

    sudo python3 script.py

    Make sure to run the script with sudo as it requires elevated privileges to interact with the wireless interface and use tools like airodump-ng and aireplay-ng. After the scan disable Monitor mode with "sudo airmon-ng start (DEVICE)" and start the NetworkManager with: "sudo airmon-ng

Usage:

    START Scan: Starts scanning for available Wi-Fi networks.
    STOP Scan: Stops the ongoing Wi-Fi network scan.
    Deauth Selected: Deauthenticates the selected Wi-Fi network(s).
    Deauth All: Deauthenticates all available networks in the range.
    Stop Deauth: Stops the ongoing deauthentication process (please see the note below regarding a limitation).

Known Issues:

    Stop Deauth Button: The "Stop Deauth" button currently does not stop the deauthentication process completely. This is due to how the aireplay-ng process is handled in the background. A fix for this issue is needed to properly terminate all running aireplay-ng processes when the button is pressed. This is a known limitation that will be addressed in a future update.
    Help is appreciated.
    
License:

This project is licensed under the MIT License - see the LICENSE file for details.
Disclaimer:

This tool is intended for educational purposes only. Using this tool to interfere with networks that you do not own or have explicit permission to test is illegal in many countries. Please ensure that you have permission before using it.
