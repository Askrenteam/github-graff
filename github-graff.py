from datetime import date
from datetime import timedelta
from subprocess import call
message = "abc"
alphabet = {
'a': [
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,1,1,1],
        [0,1,0,0,1],
        [0,1,0,0,1],
        [0,0,1,1,1],
        [0,0,0,0,0]
    ],
'b': [
        [0,1,0,0,0],
        [0,1,0,0,0],
        [0,1,1,1,0],
        [0,1,0,0,1],
        [0,1,0,0,1],
        [0,1,1,1,0],
        [0,0,0,0,0]
    ],
'c': [
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,1,1,0],
        [0,1,0,0,0],
        [0,1,0,0,0],
        [0,0,1,1,0],
        [0,0,0,0,0]

    ]
}
today = date.today()
last_sunday = today - timedelta(days=today.isoweekday()%7)
start = last_sunday - timedelta(weeks=51)
def getDate(date):
    return date.isoformat().replace('-','.')

print(getDate(start))

for index in range(len(message)):
    char=message[index]
    for row in range(7):
        for col in range(5):
            if alphabet[char][row][col]:
                for i in range(15):
                    # TODO: calc days offset for (row,col)
                    call(["git", "commit", "--allow-empty", "--date", getDate(start + timedelta(weeks=5*index, )), "-m", "lol"])



