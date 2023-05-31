from time import time
from typing import List
from os import getenv

from dotenv import load_dotenv
import cv2
from numpy import ndarray

from utils import is_even, nearest_number, Jokenpo
from handtracking import HandDetector
from handtracking.utils import detect_skin, statistical_mode
load_dotenv()

# ------------------------------- CONSTANTES ----------------------------------#
try:
    WEBCAM_INDEX: int = int(getenv("WEBCAM_INDEX"))
    TIMER_DURATION_EVEN_ODD: int = int(getenv("TIMER_DURATION_EVEN_ODD"))
    TIMER_DURATION_NEAREST_NUMBER: int = int(
        getenv("TIMER_DURATION_NEAREST_NUMBER")
    )
    TIMER_DURATION_JOKENPO: int = int(getenv("TIMER_DURATION_JOKENPO"))
except:
    print("Erro! As variáveis de ambiente devem ser um números inteiros.")
    exit()
# -----------------------------------------------------------------------------#

def main():
    # TODO: Quando iniciar um jogo colocar as flags dos demais para falso.
    # TODO: Identificar a mão de cada jogador.
    # TODO: Verificar os tipos dos parâmetros dos métodos.
    # TODO: Criar um método para encapsular a exibição do temporizador na tela.

    fps_start_time: float = 0

    hand_detector: HandDetector = HandDetector()

    webcam = cv2.VideoCapture(WEBCAM_INDEX)

    fps_flag: bool = True
    even_odd_flag: bool = False
    nearest_number_flag: bool = False
    jokenpo_flag: bool = False

    amount_fingers: List[int] = []

    while(True):
        success, frame = webcam.read()

        image_to_process: ndarray = detect_skin(frame)

        if(success):
            key = cv2.waitKey(1)

            hand_detector.process_image(image_to_process)
            image_with_landmarks = hand_detector.draw_landmarks(frame)
            
            number_fingers: int = hand_detector.number_fingers()

            fps_end_time: float = time()
            fps: float = 1/(fps_end_time - fps_start_time)
            fps_start_time: float = fps_end_time

            current: float = time()

            if(key == 81 or key == 113): # Q ou q
                break
            elif(key == 70 or key == 102): # F ou f
                fps_flag = not fps_flag
            elif(key == 83 or key == 115): # S ou s
                even_odd_flag = True
                start: float = time()
            elif(key == 78 or key == 110): # N ou n
                guess_one: int = int(input("Palpite do jogador 1: "))
                guess_two: int = int(input("Palpite do jogador 2: "))

                nearest_number_flag = True
                start: float = time()
            elif(key == 74 or key == 106): # J ou j
                jokenpo_flag = True
                start: float = time()

            if(even_odd_flag):
                elapsed_time = current - start
                time_left = TIMER_DURATION_EVEN_ODD - elapsed_time

                amount_fingers.append(number_fingers)

                if(time_left <= 0):
                    even_odd_flag = False
                    print(f"Dedos: {amount_fingers}")
                    print(f"Moda dedos: {statistical_mode(amount_fingers)}")
                    
                    if(is_even(statistical_mode(amount_fingers))):
                        print("É par")
                    else:
                        print("É ímpar")
                    
                    amount_fingers.clear()
                
                cv2.putText(
                    image_with_landmarks, 
                    f"Iniciando em: {int(time_left)}s", 
                    (250, 40), 
                    cv2.FONT_HERSHEY_PLAIN, 
                    2, 
                    (0, 255, 255), 
                    3
                )

            if(nearest_number_flag):
                elapsed_time = current - start
                time_left = TIMER_DURATION_NEAREST_NUMBER - elapsed_time

                amount_fingers.append(number_fingers)

                if(time_left <= 0):
                    nearest_number_flag = False
                    mode: int = statistical_mode(amount_fingers)
                    
                    print(nearest_number(guess_one, guess_two, mode))
                    print(f"Moda dedos: {mode}")

                    amount_fingers.clear()

                cv2.putText(
                    image_with_landmarks, 
                    f"Iniciando em: {int(time_left)}s", 
                    (250, 40), 
                    cv2.FONT_HERSHEY_PLAIN, 
                    2, 
                    (0, 255, 255), 
                    3
                )
                
            if(jokenpo_flag):
                elapsed_time = current - start
                time_left = TIMER_DURATION_EVEN_ODD - elapsed_time

                if(time_left <= 0):
                    jokenpo_flag = False
                    
                    hands: List = hand_detector.find_positions()
                    jokenpo: Jokenpo = Jokenpo(hand_detector, hands)

                    winner: str = jokenpo.start_game()
                    print(winner)

                cv2.putText(
                    image_with_landmarks, 
                    f"Iniciando em: {int(time_left)}s", 
                    (250, 40), 
                    cv2.FONT_HERSHEY_PLAIN, 
                    2, 
                    (0, 255, 255), 
                    3
                )
                
            if(fps_flag):
                cv2.putText(
                    image_with_landmarks, 
                    f"FPS: {int(fps)}", 
                    (10, 40), 
                    cv2.FONT_HERSHEY_PLAIN, 
                    2, 
                    (0, 255, 255), 
                    3
                )

            cv2.imshow("Webcam", image_with_landmarks)
        else:
            print("Não foi possível iniciar a webcam!")
            exit()
    
    webcam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()