"""
The template of the script for playing the game in the ml mode
"""

from pygame.draw import circle


class MLPlay:
    turn = 0
    round = 0
    def __init__(self):
        """
        Constructor
        """
        pass
        
    def update(self, scene_info):
        """
        Generate the command according to the received scene information
        """
        if scene_info["status"] == "GAME_OVER" or len(scene_info["snake_body"]) == 303:
            return "RESET"

        snake_head = scene_info["snake_head"]

        if self.turn == 0 and self.round == 0:
            if snake_head[0] < 290:
                return "RIGHT"
            else:
                self.turn = 1
                return "DOWN"
        elif self.turn == 1 and self.round == 0:
            if snake_head[1] == 290:
                self.round = 1
            if snake_head[0] > 10:
                return "LEFT"       
            else:
                self.turn = 0
                return "DOWN"   
        elif self.round == 1:
            if snake_head[0] > 0:
                return "LEFT"       
            else:
                if snake_head[1] == 0:
                    self.round = 0
                    self.turn = 0
                    return "RIGHT"
                return "UP"

        # if self.turn == 0 and self.round == 0:
        #     if snake_head[1] < 290:
        #         return "DOWN"
        #     else:
        #         self.turn = 1
        #         return "RIGHT"
        # elif self.turn == 1 and self.round == 0:
        #     if snake_head[0] == 290:
        #         self.round = 1
        #     if snake_head[1] > 10:
        #         return "UP"       
        #     else:
        #         self.turn = 0
        #         return "RIGHT"   
        # elif self.round == 1:
        #     if snake_head[1] > 0:
        #         return "UP"       
        #     else:
        #         if snake_head[0] == 0:
        #             self.round = 0
        #             self.turn = 0
        #             return "DOWN"
        #         return "LEFT"

    def reset(self):
        """
        Reset the status if needed
        """
        pass
