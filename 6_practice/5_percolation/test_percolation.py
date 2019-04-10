import unittest #line:1
from percolation import Percolation #line:2
from percolation_stats import PercolationStats #line:3
import time #line:4
class TestSolution (unittest .TestCase ):#line:7
	def test_percolation (O0OO00O0OO0O000O0 ):#line:8
		O00O0OOO0OO0O00OO =Percolation (3 )#line:10
		O00O0OOO0OO0O00OO .open (0 ,0 )#line:11
		O00O0OOO0OO0O00OO .open (1 ,0 )#line:12
		O00O0OOO0OO0O00OO .open (2 ,2 )#line:13
		O0OO00O0OO0O000O0 .assertFalse (O00O0OOO0OO0O00OO .percolates ())#line:14
		O00O0OOO0OO0O00OO .open (2 ,0 )#line:15
		O0OO00O0OO0O000O0 .assertTrue (O00O0OOO0OO0O00OO .percolates ())#line:16
		O0OO00O0OO0O000O0 .assertFalse (O00O0OOO0OO0O00OO .isOpen (0 ,2 ))#line:17
		O0OO00O0OO0O000O0 .assertTrue (O00O0OOO0OO0O00OO .isFull (1 ,0 ))#line:18
	def test_runtime (OO0O0O00O0000OOO0 ):#line:21
		OO00OOO0OOOOOOOOO =30 #line:22
		O0O0O000000O000O0 =15 #line:23
		OOO0OO000O0OO0O00 =Percolation (OO00OOO0OOOOOOOOO )#line:25
		O0OOOO0OO0O0OOO00 =time .clock ()#line:26
		for O000O00O0O0O0O0O0 in range (OO00OOO0OOOOOOOOO ):#line:27
			for O00O00OOO00OO0000 in range (OO00OOO0OOOOOOOOO ):#line:28
				OOO0OO000O0OO0O00 .open (O000O00O0O0O0O0O0 ,O00O00OOO00OO0000 )#line:29
				if O000O00O0O0O0O0O0 !=OO00OOO0OOOOOOOOO -1 :#line:30
					OO0O0O00O0000OOO0 .assertFalse (OOO0OO000O0OO0O00 .percolates ())#line:31
				else :#line:32
					OO0O0O00O0000OOO0 .assertTrue (OOO0OO000O0OO0O00 .percolates ())#line:33
		OO000OO0O000OO00O =time .clock ()#line:34
		O0OO0O00O0O00OOO0 =(OO000OO0O000OO00O -O0OOOO0OO0O0OOO00 )#line:35
		OOO0OO000O0OO0O00 =Percolation (OO00OOO0OOOOOOOOO *10 )#line:37
		O0OOOO0OO0O0OOO00 =time .clock ()#line:38
		for O000O00O0O0O0O0O0 in range (OO00OOO0OOOOOOOOO *10 ):#line:39
			for O00O00OOO00OO0000 in range (OO00OOO0OOOOOOOOO *10 ):#line:40
				OOO0OO000O0OO0O00 .open (O000O00O0O0O0O0O0 ,O00O00OOO00OO0000 )#line:41
				if O000O00O0O0O0O0O0 !=OO00OOO0OOOOOOOOO *10 -1 :#line:42
					OO0O0O00O0000OOO0 .assertFalse (OOO0OO000O0OO0O00 .percolates ())#line:43
				else :#line:44
					OO0O0O00O0000OOO0 .assertTrue (OOO0OO000O0OO0O00 .percolates ())#line:45
			OO0O0O00O0000OOO0 .assertTrue (time .clock ()-O0OOOO0OO0O0OOO00 <(O0OO0O00O0O00OOO0 *100 +O0OO0O00O0O00OOO0 *O0O0O000000O000O0 ),"RUNTIME EXCEEDED")#line:47
	def test_percolation_stats (O00OO00O0OOO00O00 ):#line:49
		OO00O0000O0O0O00O =PercolationStats (50 ,100 )#line:50
		O00OO00O0OOO00O00 .assertTrue (OO00O0000O0O0O00O .mean ()<0.7 )#line:51
		O00OO00O0OOO00O00 .assertTrue (0.5 <OO00O0000O0O0O00O .mean ())#line:52
if __name__ =='__main__':#line:55
	unittest .main ()#line:56
