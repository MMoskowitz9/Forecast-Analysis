import time 
from Wunderground_pull import Wunderground_pull
from Analyze_Data import Analyze_Data

class timer:

	listofCities = [("New_York",'NY'),("Los_Angeles","CA"),("Ardmore","PA"),("Honolulu","HI"),("Boulder","CO"),("Aurora","CO")]
	listofobservers = []
	def _init_(self):
		pass
		
	def attach(self, observer):
		self.listofobservers.append(observer)
		
	def Notify(self):
		for o in self.listofobservers:
			o.update(self.listofCities)
	
	def monitorDate(self):
		#currentDate = (time.strftime("%d/%m/%Y"))
		#print 'going to sleep soon test'

		while(1):
			#self.__update()
			#time.sleep(86400)
			self.Notify()
			time.sleep(86400/2)
			
			
t = timer()
observer1 = Wunderground_pull("Wunderground")
observer2 = Analyze_Data()
t.attach(observer1)
t.attach(observer2)
t.monitorDate()
		

