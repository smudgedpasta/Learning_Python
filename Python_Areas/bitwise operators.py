'''
Every 0 and 1 in binary is a bit. 8-bit == 1 byte.
Binary are like booleans in a way, 0 being False and 1 being True.

12 = 0000000000001100
22 = 0000000000010110

In python, and means that both conditions need to be True for it to equate to True.
or means only one of the conditions need to be True for it to equate to True.
Its similar logic with Bitwise Operators.
'''

# & = Bitwise and. It compares two binary numbers, and if both values are 1, it becomes 1. Otherwise it becomes 0.
# | = Bitwise or. Comparing two binary numbers, if one is 1 and the other is 0, it becomes 1. Two 1's still become 1.
# ^ = Bitwise XOR. It works the same was as Bitwise or, only when both values are 1, it becomes False 0.
# << = Bitwise left shift. It does not compare two binary numbers, it shifts the binary numbers to the left.
#      (Note that you don't keep the same length on the binary number. Its more like appending two 0's to the end.)
# >> = Bitwise right shift. It works the same as left shift, only shifting the binary numbers to the right.
#      (Note the same as left shift, you don't really work on the same length for the line. This is more like removing bits.

'''
(12 & 22)
12 = 0000000000001100
22 = 0000000000010110
 & = 0000000000000100

(12 | 22)
12 = 0000000000001100
22 = 0000000000010110
 | = 0000000000011110

(12 ^ 22)
12 = 0000000000001100
22 = 0000000000010110
 ^ = 0000000000011010

(12 << 2)
12 = 0000000000001100
<< = 000000000000110000

(12 >> 2)
12 = 0000000000001100
>> = 00000000000011
'''