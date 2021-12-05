from transport import *

firstcab  = Cab('Sandy', 80,'Dubai', 1200,3)
secondcab  = Cab('Mandy', 60,'Sharjah', 1890,5)

print("\n\t\t\t\t  *** PUBLIC TRANSPORT DETAILS ***")
print('\n\nFirst cab: ',  firstcab.__str__())
print('Second cab: ', secondcab.__str__())


from transport import *

Tram1  = Tram('Jumeirah Tram ', 1.4,'JBR', 33)
Tram2  = Tram('Marina Tram', 2,' Al Sufouh', 37)

print('\nTram1:',  Tram1.__str__())
print('Tram2: ', Tram2.__str__())


from transport import *

RTA_bus1 = RTAbus( "Busno.83" ,1.6 , 'AlNahda Bus Stop',  13)
RTA_bus2 = RTAbus( 'Busno.15',1.4, 'AlRaffa Bus Stop', 25)
 
print('\nRTA_bus1: ' ,  RTA_bus1.__str__())
print('RTA_bus2: ' ,  RTA_bus2.__str__())

from transport import *

EXPO1 = EXPO("EXPOBus1" ,11.2 , 'Sustainability GATE',  133)
EXPO2 = EXPO('EXPOBus2',11.3, 'Mobility GATE', 251)

print('\n\t','>',EXPO1.__str__())
print('\n\t','>',EXPO2.__str__())

