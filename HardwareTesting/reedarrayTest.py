'''
File: reedarrayTest.py
Description: This file analyzes a reed switch array connected via
    Raspberry Pi GPIO, and creates and prints a matrix containing 0s
    for open reed switches and 1s for closed reed switches in the array

Authors:  Alexis Bonnema and Paul Brouwer
Purpose:  Prophylaxis Senior Design
Date:     12/09/15
'''

#language:Python
# External module imports
import RPi.GPIO as GPIO

# Constants
NUM_ROWS = 3
NUM_COLUMNS = 2

# Pin Definitons
rows = [17, 27]
# 17 = Broadcom pin 17 = PI pin 11
# 27 = PI pin 13
columns = [5, 6] # 5 = bit 0, 6 = bit 1 for decoder
# 5 = PI pin 29
# 6 = PI pin 31

# Matrix Setup
resultsM = [[0 for i in xrange(NUM_COLUMNS)] for i in xrange(NUM_ROWS)]

# Pin Setup
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme

for row in rows:
    GPIO.setup(row, GPIO.OUT)
for col in columns:
    GPIO.setup(col, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # pull-down resistor

# Start testing at row 0
rowIdx = 0
# Loop until every row is tested
while rowIdx < NUM_ROWS:
    # send row code to one-hot decoder
    for i, rowBit in enumerate(rows):
        # use bitwise AND to set output row code
        if rowIdx & (2 ** i):
            GPIO.output(rowBit, GPIO.HIGH)
        else:
            GPIO.output(rowBit, GPIO.LOW)
    # check which columns are high
    for colIdx, col in enumerate(columns):
        if GPIO.input(col):
            print "piece at", rowIdx, colIdx
            resultsM[rowIdx][colIdx] = 1
        else:
            print "no piece at", rowIdx, colIdx
            resultsM[rowIdx][colIdx] = 0
    # increment number of row to test
    rowIdx += 1

# Print matrix
print ' ',
for i in range(len(resultsM[1])):
    print i,
print
for i, element in enumerate(resultsM):
    print i,
    for item in element:
        print item,
    print
	
# Print message that code is finished
print("Done")
