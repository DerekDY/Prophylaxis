from MCP23017_I2C import *
from Expander import *

expander = Expander(0x25)

#for x in range(16):
#	expander.setup(x, 'OUT')

#for x in range(16):
#	print(expander.output(x, 'HIGH'))

for x in range(16):
	expander.setup(x, 'IN')

for x in range(16):
	print(expander.input(x))
