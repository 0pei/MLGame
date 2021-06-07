"""
The template of the main script of the machine learning process
"""

class MLPlay:
    old_ball = []
    m = 0.0           # slope
    predictX = 100
    predictY = 395    # the height reflex happaned
    def __init__(self):
        """
        Constructor
        """
        self.ball_served = False

    def update(self, scene_info):
        """
        Generate the command according to the received `scene_info`.
        """
        # Make the caller to invoke `reset()` for the next round.
        if (scene_info["status"] == "GAME_OVER" or
            scene_info["status"] == "GAME_PASS"):
            return "RESET"

        if not self.ball_served:
            self.ball_served = True
            self.old_ball = scene_info["ball"]
            command = "SERVE_TO_LEFT"
        else:
            if scene_info["ball"][0] - self.old_ball[0] != 0 and scene_info["ball"][1] - self.old_ball[1] > 0:  # go down
                self.m = (scene_info["ball"][1] - self.old_ball[1]) / (scene_info["ball"][0] - self.old_ball[0])
                self.predictX = (395 - scene_info["ball"][1]) // self.m + scene_info["ball"][0]
                if self.predictX <= 0:
                    self.predictY = self.m * -scene_info["ball"][0] + scene_info["ball"][1]         # when x = 0
                    self.m *= -1
                    self.predictX = (395 - self.predictY) // self.m
                if self.predictX >= 195:
                    self.predictY = self.m * (195 - scene_info["ball"][0]) + scene_info["ball"][1]  # when x = 195
                    self.m *= -1
                    self.predictX = (395 - self.predictY) // self.m + 195
            if scene_info["platform"][0] + 5 > self.predictX:
                command = "MOVE_LEFT"
            elif scene_info["platform"][0] + 9 < self.predictX:
                command = "MOVE_RIGHT"
            else:
                command = "NONE"
            self.old_ball = scene_info["ball"]
        return command

    def reset(self):
        """
        Reset the status
        """
        self.ball_served = False

