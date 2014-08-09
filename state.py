class HomeState:
	def __init__(self):
		display.firstLine("pizaid.com")
		localtime = time.asctime(time.localtime(time.time()))
		display.secondLine(localtime) 
	def up(self, context): context.changeState(BatteryState)
	def down(self, context):context.changeState(NetworkState)
class NetworkState:
	def __init__(self):
		display.firstLine("IP Adress")
		display.secondLine(localtime) 
	def up(self, context): context.changeState(BatteryState)
		 
	def up(self, context): context.changeState(HomeState)
	def down(self, context):context.changeState(StorageState)
class StorageState:
	def __init__(self): pass
	def up(self, context): context.changeState(NetworkState)
	def down(self, context):context.changeState(BatteryState)
	def left(self, context):context.changeState(StorageDetail)
class StorageDetail:
	def __init__(self): pass
	def up(self, context): context.changeState(StorageDetail)
	def down(self, context):context.changeState(StorageDetail)
	def left(self, context):context.changeState(StorageState)
class BatteryState:
	def __init__(self): pass
	def up(self, context): context.changeState(StorageState)
	def down(self, context):context.changeState(HomeState)
class Context:
	def __init__(self): raise NotImplementedError
	def changeState(self, screenState): raise NotImplementedError

import sys
from threading import Timer
class LCD(Context):
	def __init__(self):
		self.state = HomeState()
	def changeState(self, screenState):
		self.state = screenState

from time import sleep
def main():
	lcd = LCD()
	while True:

class State(object):
	def change_state(self, direction):
		if direction == UP:
			self.up()

	def up(self):
		raise NotImplementedError

	def down(self):
		raise NotImplementedError

	def left(self):
		raise NotImplementedError

	def right(self):
		raise NotImplementedError

class NetworkState(State):
	def __init__(self):
		display.firstLine("IP Adress")
		display.secondLine(localtime) 

	def up(self):
		return HomeState()
	def 

if __name__=='__main__': #main()
	state = HomeState()

	while True:
		if stick_on(stick_direction):
			state = state.change_state(stick_direction)
