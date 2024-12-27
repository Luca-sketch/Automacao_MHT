import keyboard
import pyautogui
import threading
import tkinter as tk
from tkinter import messagebox

class MouseAutomation:
    def __init__(self):
        # Inicializa o programa
        self.running = True

        # Configura a posição do mouse
        self.mouse_x, self.mouse_y = self.get_mouse_position()

        # Configura a janela de controle
        self.setup_gui()

        # Inicia a thread de teclado
        self.start_keyboard_listener()

    def get_mouse_position(self):
        # Mostra instruções para capturar a posição
        messagebox.showinfo("Posicionar Mouse", "Você tem 5 segundos para posicionar o mouse.")
        pyautogui.sleep(5)
        return pyautogui.position()

    def setup_gui(self):
        # Configura a interface gráfica
        self.root = tk.Tk()
        self.root.title("Automação de Clique")
        self.root.geometry("300x150")

        # Mensagem de status
        tk.Label(self.root, text="Pressione ']' para clicar.", font=("Arial", 12)).pack(pady=10)
        tk.Label(self.root, text="Posição capturada: X={}, Y={}".format(self.mouse_x, self.mouse_y)).pack(pady=5)

        # Botão para sair
        tk.Button(self.root, text="Fechar Programa", command=self.stop_program, bg="red", fg="white").pack(pady=10)

        # Evento para fechar a janela
        self.root.protocol("WM_DELETE_WINDOW", self.stop_program)

    def start_keyboard_listener(self):
        # Thread para evitar travamento do GUI
        threading.Thread(target=self.keyboard_listener, daemon=True).start()

    def keyboard_listener(self):
        while self.running:
            if keyboard.is_pressed(']'):  # Tecla para disparar a ação
                pyautogui.moveTo(self.mouse_x, self.mouse_y, duration=0.2)
                pyautogui.click()
                pyautogui.sleep(0.5)  # Pequeno atraso para evitar múltiplos cliques

    def stop_program(self):
        # Para o programa
        self.running = False
        self.root.quit()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = MouseAutomation()
    app.run()
