import pyautogui
import time

# Tempo para posicionar o mouse manualmente antes de iniciar
print("Posicione o mouse. O script iniciará em 5 segundos...")
time.sleep(5)

# Move o mouse para a posição (x=100, y=100)
pyautogui.moveTo(100, 100, duration=1)  # duration é o tempo em segundos para mover

# Clica com o botão esquerdo
pyautogui.click()

print("Mouse movido e clicado com sucesso!")
