from tkinter import LabelFrame
import pyautogui
from time import sleep
# from pynput import keyboard

pyautogui.PAUSE = 0.5

# DEIXANDO TUDO PRONTO

# ABRIR WPP
# pyautogui.press('win')
# pyautogui.write('whatsapp', interval=0.2)
# pyautogui.press('enter')

# # ABRIR E-MAIL
# pyautogui.press('win')
# pyautogui.write('thunderbird', interval=0.2)
# pyautogui.press('enter')

# ABRIR NAVEGADOR / ACESSAR YOUTUBE
pyautogui.press('win')
pyautogui.write('firefox', interval=0.1)
pyautogui.click(482, 372, 1, button='left')

pyautogui.sleep(2)
pergunta = pyautogui.confirm('Olá Rany, posso continuar?', buttons=['Sim','Não'])
print(pergunta)
if pergunta == 'Sim':
    pyautogui.write('youtu.be')
    pyautogui.press('enter')
    pyautogui.sleep(10)
    pyautogui.click(1266, 143, 1, interval=0.3, button='left')# clica para acessar o login.
else: 
    pyautogui.PAUSE


# if pyautogui.press (['enter','enter']):
#         pyautogui.alert('Acessando conta...')
# else:
#     pergunta2 = pyautogui.confirm('Assim que tiver ok avise...', buttons=['Ok','Parar!'])
#     if pergunta2 == 'Ok':   
#         ... #faça tal coisa...
#     else:
#         pyautogui.FailSafeException

# ABRIR SISTEMA REMOTO