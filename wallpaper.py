import os
import random


def fondorandom():
    '''funcion creada para generar fondos aleatorio'''
    home = os.path.expanduser("~")
    direccion = f"{home}/.config/qtile/wallpaper"
    fondos = os.listdir(direccion)
    try:
        fondos.remove('.git')
    except:
        pass
    random.shuffle(fondos)
    os.system(f"feh --no-fehbg --bg-scale { direccion }/{ fondos[ random.randrange( 0 , len(fondos) ) ] }")

if __name__ == "__main__":
    fondorandom()
