import keyboard
from tkinter import *
from tkinter import messagebox
import queue
import pyautogui
import time

class AutomationApp:
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
        
        # Captura a posição inicial do mouse
        print("Posicione o mouse onde deseja que ele clique.")
        print("Aguardando 5 segundos...")
        time.sleep(5)
        self.mouse_x, self.mouse_y = pyautogui.position()
        print(f"Posição capturada: X={self.mouse_x}, Y={self.mouse_y}")
        
        # Inicia a verificação da fila
        self.check_queue()
    
    def check_queue(self):
        try:
            while True:
                action = self.queue.get_nowait()
                if action == "click":
                    # Move o mouse e clica
                    pyautogui.moveTo(self.mouse_x, self.mouse_y, duration=0.5)
                    pyautogui.click()
                    
                    # Mostra o pop-up
                    self.root.deiconify()
                    self.root.withdraw()
                    messagebox.showinfo("Ação Executada", f"Mouse movido para ({self.mouse_x}, {self.mouse_y}) e clicado!")
        except queue.Empty:
            pass
        finally:
            self.root.after(100, self.check_queue)
    
    def trigger_action(self):
        self.queue.put("click")
    
    def start(self):
        print("\nPrograma iniciado!")
    
    # Comentario do local clicado
        print("Pressione 'a' em qualquer lugar para mover o mouse e clicar.")
        print("Pressione Ctrl+C no terminal para encerrar o programa.")
        self.root.mainloop()

    # Definindo o caracter
def on_press(event, app):
    if event.name == '-':
        app.trigger_action()

def main():
    # Configurações de segurança do PyAutoGUI
    pyautogui.FAILSAFE = True  # Move o mouse para o canto superior esquerdo para parar
    
    app = AutomationApp()
    
    # Registra o callback para quando uma tecla for pressionada
    keyboard.on_press(lambda e: on_press(e, app))
    
    # Inicia o loop principal
    app.start()

if __name__ == "__main__":
    main()