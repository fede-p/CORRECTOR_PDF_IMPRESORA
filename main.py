import ROTAR_DESPLAZAR
import tkinter
import json

def cargar_json():
    _dic = {}

    try:
        file = open("config.json")
        _dic = json.load(file)
        file.close()
    except Exception as e:
        _dic = {"CORRECCION_EN_PIXELES_VERTICAL": 0, "CORRECCION_EN_PIXELES_HORIZONTAL": 0, "ROTAR": False }
        guardar_json(_dic)

    return _dic

def guardar_json(_dict):
    file = open("config.json", "w")
    file.write(json.dumps(_dict))
    file.close()

def cargar_files(texto_vertical, texto_horizontal, texto_rotar, _config):
    _texto_vertical = int(texto_vertical.get(1.0, "end"))
    _texto_horizontal = int(texto_horizontal.get(1.0, "end"))
    _angulo = 0
    _rotar = False
    if texto_rotar.get() == 1:
        _rotar = True
        _angulo = 180

    _config["CORRECCION_EN_PIXELES_VERTICAL"] = _texto_vertical
    _config["CORRECCION_EN_PIXELES_HORIZONTAL"] = _texto_horizontal
    _config["ROTAR"] = _rotar
    guardar_json(_config)

    ROTAR_DESPLAZAR.CORRECCION_EN_PIXELES_VERTICAL = _texto_vertical
    ROTAR_DESPLAZAR.CORRECCION_EN_PIXELES_HORIZONTAL = _texto_horizontal
    if _rotar:
        ROTAR_DESPLAZAR.ANGULO = 180
    ROTAR_DESPLAZAR.procesar(_texto_vertical, _texto_horizontal, _angulo)


def main():

    _config =  cargar_json()

    window = tkinter.Tk()
    window.geometry('230x160')
    window.title("Rotar y desplazar")
    window.resizable(0, 0)

    frame_botones = tkinter.Frame(window)

    label_1 = tkinter.Label(frame_botones, text="CORRECCION_EN_PIXELES_VERTICAL")
    label_1.grid(column=0, row=0)
    texto_vertical = tkinter.Text(frame_botones, width=20, height=1)
    texto_vertical.insert(tkinter.END, _config["CORRECCION_EN_PIXELES_VERTICAL"])
    texto_vertical.grid(column=0, row=1)

    label_2 = tkinter.Label(frame_botones, text="CORRECCION_EN_PIXELES_HORIZONTAL")
    label_2.grid(column=0, row=2)
    texto_horizontal = tkinter.Text(frame_botones, width=20, height=1)
    texto_horizontal.insert(tkinter.END, _config["CORRECCION_EN_PIXELES_HORIZONTAL"])
    texto_horizontal.grid(column=0, row=3)

    label_3 = tkinter.Label(frame_botones, text="ROTAR 180")
    label_3.grid(column=0, row=4)
    var_check = tkinter.IntVar()
    texto_rotar = tkinter.Checkbutton(frame_botones, text="", onvalue=1, offvalue=0, variable=var_check)
    if _config["ROTAR"]:
        texto_rotar.select()
    
    texto_rotar.grid(column=0, row=5)

    

    tkinter.Button(frame_botones, text="Procesar", command=lambda: cargar_files(texto_vertical, texto_horizontal, var_check, _config)).grid(column=0, row=6)

    tkinter.Frame(frame_botones)
    frame_botones.grid(column=0, row=0)
    
    

    window.mainloop()



main()
























