# Imagine Gift Box, by opening if we have another gift box and so on untill gift arrive

# Psuedo Code
"""
def open_gift_box():
    if ball:
        return box
    open_gift_box()
    
"""

# Call stack

def Three():
    print('THREE')

def Two():
    Three()
    print('TWO')

def First():
    Two()
    print('ONE')

First() # Eventhough we call First, it will print THREE,TWO and ONE # Note To see call stack RUN Debug mode