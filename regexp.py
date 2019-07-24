# Python program for fetching emails from string, even surrounded
# by characters.
# Kendall Jackson 2019

import re 

# Example string 
text = 'Hello from >kendallwinsatlife@gmail.com< to >mailto:kendallisbest@yahoo.com< about the meeting @2PM'


# + for Repeats a character one or more times 
email = re.findall('[\w.]+@[\w.]+', text)

# Printing of List 
print(email) 
