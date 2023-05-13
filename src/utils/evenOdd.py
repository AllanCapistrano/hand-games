from typing import List

from handtracking import HandDetector

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