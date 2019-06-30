#!/usr/bin/python3
print("Content-type: text/html\r\n\r\n")

from bs4 import BeautifulSoup
import requests

page = requests.get('http://scores.sify.com/?ref=deskcric')

soup = BeautifulSoup(page.content,'html.parser')

match_name=soup.find_all('a',{'class':'scroll'})[0].string
print("<h1>Current match running is:"+match_name+"</h1>")



match_location=soup.select_one('div.scoresbox-center span').string
print("<h2> Match location:"+match_location+"</h2>")
live_match_link=soup.select_one('div.scoresbox-center h2 a').attrs.get('href')



page_curr_match = requests.get(live_match_link)
soup_live = BeautifulSoup(page_curr_match.content,'html.parser')



teams_info=soup_live.find_all('div',{'class':'team-live'})[0].find('h1').string

bat_team_info=soup_live.select_one('div.team-live-venue h2').string



bat_team_name=''
bat_team_run=''
for i in range(0,len(bat_team_info)):
    try:
        if type(int(bat_team_info[i])) is int:
            for j in range(i,len(bat_team_info)):
                bat_team_run = bat_team_run + bat_team_info[j]
            break
        else:
            continue
    except:
        bat_team_name = bat_team_name + bat_team_info[i]

# run rat and needs that run to win the match
try:
    target_split=soup_live.find_all('div',{'class':'team-live-venue'})[0].find('p').string.split('|')
    target=target_split[1]
except:
    target='Match yet to start'



#finding team 1
team1_finder=soup_live.find_all('div',{'id':'team1'})[0].find_all('ul')

team1_squad=[]
for i in team1_finder[0].find_all('li'):
    team1_squad.append(i.find_all('a')[0].string)


# finding the team2 members
team2_finder=soup_live.find_all('div',{'id':'team2'})[0].find_all('ul')


team2_squad=[]
for i in team2_finder[0].find_all('li'):
    team2_squad.append(i.find_all('a')[0].string)


over=soup.find_all('h3',{'id':'batteamnameruns1'})[0].text.split('(')[1].split(')')[0]


try:
    batsman1=soup.find_all('h4',{'id':'batsmanbowlerdetails1'})[0].find_all('p')[0].find('a').string
except:
    batsman1='Wait For Match To Start'



try:
    batsman2=str(soup.find_all('h4',{'id':'batsmanbowlerdetails1'})[0].find_all('p')[0]).split('|')[1].split('>')[1].split('<')[0]
except:
    batsman2='Wait For Match To Start'












print('<!DOCTYPE html>')
print('<html>')
print('<head>')
print('<meta http-equiv="refresh" content="15">')
print('<link rel="stylesheet" type="text/css" href="my.css">')
print('<title>	LIVE SCORE</title>')
#print('<style>')
#print('body "background-image:url(http://13.234.67.54/web.gif)"')
#print('</style>')
print('</head>')
print('<body background="https://media.giphy.com/media/cx0ZH3AzlYc12/giphy.gif">')
print('<b style="color: #f44167" >SCORE VIEWER</b>')
print('<marquee width = "100%"><b><font color="red">'+target+'</b></marquee>')
print('</body>')
print('</html>')
print('<form >')
print('<div id="tm" style=" width:100%;">')
print('<div id="tm1" style="float: left"> Team 1: <label>'+bat_team_name+'</label></div>')
print('<div id="tm2" style="margin-right:20px; float: right"> Team 2: <input type = "text"  style="align="right" name = "Team 2" /></div>')
print('</div>')
#print('Team 1: <input type = "text"  align="left" name = "Team 1" />')
print('<br>')
print('<table border = "1"   width="250" align="left" >')
print('<tr>')
print('<th><font color="blue"><b>Players :TEAM 1</b></font></th>')
print('</tr>')
print('<tr>')
print('<td><label>'+team1_squad[0]+'</label></td>')
print('</tr>')
print('<tr>')
print('<td><label>'+team1_squad[1]+'</label></td>')
print('</tr>')
print('<tr>')
print('<td><label>'+team1_squad[2]+'</label></td>')
print('</tr>')
print('<tr>')
print('<td><label>'+team1_squad[3]+'</label></td>')
print('</tr>')
print('<tr>')
print('<td><label>'+team1_squad[4]+'</label></td>')
print('</tr>')
print('<tr>')
print('<td><label>'+team1_squad[5]+'</label></td>')
print('</tr>')
print('<tr>')
print('<td><label>'+team1_squad[6]+'</label></td>')
print('</tr>')
print('<tr>')
print('<td><label>'+team1_squad[7]+'</label></td>')
print('</tr>')
print('<tr>')
print('<td><label>'+team1_squad[8]+'</label></td>')
print('</tr>')
print('<tr>')
print('<td><label>'+team1_squad[9]+'</label></td>')
print('</tr>')
print('<tr>')
print('<td><label>'+team1_squad[10]+'</label></td>')
print('</tr>')
print('</table>')
print('<style>')
print('table, td, th {border: 1px solid black;}')
print('table {border-collapse: collapse; width: 25%;}')
print('th {height: px;}')
print('</style>')
print('<table border="1"  	align="right" width="250" >')
print('<tr>')
print('<th><font color="blue"><b>Players : TEAM 2</b></font></th>')
print('</tr>')
print('<tr>')
print('<td><label>'+team2_squad[0]+'</label></td>')
print('</tr>')
print('<tr>')
print('<td><label>'+team2_squad[1]+'</label></td>')
print('</tr>')
print('<tr>')
print('<td><label>'+team2_squad[2]+'</label></td>')
print('</tr>')
print('<tr>')
print('    <td><label>'+team2_squad[3]+'</label></td>')
print('    </tr>')
print('    <tr>')
print('    <td><label>'+team2_squad[4]+'</label></td>')
print('    </tr>')
print('    <tr>')
print('    <td><label>'+team2_squad[5]+'</label></td>')
print('    </tr>')
print('    <tr>')
print('    <td><label>'+team2_squad[6]+'</label></td>')
print('    </tr>')
print('    <tr>')
print('    <td><label>'+team2_squad[7]+'</label></td>')
print('    </tr>')
print('    <tr>')
print('    <td><label>'+team2_squad[8]+'</label></td>')
print('    </tr>')
print('   <tr>')
print('    <td><label>'+team2_squad[9]+'</label></td>')
print('    </tr>')
print('    <tr>')
print('    <td><label>'+team2_squad[10]+'</label></td>')
print('    </tr>')
print('      </table>')
print('      <table align="center" border="1" width="500" height="150">')
print('  <tr>')
print('   <th>Bating team : <label>'+bat_team_name+'</label> </th> ')
print('    </tr>')
print('  <tr>')
print('    <td>Batsman1 : <label>'+batsman1+'</label></td>')
print('  </tr>')
print('  <tr>')
print('    <td>Batsman 2 :  <label>'+batsman2+'</label></td>')
print('  </tr>')
print('</table>')
print('<table align="center" border="1" width="500">')
print('<tr>')
print('    <th>Bowling team : <input type = "text"name = "name"/> </th> ')
print('    </tr>')
print('  <tr>')
print('    <td>Bowler : <input type = "text"name = "name"/></td>')
print('    </tr>')
print('</table>')
print('<div align="center"  style="vertical-align:bottom">')
print('<div align="center" style="vertical-align:bottom">')
print('<table>')
print('<tr>')
print('    <td><b style="color:#f44167" > SCORE</b> : <label>'+bat_team_run+'</label></td>')
print('  </tr>')
print('      <tr>')
print('    <td><b style="color:#f44167">OVER</b> : <label>'+over+'</label></td>')
print('  </tr>')
print('</table>')
print('</div>')
print('</div>')
print('</body>')
print('</html> ')
