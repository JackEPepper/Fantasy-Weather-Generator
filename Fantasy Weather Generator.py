from datetime import datetime, timedelta
import random
import csv
winter = dict({
(1,"Blizzard"),
(2,"Snow"),
(21,"Freezing Cold"),
(31,"Heavy Clouds"),
(41,"Light Clouds"),
(61,"Clear Skies"),
(100,"Strange Phenomena")})
spring = dict({
(1,"Thunderstorm"),
(3,"Heavy Rain"),
(6,"Rain"),
(21,"Light Clouds"),
(51,"Clear Skies"),
(81,"High Winds"),
(91,"Scorching Heat"),
(100,"Strange Phenomena")})
summer = dict({
(1,	"Thunderstorm"),
(2,	"Rain"),
(6,	"Light Clouds"),
(31,	"Clear Skies"),
(81,	"High Winds"),
(86,	"Scorching Heat"),
(100,	"Strange Phenomena")})
fall = dict({
(1,	"Thunderstorm"),
(3,	"Rain"),
(11,	"Heavy Clouds"),
(21,	"Light Clouds"),
(51,	"Clear Skies"),
(71,	"High Winds"),
(91,	"Scorching Heat"),
(100,	"Strange Phenomena")})
strange_phenomena = dict({
(1,	"Ashfall"),
(2,	"Solar Eclipse"),
(3,	"Strange Lights"),
(4,	"Meteor Shower"),
(5,	"Malevolent Storm"),
(6,	"Wild Magic Storm")})

# Generic function to lookup the result on a table according to a random input
def table_return(table, roll):
        diff = []
        for i in table.keys():
            if roll - i < 0:
                continue
            diff.append(i)
        return max(diff)

# Calls the correct table/the special table for a given date
def get_weather(rand, date):
        if date.month == 12 or date.month <= 2:
            weather = winter[table_return(winter,rand)]
        elif date.month >= 3 and date.month <= 5:
            weather = spring[table_return(spring,rand)]
        elif date.month >= 6 and date.month <= 8:
            weather = summer[table_return(summer,rand)]
        elif date.month >=9 and date.month <= 11:
            weather = fall[table_return(fall,rand)]
        if weather == "Strange Phenomena":
            weather = strange_phenomena[table_return(strange_phenomena,random.randint(1,6))]
        return weather    

def main():
    # Initial random roll on the table
    rand = random.randint(1,100)
    # Can be anytime, future dates work better for use with excel
    x = datetime(2048,1,1)
    cal = []
    for _ in range(0,364):
        # Adjusts the roll by a preset, bounded amount for more predictable weather
        rand += random.randint(-30,30)
        rand = max(min(rand,100),1)
        cal.append((x.strftime("%Y-%m-%d"), get_weather(rand,x)))
        x = x + timedelta(1)
    # Writes output to a csv
    fields = ["Date", "Weather"]
    filename = "fantasy_weather.csv"
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(cal)

if __name__ == '__main__':
    main()