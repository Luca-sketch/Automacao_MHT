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
                self.queue.get_nowait()
                # Força a janela a ficar em primeiro plano
                self.root.deiconify()
                self.root.withdraw()
                messagebox.showinfo("Tecla Detectada", "Você digitou a tecla 'a'!")
        except queue.Empty:
            pass
        finally:
            self.root.after(100, self.check_queue)
    
    def show_popup(self):
        self.queue.put("show")
    
    def start(self):
        self.root.mainloop()

def on_press(event, app):
    if event.name == 'a':
        app.show_popup()

def main():
    app = PopupApp()
    
    # Registra o callback para quando uma tecla for pressionada
    keyboard.on_press(lambda e: on_press(e, app))
    
    print("Programa iniciado! Pressione 'a' em qualquer lugar para ver o pop-up.")
    print("Pressione Ctrl+C no terminal para encerrar o programa.")
    
    # Inicia o loop principal
    app.start()

if __name__ == "__main__":
    main()