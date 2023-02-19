import subprocess 
import os 
from mediafiredl import MediafireDL as MF 
from time import sleep 

urls = ["http://www.mediafire.com/file/d5050f6c1xk8ikl/MATRIX.wmv/file", 
"https://www.mediafire.com/file/8mfwhasojxr261u/Oxygen_14_Matrix_Green.tar/file"]
MF.BulkDownload(urls)
sleep(4)
os.system("mkdir ~/.icons")
os.system("mkdir ~/.themes")
os.system("mkdir ~/.videos")
os.system("mkdir ~/.documents")

subprocess.call(["sudo", "apt", "install", "gnome-tweaks", "-y"])
subprocess.call(["sudo", "gsettings", "set", "org.gnome.desktop.interface", "gtk-theme", "Yaru-Viridan-Dark"])
subprocess.call(["curl", "https://ocs-dl.fra1.cdn.digitaloceanspaces.com/data/files/1509460911/Oxygen%2014%20Matrix%20Green.tar.gz?response-content-disposition=attachment%3B%2520Oxygen%2014%20Matrix%20Green.tar.gz&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=RWJAQUNCHT7V2NCLZ2AL%2F20230219%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230219T110335Z&X-Amz-SignedHeaders=host&X-Amz-Expires=60&X-Amz-Signature=9f182dc076c50a42acc0d0e9230c8e13db59fa041468f614cb892a86f8105cfd", "--output", "Oxygen 14 Matrix Green.tar"])
subprocess.call(["tar", "xvzf", "Oxygen 14 Matrix Green.tar"])
subprocess.call(["sudo", "cp", "Oxygen 14 Matrix Green", "~/.icons"])
subprocess.call(["sudo", "gsettings", "set", "org.gnome.desktop.interface", "cursor-theme", "Oxygen 14 Matrix Green"])
subprocess.call(["sudo", "apt", "install", "cmatrix", "-y"])
subprocess.call(["sudo", "cp", "-R", "MATRIX.wmv", "~/.videos"])
subprocess.call(["sudo", "apt", "install", "git", "-y"])
subprocess.call(["git", "clone", "https://github.com/ghostlexly/gpu-video-wallpaper.git"])
subprocess.call(["curl", "https://www.mediafire.com/file/y7ey8whbifjuaie/xwinwrap/file", "--output", "xwinwrap"])
subprocess.call(["cp", "-R", "xwinwrap", "gpu-video-wallpaper"])
subprocess.call(["cd", "gpu-video-wallpaper"])
subprocess.call(["sudo", "./install.sh"])
subprocess.call(["cd", ". ."])
subprocess.call(["cp", "-R MATRIX.wmv", "~/.videos"])
subprocess.call(["sudo", "sh", "video-wallpaper.sh", "--startup", "~/.videos/MATRIX.wmv"])
subprocess.call(["sudo", "echo export PS1=\e[0;32[\u@\h \W]\$ \e[m ", ">>", "~/.bashrc"])
subprocess.call(["sudo", "gsettings", "set", "org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:$(gsettings get org.gnome.Terminal.ProfilesList", "default", "|", "awk", "-F \' '{print $2}')/", "background-color", "#000000"])
