from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import json
from datetime import datetime, timedelta
from vlr_utils.classes.match import Match
from vlr_utils.classes.team import Team
from vlr_utils.classes.event import Event

def remove_indents(value):
    value = value.replace('\n', '')
    value = value.replace('\t', '')
    return value

def remove_commas(value):
    value = value.replace(',', '')
    return value

def remove_quotes(value):
    value = value.replace('"', '')
    return value

def remove_formatting(team):
    team_name = remove_indents(team)
    team_name = remove_quotes(team_name)
    return team_name

def get_date(date, time):
    date = remove_indents(date.text)
    date = remove_commas(date)
    time = remove_indents(time.text)
    words = date.split(' ')
    date = words[1] + ' ' +  words[2] + ' ' + words[3]
    value = date + ' ' + time
    new_datetime = datetime.strptime(value, '%B %d %Y %I:%M %p')
    return new_datetime

def find_event_matches(id):

    matches = []

    url = f"https://www.vlr.gg/event/matches/{id}/?group=upcoming"

    options = webdriver.ChromeOptions()
    options.add_argument("--log-level=3")
    options.add_argument("--headless")

    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    driver.get(url)

    content = driver.page_source
    soup = BeautifulSoup(content, 'lxml')

    event_soup = soup.find('div', 'event-header').find('div', 'event-desc').div
    event_title = remove_indents(event_soup.h1.text)
    event_subtitle = remove_indents(event_soup.h2.text)

    dates_soup = soup.find_all('div', 'wf-label mod-large')

    for date in dates_soup:
        date_matches = date.find_next_sibling('div', 'wf-card').find_all('a')
        for date_match in date_matches:
            date_match_time = date_match.find('div', 'match-item-time')
            if (date_match_time is None or 'TBD' in remove_indents(date_match_time.text)):
                continue
            match_date = get_date(date, date_match_time)
            match_teams = date_match.find('div', 'match-item-vs').find_all('div', 'match-item-vs-team')
            match_team1 = Team(remove_formatting(match_teams[0].div.div.text))
            match_team2 = Team(remove_formatting(match_teams[1].div.div.text))
            match_info = date_match.find('div', 'match-item-event')
            match_round = remove_indents(match_info.div.text)
            match_stage = remove_formatting(match_info.div.next_sibling.text)
            match_length = 180
            new_match = Match(match_date, match_length, match_team1, match_team2, match_round, match_stage)
            matches.append(new_match)

    driver.close()

    new_event = Event(event_title, event_subtitle, matches)
    return new_event