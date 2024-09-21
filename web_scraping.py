# 1st step install and import moduls
    # pip install lxml
    # pip install requests
    # pip instal BeautifulSoup4
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

# create empty lists to store future data in it

#2nd step user request to fetch url

# give date

date = input("Please enter a Date in The Following Format MM/DD/YYYY: ")
page = requests.get(f'https://www.yallakora.com/match-center/?date={date}')



def main(page):
    src = page.content
    soup = BeautifulSoup(src,"lxml")
    matches_details=[]
    
    championships = soup.find_all("div", {'class':'matchCard'})
    
    def get_match_info(championships):
        championship_title = championships.find('h2').text.strip() 

        all_matches = championships.find_all('div',{'class':'ul'})
        number_of_matches = len(all_matches)

        for i in range(number_of_matches):
            #get teams name
            team_A= all_matches[i].find('div', {'class':'teamA'}).text.strip()
            team_B= all_matches[i].find('div', {'class':'teamB'}).text.strip()

            #get score
            match_result = all_matches[i].find('div', {'class':'MResult'}).find_all('span', {'class':'score'})
            score = f"{match_result[0].text.strip()} _ {match_result[1].text.strip()}"
            
            # get time
            match_time = all_matches[i].find('div', {'class':'MResult'}).find('span', {'class':'time'}).text.strip()

            #add info to match_details list
            matches_details.append({
                'إسم البطولة':championship_title,
                'الفريق الاول':team_A,
                'الفريق الثاني':team_B,
                'النتيجة':score,
                'وقت المباراة':match_time
            })


    # loop to go all the championships
    for i in range(len(championships)):
        get_match_info(championships[i])


    # add the match details to csv file
    keys = matches_details[0].keys()

    with open('C:\\Users\\aminh\\OneDrive\\Desktop\\data analyst\\Python\\scraping\\project2\\matches_details.csv','w',newline='', encoding='utf-8-sig') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(matches_details)
        print("Done")
main(page)
