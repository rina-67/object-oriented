from football_team import Football_Team

Brazil = Football_Team('Brazil', 73, 45, 18)
Italy = Football_Team('Italy', 45, 21, 21)
Argentina = Football_Team('Argentina', 43, 15, 15)
WestGermany = Football_Team('WestGermany', 36, 14, 14)
France = Football_Team('France', 34, 13, 13)
Germany = Football_Team('Germany', 31, 6, 6)
Spain = Football_Team('Spain', 30, 15, 15)

#インスタンスをリストに追加、大事
teams = [Brazil, Italy, Argentina, WestGermany, France, Germany, Spain]
#teamsからteamを１つずつ取り出して結果を表示
for team in teams:
	team.show_team_result()
