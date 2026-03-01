"""
CCR3 - Chinese Chess Robot
Game Manager - Main Entry Point

State Machine:
    IDLE → DETECT → THINK → MOVE → WAIT → DETECT → ...
"""


class GameState:
    IDLE = "IDLE"
    DETECT = "DETECT"
    THINK = "THINK"
    MOVE = "MOVE"
    WAIT = "WAIT"


class GameManager:
    def __init__(self):
        self.state = GameState.IDLE
        # TODO: Initialize vision, engine, control modules

    def run(self):
        """Main game loop"""
        print("CCR3 - Chinese Chess Robot")
        print("Starting game manager...")

        while True:
            if self.state == GameState.IDLE:
                self._handle_idle()
            elif self.state == GameState.DETECT:
                self._handle_detect()
            elif self.state == GameState.THINK:
                self._handle_think()
            elif self.state == GameState.MOVE:
                self._handle_move()
            elif self.state == GameState.WAIT:
                self._handle_wait()

    def _handle_idle(self):
        # TODO: Wait for game start signal
        pass

    def _handle_detect(self):
        # TODO: Capture image and detect board state
        pass

    def _handle_think(self):
        # TODO: Send FEN to engine and get best move
        pass

    def _handle_move(self):
        # TODO: Execute robot movement
        pass

    def _handle_wait(self):
        # TODO: Wait for opponent's move
        pass


if __name__ == "__main__":
    gm = GameManager()
    gm.run()
