import sys
import os
import os.path
import subprocess
import hashlib
import base64
from io import BytesIO
import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image
from tkinter import messagebox

script_dir = os.path.dirname(os.path.realpath(sys.argv[0]))

bin_dir = os.path.join(script_dir, "bin")

xrshell_path = os.path.join(script_dir, "bin", "OpenXR", "1.apk")
xrruntime_path = os.path.join(script_dir, "bin", "OpenXR", "2.apk")
mrservice_path = os.path.join(script_dir, "bin", "OpenXR", "3.apk")
seethr_path = os.path.join(script_dir, "bin", "OpenXR", "4.apk")
guardian_path = os.path.join(script_dir, "bin", "OpenXR", "5.apk")

def install():
    try:
        subprocess.run(["adb", "install", xrshell_path], stderr=subprocess.STDOUT, text=True)
        subprocess.run(["adb", "install", xrruntime_path], stderr=subprocess.STDOUT, text=True)
        subprocess.run(["adb", "install", mrservice_path], stderr=subprocess.STDOUT, text=True)
        subprocess.run(["adb", "install", seethr_path], stderr=subprocess.STDOUT, text=True)
        subprocess.run(["adb", "install", guardian_path], stderr=subprocess.STDOUT, text=True)
        subprocess.run(["adb", "reboot"], stderr=subprocess.STDOUT, text=True)
        messagebox.showinfo("Success", "OpenXR_Fix successfully installed")
    except Exception as e:
        print(f"Fehler: {e}")

def uninstall():
    try:
        subprocess.run(["adb", "uninstall", "com.picoxr.xrshell"], stderr=subprocess.STDOUT, text=True)
        subprocess.run(["adb", "uninstall", "com.pico.xr.openxr_runtime"], stderr=subprocess.STDOUT, text=True)
        subprocess.run(["adb", "uninstall", "com.pico.mrservice"], stderr=subprocess.STDOUT, text=True)
        subprocess.run(["adb", "uninstall", "com.pvr.seethrough.setting"], stderr=subprocess.STDOUT, text=True)
        subprocess.run(["adb", "uninstall", "com.pico.guardian"], stderr=subprocess.STDOUT, text=True)
        subprocess.run(["adb", "reboot"], stderr=subprocess.STDOUT, text=True)
        messagebox.showinfo("Success", "OpenXR_Fix successfully uninstalled")
    except Exception as e:
        print(f"Fehler: {e}")

def create_gui():
    window = tk.Tk()
    window.title("OpenXR Fixer - Made by FallenAngel / PicoPiracy Team")
    window.geometry("300x300") 

    top_frame = tk.Frame(window)
    top_frame.pack()

    middle_frame = tk.Frame(window)
    middle_frame.pack()

    bottom_frame = tk.Frame(window)
    bottom_frame.pack()

    man_output_label = tk.Label(top_frame, text="Fix to getting some")
    man_output_label.pack(pady=5)

    adb_output_label = tk.Label(top_frame, text="new games running on 5.4.0")
    adb_output_label.pack(pady=5)

    adb_output_label = tk.Label(top_frame, text="")
    adb_output_label.pack(pady=20)

    start_button = tk.Button(middle_frame, text="Install", command=install)
    start_button.pack(side="left", padx=10, pady=20)

    end_button = tk.Button(bottom_frame, text="Uninstall", command=uninstall)
    end_button.pack(side="left", padx=10)

    window.mainloop()

create_gui()
