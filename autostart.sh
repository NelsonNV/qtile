#!/bin/sh

# systray volume
# volumeicon &
# network manager
# nm-applet &
#fondo de pantalla
python3 $HOME/.config/qtile/wallpaper.py fondorandom &
#ajustes de volumen
#activar opacity
#compton -r 12 -o 0.00 -l 15 -t 15 -I 0.028 -O 0.03 -D 3 -c -f -C -F -G -b &

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 & # Agente de autenticación gráfica

xrandr --output DVI-D-0 --off --output HDMI-0 --mode 1440x900 --pos 1920x90 --rotate normal --output DP-0 --mode 1920x1080 --pos 0x0 --rotate normal --output DP-1 --off &

picom &
# ejecutar key mouse
setxkbmap -option keypad:pointerkeys &
# ejecutar telegram
telegram-desktop -startintray %u &

