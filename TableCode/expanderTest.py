from MCP23017 import MCP23017
import quick2wire

exp = MCP23017.MCP23017(0x25, 1)

for x in range(16):
	expander = MCP23017.PortManager(exp, 0x00, x)
	print(expander.digital_read())
	
print(exp.read(0x09))
