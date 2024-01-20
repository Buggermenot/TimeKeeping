timeKeeper = dict()

def run():
    global timeKeeper
    with open("timekeeping.csv", 'r') as tfile:
        rows = tfile.readlines()[1:]
    
    rows = [row.rstrip('\n').split(', ') for row in rows]
    rows = [(", ".join(row[:2]).lower(), row[2]) for row in rows]
    
    for row in rows:
        timeKeeper.setdefault(row[0], []).append(row[1])
    
    sortAlphabetical()
    sortTeamwise()
    
def getOut():
    for participant, times in timeKeeper.items():
        print(f'{participant.title()}: {f'Out At: {times[-1]}' if len(times) & 1 else "In"}')

def displayAll():
    for participant, times in timeKeeper.items():
        print(participant, ': ', times)
    
def sortAlphabetical():
    global timeKeeper
    timeKeeper = dict(sorted(timeKeeper.items(), key = lambda k: k[0]))

def sortTeamwise():
    global timeKeeper
    timeKeeper = dict(sorted(timeKeeper.items(), key = lambda k: int(k[0].split(', ')[1])))


run()
