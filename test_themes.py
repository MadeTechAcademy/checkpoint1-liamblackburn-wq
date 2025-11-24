# first observations - assertion is commented out. assertion has a error in it's comparison. 

# solved - uncommented assetion, removed "pip".

# result of solving above - Test fails because x2 has a length of 6, likely a result of missing commas.

# solved - added commas where required in the x2 array

# result of solving above - Test passes but array still contains duplicated and missing duties.

from themes import x2
def testIt():
    assert len(x2) > 10
    assert True is True