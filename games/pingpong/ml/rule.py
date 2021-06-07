"""
The template of the script for the machine learning process in game pingpong
"""

class MLPlay:
    old_ball = []
    m = 0.0           # slope
    predictX = 100
    predictY_1P = 415    # the height reflex happaned
    predictY_2P = 85
    def __init__(self, side):
        """
        Constructor

        @param side A string "1P" or "2P" indicates that the `MLPlay` is used by
               which side.
        """
        self.ball_served = False
        self.side = side

    def update(self, scene_info):
        """
        Generate the command according to the received scene information
        """
        if scene_info["status"] != "GAME_ALIVE":
            print(scene_info["ball_speed"])
            return "RESET"

        if not self.ball_served:
            self.ball_served = True
            self.old_ball = scene_info["ball_speed"]
            return "SERVE_TO_LEFT"
        else:
            if self.side == '1P':
                if scene_info["ball"][0] - self.old_ball[0] != 0 and scene_info["ball"][1] - self.old_ball[1] > 0:  # go down
                    self.m = (scene_info["ball"][1] - self.old_ball[1]) / (scene_info["ball"][0] - self.old_ball[0])
                    self.predictX = (415 - scene_info["ball"][1]) // self.m + scene_info["ball"][0]
                    if self.predictX <= 0:
                        self.predictY_1P = self.m * -scene_info["ball"][0] + scene_info["ball"][1]         # when x = 0
                        self.m *= -1
                        self.predictX = (415 - self.predictY_1P) // self.m
                    if self.predictX >= 195:
                        self.predictY_1P = self.m * (195 - scene_info["ball"][0]) + scene_info["ball"][1]  # when x = 195
                        self.m *= -1
                        self.predictX = (415 - self.predictY_1P) // self.m + 195
                if scene_info["platform_1P"][0] + 13 > self.predictX:
                    command = "MOVE_LEFT"
                elif scene_info["platform_1P"][0] + 10 < self.predictX:
                    command = "MOVE_RIGHT"
                else:
                    command = "NONE"
                self.old_ball = scene_info["ball"]
                return command
                
            if self.side == '2P':
                if scene_info["ball"][0] - self.old_ball[0] != 0 and scene_info["ball"][1] - self.old_ball[1] < 0:  # go up
                    self.m = (scene_info["ball"][1] - self.old_ball[1]) / (scene_info["ball"][0] - self.old_ball[0])
                    self.predictX = (85 - scene_info["ball"][1]) // self.m + scene_info["ball"][0]
                    if self.predictX <= 0:
                        self.predictY_2P = self.m * -scene_info["ball"][0] + scene_info["ball"][1]         # when x = 0
                        self.m *= -1
                        self.predictX = (85 - self.predictY_2P) // self.m
                    if self.predictX >= 195:
                        self.predictY_2P = self.m * (195 - scene_info["ball"][0]) + scene_info["ball"][1]  # when x = 195
                        self.m *= -1
                        self.predictX = (85 - self.predictY_2P) // self.m + 195
                if scene_info["platform_2P"][0] + 10 > self.predictX:
                    command = "MOVE_LEFT"
                elif scene_info["platform_2P"][0] + 10 < self.predictX:
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
