import unittest

class Score0_0():
    def serverWin(self):
        return Score15_0()
    def receiverWin(self):
        return Score0_15()

class Score15_0():
    def serverWin(self):
        return Score30_0()

class Score0_15():
    def receiverWin(self):
        return Score0_30()

class Score30_0():
    def serverWin(self):
        return Score40_0()

class Score40_0():
    def serverWin(self):
        return WinnerIsServer()
    
class Score0_30():
    pass

class Score40_40():
    def serverWin(self):
        return ServerAdvantage()

class ServerAdvantage():
    def receiverWin(self):
        return Score40_40()

class WinnerIsServer():
    pass

class  Score15_15():
    pass

class TennisKataTest(unittest.TestCase):
    def test_dictionary(self):
        dictScore = {
            [Score0_0, 'serverWin']: Score15_0,
            [Score0_0, 'receiverWin']: Score0_15,
            [Score15_0, 'serverWin']: Score30_0,
            [Score15_0, 'receiverWin']: Score15_15,
            
        }
        for currentState, nextScore in dictScore:
            score = currentState[0]
            action = currentState[1] 
            result = getattr(score, action)()
            self.assertTrue(isinstance(result, nextScore))
            
        
    def test_first_1_ball_second_0_balls(self):
        currentScore = Score0_0()
        result = currentScore.serverWin()
        self.assertTrue(isinstance(result, Score15_0))

    def test_first_0_balls_second_1_ball(self):
        currentScore = Score0_0()
        result = currentScore.receiverWin()
        self.assertTrue(isinstance(result, Score0_15))

    def test_first_2_balls_second_0_balls(self):
        currentScore = Score15_0()
        result = currentScore.serverWin()
        self.assertTrue(isinstance(result, Score30_0))

    def test_first_0_balls_second_2_balls(self):
        currentScore =  Score0_15()
        result = currentScore.receiverWin()
        self.assertTrue(isinstance(result, Score0_30))

    def test_first_3_balls_second_0_balls(self):
        currentScore = Score30_0()
        result = currentScore.serverWin()
        self.assertTrue(isinstance(result, Score40_0))

    def test_first_4_balls_second_0_balls(self):
        currentScore = Score40_0()
        result = currentScore.serverWin()
        self.assertTrue(isinstance(result, WinnerIsServer))

    def test_first_5_balls_second_4_balls(self):
        currentScore = Score40_40()
        result = currentScore.serverWin()
        self.assertTrue(isinstance(result, ServerAdvantage))

    def test_first_5_balls_second_5_balls(self):
        currentScore = ServerAdvantage()
        result = currentScore.receiverWin()
        self.assertTrue(isinstance(result, Score40_40))



if __name__ == "__main__":
    unittest.main()
