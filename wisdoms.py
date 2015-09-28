from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from random import randint
# need for using handles to labels
from kivy.properties import ObjectProperty, StringProperty

# for work with csv text file
import operator
import csv


Builder.load_file('wisdoms.kv')

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.


# Declare all screens
class MainScreen(Screen):
    # initialize handle/text of label
    wisdom_text_id = StringProperty()
    def callback_get_wisdom(self):

        good_text_id = StringProperty()
        good_text_id = 'List of most implemented wisdoms:' + '\n'
        wisdoms_list = open('wisdoms.txt','r')
        wisdoms_list = list(csv.reader(wisdoms_list,delimiter='|'))
        wisdom_number = randint(0,len(wisdoms_list)-1)
        global wisdom_number
        wisdom_cell = wisdoms_list[wisdom_number][0]
	self.wisdom_text_id = wisdom_cell	

    def callback_update_GOOD(self):
	wisdoms_list = open('wisdoms.txt','r')
        wisdoms_list = list(csv.reader(wisdoms_list,delimiter='|'))
	wisdoms_list[wisdom_number][1] = int(wisdoms_list[wisdom_number][1]) + 1
        writer = csv.writer(open('wisdoms.txt','w'),delimiter ='|')
	writer.writerows(wisdoms_list)

	
    def callback_update_BAD(self):
        wisdoms_list = open('wisdoms.txt','r')
        wisdoms_list = list(csv.reader(wisdoms_list,delimiter='|'))
        wisdoms_list[wisdom_number][2] = int(wisdoms_list[wisdom_number][2]) + 1
        writer = csv.writer(open('wisdoms.txt','w'),delimiter ='|')
        writer.writerows(wisdoms_list)
	

class SettingsScreen(Screen):
    pass
class MenuScreen(Screen):
    pass
class ImplementedScreen(Screen):
#    print 'prve nbavi'
    good_text_id = StringProperty()
    good_text_id = 'List of most implemented wisdoms:' + '\n'
    implemented_list = open('wisdoms.txt','r')
    implemented_list = list(csv.reader(implemented_list,delimiter='|'))
    sort = sorted(implemented_list,key=operator.itemgetter(1),reverse=True)
    for eachline in sort:
	good_text_line = eachline[:][0]
        good_text_id = good_text_id +'\n' + unichr(183)+ ' '  + good_text_line + '\n'

class Will_tryScreen(Screen):
#    print 'bavi to'
    bad_text_id = StringProperty()
    bad_text_id = 'List of least implemented wisdoms:' + '\n'
    will_try_list = open('wisdoms.txt','r')
    will_try_list = list(csv.reader(will_try_list,delimiter='|'))
    sort = sorted(will_try_list,key=operator.itemgetter(2),reverse=True)
    for eachline in sort:
        bad_text_line = eachline[:][0]
        bad_text_id = bad_text_id +'\n' + unichr(183)+ ' '  + bad_text_line + '\n'


# Create the screen manager
sm = ScreenManager()
sm.add_widget(MainScreen(name='main'))
sm.add_widget(SettingsScreen(name='settings'))
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ImplementedScreen(name='implemented'))
sm.add_widget(Will_tryScreen(name='will_try'))

class Wisdoms(App):
    def build(self):
        return sm

if __name__ == '__main__':
    Wisdoms().run()
