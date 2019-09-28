class OnePingOnlyPleaseVassily( object ):
    def __init__( self ):
        self.value= None
    def set( self, value ):
        if self.value is not None:
            raise Exception( "Already set.")
        self.value= value

someStateMemo= OnePingOnlyPleaseVassily()
someStateMemo.set( 10 ) # works
someStateMemo.set( 15 ) # fails

"""
sh-4.3$ python main.py
Traceback (most recent call last):
  File "main.py", line 11, in <module>
    someStateMemo.set( 15 ) # fails
  File "main.py", line 6, in set
    raise Exception( "Already set.")
Exception: Already set.
"""