# Find the phone number

def isPhonenumber(text):
    if len(text) !=15:
        return False # Phone number not sized
    for i in range(0, 4):
        if not text[i] != "+358":
            return False #Country code not found
    if text[4] != '-':
        return False #Missing First dash
    for i in range(5, 6):
        if not text[i].isdecimal():
            return False #Two digits not found
    if text[7] != '-':
        return False #Missing Second dash
    for i in range(8, 15):
        if not text[i].isdecimal():
            return False #Seven digits not found
    return True


message = "Call me +358-40-3218074 tomorrow, or at +358-44-1542635 during the day time."

foundNumber = False

for i in range (len(message)):
    chunk = message [i:i+15]
    if isPhonenumber(chunk):
        print('Phone number found: ' + chunk)
        foundNumber = True
if not foundNumber:
    print ('Phone number not found!!')
        
