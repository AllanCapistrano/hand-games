from time import time
from typing import List

import cv2
from numpy import bincount, argmax
from utils import EvenOdd

WEBCAM_INDEX = 1

def main():
    fps_start_time: float = 0

    hand_detector = EvenOdd()

    webcam = cv2.VideoCapture(WEBCAM_INDEX)

    fps_flag: bool = True
    even_odd_flag: bool = False

    amount_fingers: List[int] = []

    while(True):
        success, frame = webcam.read()

        if(success):
            key = cv2.waitKey(1)

            hand_detector.process_image(frame)
            # image_with_landmarks = frame
            image_with_landmarks = hand_detector.draw_landmarks()
            # hands: List[Dict] = hand_detector.find_positions()

            # if(len(hands) > 0):
            #     print(hand_detector.hand_orientation(hands[0]))
            #     print(hands[0]["landmarks"][6])

            number_fingers: int = hand_detector.number_fingers()

            # print(f"Número de dedos: {number_fingers}")

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

            # Define o tempo de duração do temporizador em segundos
            duration_timer = 3

            if(even_odd_flag):
                elapsed_time = current - start
                time_left = duration_timer - elapsed_time

                amount_fingers.append(number_fingers)

                if(time_left <= 0):
                    print("3 segundos")
                    even_odd_flag = False
                    print(f"Dedos: {amount_fingers}")
                    print(f"Moda dedos: {argmax(bincount(amount_fingers))}")
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
    
    webcam.release()

if __name__ == "__main__":
    main()