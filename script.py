from dataclasses import replace
from scrap import Scrap 
import helpers
import os
from notify import Notify

title = Scrap.get_data()['title']
date = Scrap.get_data()['date']
buy = helpers.parse_to_float(Scrap.get_data()['values']['buy'])
sell = helpers.parse_to_float(Scrap.get_data()['values']['sell'])
variation = helpers.parse_to_float(Scrap.get_data()['variation'])

variation_notify_diff = float(os.getenv('VARIATION_NOTIFY_DIFF'))

response = {
    'title': title,
    'date': date,
    'buy': buy,
    'sell': sell,
    'variation': variation 
}

if variation >= variation_notify_diff:
    Notify.send_mail_notification()

""" Alexa Skill to notify """