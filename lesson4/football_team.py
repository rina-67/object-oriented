class Football_Team():
	def __init__(self, name, win, lose, draw):
		self.name = name
		self.win = win
		self.lose = lose
		self.draw = draw

	def calc_win_rate(self):
		return self.win / (self.win + self.lose)
		#self.win+self.loseの左右に()忘れない

	def show_team_result(self):
		print(
		    f"{self.name:12s} {self.win:3d}{self.lose:3d} {self.draw:2d} {self.calc_win_rate():.3f}"
		)
		#self.関数
		"""
    {}の中で、、
    s...文字ボックス
      12s...12文字の欄
    d...数字ボックス
      3d...3つの数字欄
    
    :.3fとは
    少数第3位まで表示、それ以下は切り捨て
    """
