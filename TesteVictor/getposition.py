import pyautogui
import keyboard
from tkinter import *
from tkinter import messagebox
import queue

class PopupApp:
    def __init__(self):
        # Inicializa a janela principal
        self.root = Tk()
        self.root.withdraw()
        
        # Desativa o beep padrão do Windows
        self.root.bell = lambda: None
        
        # Configura a janela para ficar sempre no topo
        self.root.attributes('-topmost', True)
        
        # Inicializa a fila de mensagens
        self.queue = queue.Queue()
        self.check_queue()
    
    def check_queue(self):
        try:
            while True:
                message = self.queue.get_nowait()
                if message == "show_coordinates":
                    # Obtém as coordenadas do mouse
                    x, y = pyautogui.position()
                    # Exibe um pop-up com as coordenadas
                    self.root.deiconify()
                    self.root.withdraw()
                    messagebox.showinfo("Coordenadas do Mouse", f"Posição atual do mouse: x={x}, y={y}")
        except queue.Empty:
            pass
        finally:
            self.root.after(100, self.check_queue)
    
    def show_coordinates(self):
        self.queue.put("show_coordinates")
    
    def start(self):
        self.root.mainloop()

def on_press(event, app):
    if event.name == '4':  # Verifica se a tecla pressionada é '4'
        app.show_coordinates()

def main():
    app = PopupApp()
    
    # Registra o callback para quando uma tecla for pressionada
    keyboard.on_press(lambda e: on_press(e, app))
    
    print("Programa iniciado! Pressione '4' para exibir as coordenadas do mouse.")
    print("Pressione Ctrl+C no terminal para encerrar o programa.")
    
    # Inicia o loop principal
    app.start()

if __name__ == "__main__":
    main()
