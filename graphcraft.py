import urllib, json, pylab as P, numpy as np


url1 = 'http://api.ggtracker.com/api/v1/matches?category=Ladder&game_type=1v1&identity_id=1279&page=1&paginate=true&race=protoss&vs_race=terran&limit=300'
url2 = 'http://api.ggtracker.com/api/v1/matches?category=Ladder&game_type=1v1&identity_id=1279&page=1&paginate=true&race=protoss&vs_race=zerg&limit=300'
url3 = 'http://api.ggtracker.com/api/v1/matches?category=Ladder&game_type=1v1&identity_id=1279&page=1&paginate=true&race=protoss&vs_race=protoss&limit=300'


wins = 0
losses = 0
twins = 0
tlosses = 0
zwins = 0
zlosses = 0
pwins = 0
plosses = 0
winDuration = []
lossDuration = []
winDurationMins = []
lossDurationMins = []
twinDuration = []
tlossDuration = []
twinDurationMins = []
tlossDurationMins = []
zwinDuration = []
zlossDuration = []
zwinDurationMins = []
zlossDurationMins = []
pwinDuration = []
plossDuration = []
pwinDurationMins = []
plossDurationMins = []
totalWinTime = 0
totalLossTime = 0

gameData = json.load(urllib.urlopen(url1))

for game in gameData['collection']:
	if game['entities'][1]['win'] == True:
		wins+=1
                twins+=1
		winDuration.append(game['duration_seconds'])
		twinDuration.append(game['duration_seconds'])
                winDurationMins.append(game['duration_seconds']/60)
                twinDurationMins.append(game['duration_seconds']/60)
	else:
		losses+=1
                tlosses+=1
		lossDuration.append(game['duration_seconds'])
                lossDurationMins.append(game['duration_seconds']/60)
                tlossDuration.append(game['duration_seconds'])
                tlossDurationMins.append(game['duration_seconds']/60)

gameData = json.load(urllib.urlopen(url2))

for game in gameData['collection']:
	if game['entities'][1]['win'] == True:
		wins+=1
                zwins+=1
		winDuration.append(game['duration_seconds'])
		zwinDuration.append(game['duration_seconds'])
                winDurationMins.append(game['duration_seconds']/60)
                zwinDurationMins.append(game['duration_seconds']/60)
	else:
		losses+=1
                zlosses+=1
		lossDuration.append(game['duration_seconds'])
                lossDurationMins.append(game['duration_seconds']/60)
                zlossDuration.append(game['duration_seconds'])
                zlossDurationMins.append(game['duration_seconds']/60)

gameData = json.load(urllib.urlopen(url3))

for game in gameData['collection']:
	if game['entities'][1]['win'] == True:
		wins+=1
                pwins+=1
		winDuration.append(game['duration_seconds'])
		pwinDuration.append(game['duration_seconds'])
                winDurationMins.append(game['duration_seconds']/60)
                pwinDurationMins.append(game['duration_seconds']/60)
	else:
		losses+=1
                plosses+=1
		lossDuration.append(game['duration_seconds'])
                lossDurationMins.append(game['duration_seconds']/60)
                plossDuration.append(game['duration_seconds'])
                plossDurationMins.append(game['duration_seconds']/60)

for win in winDuration:
	totalWinTime += win		

for loss in lossDuration:
	totalLossTime += loss


x = lossDurationMins


n, bins, patches = P.hist(x, losses, normed=0, histtype='stepfilled')
P.ylabel('number of losses')
P.xlabel('game length in minutes')
P.setp(patches, 'facecolor', 'black', 'alpha', 1)





P.figure()

x = tlossDurationMins


n, bins, patches = P.hist(x, tlosses, normed=0, histtype='stepfilled')
P.ylabel('number of losses')
P.xlabel('game length in minutes')
P.setp(patches, 'facecolor', 'blue', 'alpha', 1)




P.figure()

x = zlossDurationMins


n, bins, patches = P.hist(x, zlosses, normed=0, histtype='stepfilled')
P.ylabel('number of losses')
P.xlabel('game length in minutes')
P.setp(patches, 'facecolor', 'purple', 'alpha', 1)





P.figure()

x = plossDurationMins


n, bins, patches = P.hist(x, plosses, normed=0, histtype='stepfilled')
P.ylabel('number of losses')
P.xlabel('game length in minutes')
P.setp(patches, 'facecolor', 'green', 'alpha', 1)




P.show()