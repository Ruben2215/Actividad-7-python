import tkinter as tk
import serial

port='COM5'
baudrate =9600
ser = serial.Serial(port, baudrate )

def encender_led():
    ser.write(b'b')
    print("led encendido")
    
def apagar_led():
    ser.write(b'a')
    print("led apagado")
    
ventana = tk.Tk()
ventana.geometry("250x250")
ventana.title("Control de led")

bnEncender = tk.Button(ventana, text="Encender led", command=encender_led)
bnEncender.pack(pady=10)

bnApagar=tk.Button(ventana, text="Apagar led", command=apagar_led)
bnApagar.pack(pady=10)

ventana.mainloop()

ser.close()
    