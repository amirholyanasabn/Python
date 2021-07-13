teams = ['GERMANY', 'ITALY', 'BRAZIL', 'ARGENTINA', 'NETHERLAND', 'ENGLAND', 'SPAIN', 'FRANCE']
your_team = (input('Please enter a team name : ')).upper()
if your_team in teams :
    rank = teams.index(your_team)+1
    print(rank)
else :
    print('not valid')
