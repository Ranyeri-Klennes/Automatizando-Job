import pyautogui, time

pyautogui.PAUSE = 1

# DEIXANDO TUDO PRONTO

# # ABRIR WPP
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
pyautogui.hotkey('ctrl','l')
pyautogui.write('youtu.be')
pyautogui.press('enter')
pyautogui.sleep(10)
pyautogui.click(1266, 143, 1, interval=0.3, button='left')# clica para acessar o login.

# ABRIR SISTEMA REMOTO
pergunta = pyautogui.confirm('Rany, posso continuar?', buttons=['Sim','Não'])
if pergunta == 'Sim':
    pyautogui.press('win')
    pyautogui.write('remota', interval=0.2)
    pyautogui.press('enter')
    time.sleep(1)
else:
    pyautogui.PAUSE
pyautogui.confirm('Rany, posso continuar?', buttons=['Sim','Não'])
if pergunta == 'Sim':
    pyautogui.sleep(15)
    pyautogui.click(621, 435, 1, button='left')
    pyautogui.write('gcf')
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.click(621, 435, 1, button='left')
else: 
    pyautogui.sleep()