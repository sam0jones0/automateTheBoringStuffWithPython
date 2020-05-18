#! python3
# myFileBot.py - Moves individual TV show files from Downloads 
# folder to TV/{showname} subfolder
# Usage - python myFileBot.py {showname}

from pathlib import Path
import os, sys, re, shutil, send2trash

showName = sys.argv[1]

showFolderRegex = re.compile(rf'{re.escape(showName)}.*', re.I)   # Regex for TV show folder name

showEpisodeRegex = re.compile(rf'''
    ({re.escape(showName)})       # Show name as match group1
    .*                            
    (S\d\dE\d\d)                  # Season & episode number as match group2
    .*
    \.mkv                         # File suffix
''', re.I | re.VERBOSE)

downloadsFiles = os.listdir(Path('D:/Downloads'))    # Location of Download folder

# Creates folder for files to be moved to D:/Documents/TV/{showname}
tvFolder = (Path(f'D:/Documents/TV/{sys.argv[1].title()}'))    
if not tvFolder.exists():
    os.makedirs(tvFolder)

for matches in downloadsFiles:
    episodeFolder = showFolderRegex.search(matches)
    if episodeFolder != None:
        episodeSubFolder = os.listdir(Path(f'D:/Downloads/{episodeFolder.group()}/'))
        for filesInSubfolder in episodeSubFolder:
            episode = showEpisodeRegex.search(filesInSubfolder)
            if episode != None:
                # Matches season and episode number, e.g. S01E01
                seasonAndEpisode = episode.group(2)
                # Set episode path
                episodePath = Path(f'D:/Downloads/{episodeFolder.group()}/{episode.group()}')
                # Moves and renames episode in format {showname}SXXEXX
                shutil.move(episodePath, tvFolder / f'{sys.argv[1].title()} {seasonAndEpisode}.mkv')
                # Remove folder from Downloads folder
                send2trash.send2trash((Path(f'D:/Downloads/{episodeFolder.group()}')))
