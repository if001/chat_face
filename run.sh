export DISPLAY=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2}'):0.0
# fcitx &\
python main.py
# pkill fcitx
