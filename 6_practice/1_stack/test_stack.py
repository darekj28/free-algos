import unittest #line:1
from stack import Stack #line:2
import time #line:3
class TestSolution (unittest .TestCase ):#line:5
	def test_empty_stack (OO0OO0OOO000O00O0 ):#line:6
		O00OOOOOOO0O0OO00 =Stack ()#line:7
		OO0OO0OOO000O00O0 .assertTrue (O00OOOOOOO0O0OO00 .isEmpty ())#line:8
	def test_one_through_five (OO0O00OO0O0O0000O ):#line:10
		OO00OO0OOOO00O00O =Stack ()#line:11
		OO0O00OO0O0O0000O .assertTrue (OO00OO0OOOO00O00O .isEmpty ())#line:12
		OO00OO0OOOO00O00O .push (1 )#line:13
		OO0O00OO0O0O0000O .assertEqual (OO00OO0OOOO00O00O .size (),1 )#line:14
		OO0O00OO0O0O0000O .assertFalse (OO00OO0OOOO00O00O .isEmpty ())#line:15
		OO0O00OO0O0O0000O .assertEqual (OO00OO0OOOO00O00O .pop (),1 )#line:16
		OO0O00OO0O0O0000O .assertTrue (OO00OO0OOOO00O00O .isEmpty ())#line:17
		OO00OO0OOOO00O00O .push (2 )#line:19
		OO00OO0OOOO00O00O .push (3 )#line:20
		OO00OO0OOOO00O00O .push (4 )#line:21
		OO0O00OO0O0O0000O .assertEqual (OO00OO0OOOO00O00O .size (),3 )#line:23
		OO0O00OO0O0O0000O .assertEqual (OO00OO0OOOO00O00O .peek (),4 )#line:24
		OO0O00OO0O0O0000O .assertEqual (OO00OO0OOOO00O00O .pop (),4 )#line:25
		OO0O00OO0O0O0000O .assertEqual (OO00OO0OOOO00O00O .size (),2 )#line:26
		OO0O00OO0O0O0000O .assertEqual (OO00OO0OOOO00O00O .pop (),3 )#line:27
		OO00OO0OOOO00O00O .push (5 )#line:28
		OO0O00OO0O0O0000O .assertFalse (OO00OO0OOOO00O00O .isEmpty ())#line:29
		OO0O00OO0O0O0000O .assertEqual (OO00OO0OOOO00O00O .pop (),5 )#line:30
		OO0O00OO0O0O0000O .assertEqual (OO00OO0OOOO00O00O .pop (),2 )#line:31
		OO0O00OO0O0O0000O .assertTrue (OO00OO0OOOO00O00O .isEmpty ())#line:32
		OO0O00OO0O0O0000O .assertEqual (OO00OO0OOOO00O00O .pop (),None )#line:33
	def test_stress_test (OO00000OO0OOO00O0 ):#line:35
		O0O00O0O00O0OOOOO =500000 #line:36
		OO00O00OO0OO00O00 =time .time ()#line:37
		OOOO0OOO0000O00O0 =Stack ()#line:38
		for O00OOO0O0O000OOO0 in range (O0O00O0O00O0OOOOO ):#line:39
			OOOO0OOO0000O00O0 .push (O00OOO0O0O000OOO0 )#line:40
			OOOO0OOO0000O00O0 .pop ()#line:41
		OO00000OO0OOO00O0 .assertEqual (True ,time .time ()-OO00O00OO0OO00O00 <1.25 )#line:42
if __name__ =='__main__':#line:44
	unittest .main ()#line:45
