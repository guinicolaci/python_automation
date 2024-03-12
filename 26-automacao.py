import pyautogui
from time import sleep

with open("files/alunos.txt", "r", encoding="utf-8") as file:
    for line in file:
        aluno = line.split(',')[0]
        email = line.split(',')[1]
        pyautogui.click(1429, 747, duration=1)
        pyautogui.write(aluno)
        pyautogui.click(1444, 809, duration=1)
        pyautogui.write(email)
        pyautogui.click(1460,837, duration=0.5)
        pyautogui.screenshot(f'files/img/{aluno}.png')
        sleep(1)
    
        # 1267, 718
        # 1267, 775