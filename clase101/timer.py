# importar el modulo time
import time
#función countdown
def countdown_timer(seconds):
    while seconds>0:

        mins=int(seconds/60)
        secs=int(seconds%60)

        timer= f'{mins}:{secs}'

        print(timer, end='\r')

        time.sleep(1)
        seconds -=1

    print("\nSe acabó el tiempo\n\n༼ఠ ౪ఠ༽\n\n")

# tiempo  del input en segundos
seconds= input("Ingresa el tiempo en segundos ")
countdown_timer(int(seconds))