from typing import List
from handtracking import HandDetector

class Jokenpo:
    def __init__(self) -> None:
        pass

    def is_rock(self, hand_detector: HandDetector, hand: List) -> bool:
        """ Verifica se o sinal feito com a mão representa a 'pedra' do jogo
        Jokenpô.

        Parameters
        ----------
        hand_detector: :class:`HandDetector`
            Objeto detector de mãos.
        hand: :class:`List`
            Lista contendo as mãos.

        Returns
        -------
        :class:`bool`
        """

        return True if (
            not hand_detector.is_thumb_raised(hand) and
            not hand_detector.is_index_finger_raised(hand) and
            not hand_detector.is_middle_finger_raised(hand) and
            not hand_detector.is_ring_finger_raised(hand) and
            not hand_detector.is_pinky_raised(hand)
        ) else False
    
    def is_paper(self, hand_detector: HandDetector, hand: List) -> bool:
        """ Verifica se o sinal feito com a mão representa o 'papel' do jogo
        Jokenpô.

        Parameters
        ----------
        hand_detector: :class:`HandDetector`
            Objeto detector de mãos.
        hand: :class:`List`
            Lista contendo as mãos.

        Returns
        -------
        :class:`bool`
        """

        return True if (
            hand_detector.is_thumb_raised(hand) and
            hand_detector.is_index_finger_raised(hand) and
            hand_detector.is_middle_finger_raised(hand) and
            hand_detector.is_ring_finger_raised(hand) and
            hand_detector.is_pinky_raised(hand)
        ) else False
    
    def is_scissors(self, hand_detector: HandDetector, hand: List) -> bool:
        """ Verifica se o sinal feito com a mão representa a 'tesoura' do jogo
        Jokenpô.

        Parameters
        ----------
        hand_detector: :class:`HandDetector`
            Objeto detector de mãos.
        hand: :class:`List`
            Lista contendo as mãos.

        Returns
        -------
        :class:`bool`
        """

        return True if (
            not hand_detector.is_thumb_raised(hand) and
            hand_detector.is_index_finger_raised(hand) and
            hand_detector.is_middle_finger_raised(hand) and
            not hand_detector.is_ring_finger_raised(hand) and
            not hand_detector.is_pinky_raised(hand)
        ) else False