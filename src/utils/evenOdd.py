from typing import List

from .handDetector import HandDetector

THUMB_TIP: int = 4
INDEX_FINGER_TIP: int = 8
MIDDLE_FINGER_TIP: int = 12
RING_FINGER_TIP: int = 16
PINKY_TIP: int = 20

class EvenOdd(HandDetector):
    def __init__(
        self,
        max_num_hands: int = 2,
        model_complexity: int = 1,
        min_detection_confidence: float = 0.5, 
        min_tracking_confidence: float = 0.5
    ) -> None:
        """ Método construtor

        Parameters
        ----------
        max_num_hands: :class:`int`
            Número máximo de mãos que presentes na imagem.
        model_complexity: :class:`int`
            Complexidade do modelo 'landmark' (0 ou 1).
        min_detection_confidence: :class:`float`
            Valor mínimo de confiança para que a detecção das mãos seja 
            considerada bem-sucedida.
        min_tracking_confidence: :class:`float`
            Valor mínimo de confiança para os pontos de referência das mãos 
            serem considerados rastreados com sucesso.
        """

        super().__init__(
            self,
            max_num_hands = max_num_hands, 
            model_complexity = model_complexity, 
            min_detection_confidence = min_detection_confidence,
            min_tracking_confidence = min_tracking_confidence
        )

    def number_fingers(self) -> int:
        """ Retorna o número de dedos que estão levantados.

        Returns
        -------
        :class:`int`
        """

        hands: List = self.find_positions()

        count_fingers: int = 0

        if(len(hands) > 0):
            for hand in hands:
                for index in range(len(hand["landmarks"])):
                    if(index == INDEX_FINGER_TIP):
                        finger_tip: int = hand["landmarks"][index]["y"]
                        finger_pip: int = hand["landmarks"][index - 2]["y"]
                        
                        if(finger_tip < finger_pip):
                            count_fingers += 1
                    elif(index == MIDDLE_FINGER_TIP):
                        finger_tip: int = hand["landmarks"][index]["y"]
                        finger_pip: int = hand["landmarks"][index - 2]["y"]
                        
                        if(finger_tip < finger_pip):
                            count_fingers += 1
                    elif(index == RING_FINGER_TIP):
                        finger_tip: int = hand["landmarks"][index]["y"]
                        finger_pip: int = hand["landmarks"][index - 2]["y"]
                        
                        if(finger_tip < finger_pip):
                            count_fingers += 1
                    elif(index == PINKY_TIP):
                        finger_tip: int = hand["landmarks"][index]["y"]
                        finger_pip: int = hand["landmarks"][index - 2]["y"]
                        
                        if(finger_tip < finger_pip):
                            count_fingers += 1
                    elif(index == THUMB_TIP):
                        thumb_tip: int = hand["landmarks"][THUMB_TIP]["x"]
                        index_finger_mcp: int = hand["landmarks"][5]["x"]
                        
                        if(abs(thumb_tip - index_finger_mcp) > 30):
                            count_fingers += 1
           
        return count_fingers