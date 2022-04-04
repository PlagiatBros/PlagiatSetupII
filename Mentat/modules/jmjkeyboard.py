from .keyboard import Keyboard


class JmjKeyboard(Keyboard):
    """
    Jean-Michel Jarring Effects & Planche à Touches Incorporated (mididings patch)
    """

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
