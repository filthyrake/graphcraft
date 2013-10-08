from json import load
from pylab import figure, hist, setp, show, xlabel, ylabel, annotate, subplots_adjust
import numpy as np
import matplotlib.pyplot as plt
from urllib import urlopen
from time import sleep
from collections import Counter
from matplotlib.ticker import FormatStrFormatter

# The race you play - one of terran, zerg, protoss
MY_RACE = 'protoss'

# Your unique ggtracker ID
MY_GGTRACKER_ID = 1279
#MY_GGTRACKER_ID = 393266

# Maximum number of games to analyze
MAX_GAMES = 300

# The root API URL to filter your 1v1 ladder games
API_ROOT_URL = 'http://api.ggtracker.com/api/v1/matches?category=Ladder' + \
	'&game_type=1v1&race=' + MY_RACE + '&limit=' + repr(MAX_GAMES) + '&page=1' + \
	'&paginate=true&identity_id=' + repr(MY_GGTRACKER_ID)

# Class to store information about your race vs. another race
class RaceData:
	# Static data to summarize all races
	NumWins = 0
	NumLosses = 0
	WinDuration = []
	LossDuration = []

	# Initialize against the provided race
	def __init__(self, raceName):
		self.raceName = raceName
		self.numWins = 0
		self.numLosses = 0
		self.winDuration = []
		self.lossDuration = []

		self.urlPath = API_ROOT_URL + '&vs_race=' + raceName

	# Use the ggtracker API to query for all games versus this race
	# Record the number of wins & losses, as well as the duration of each win and loss
	def CountWinsAndLossesVersusRace(self):
		gameData = load(urlopen(self.urlPath))

		for game in gameData['collection']:
			if game['entities'][1]['win'] == True:
				self.numWins += 1
				self.winDuration.append(int(game['duration_seconds'] / 60))

				RaceData.NumWins += 1
				RaceData.WinDuration.append(int(game['duration_seconds'] / 60))
			else:
				self.numLosses += 1
				self.lossDuration.append(int(game['duration_seconds'] / 60))

				RaceData.NumLosses += 1
				RaceData.LossDuration.append(int(game['duration_seconds'] / 60))

		# Honor limit of 1 request per second
		sleep(1)

def PlotHistogram(bins, frequency, color, wins):
    figure()
#        percentages = []
    n, bins, patches = hist(bins, frequency, normed = 0, histtype = 'stepfilled')
    ylabel('Number of losses')
    xlabel('Game length (minutes)')
#
    data = bins
    myWins = Counter(wins)


    # Label the raw counts and the percentages below the x-axis...
    bin_centers = 0.5 * np.diff(bins) + bins[:-1]

    setp(patches, 'facecolor', color, 'alpha', 1)
    for count, x in zip(n, bin_centers):
        # Label the percentages
        
        if (float(count)+myWins[count]) != 0:
            percent = '%0.0f%%' % (100 * myWins[count] / (float(count)+myWins[count]))
        else :
            percent = '0%'
        if 100 * float(count) / n.sum() != 0:
            annotate(percent, xy=(x, 0), xycoords=('data', 'axes fraction'),
                xytext=(0, -45), textcoords='offset points', va='top', ha='center')
    
    # Give ourselves some more room at the bottom of the plot
    subplots_adjust(bottom=0.20)

def main():
	# Versus terran
	terran = RaceData('terran')
	terran.CountWinsAndLossesVersusRace()

	# Versus zerg
	zerg = RaceData('zerg')
	zerg.CountWinsAndLossesVersusRace()

	# Versus protoss
	protoss = RaceData('protoss')
	protoss.CountWinsAndLossesVersusRace()

	# Show the histograms
	PlotHistogram(RaceData.LossDuration, RaceData.NumLosses,'black', RaceData.WinDuration)
	PlotHistogram(terran.lossDuration, terran.numLosses,'blue', terran.winDuration)
	PlotHistogram(zerg.lossDuration, zerg.numLosses,'purple', zerg.winDuration)
	PlotHistogram(protoss.lossDuration, protoss.numLosses,'green', protoss.winDuration)
	show()


if __name__ == '__main__':
	main()
