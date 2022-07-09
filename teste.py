import pyautogui as spam
from time import sleep

# Mostra onde esta o cursor do mouse, usa-se as coordenadas para inserir no laço
#import mouse
#while True:
#    print(mouse.get_position())
#    sleep(1)

# Define uma quantidade finita de repetições
#limite_msg = int(input('Entre com o numero de mensagem que deseja enviar: '))

msg =  str(input('Digite a mensagem: '))

i = 0

sleep(2)

while True:#i < int(limite_msg):
    spam.click(1126, 684)
    spam.typewrite(msg)
    sleep(5)
    spam.click(1342, 684)
    i += 1
