from deque import Deque #line:1
import unittest #line:2
import time #line:3
class TestDequeMethods (unittest .TestCase ):#line:5
   def test_init (O0OOOO00O00000000 ):#line:6
      OO0O000OO00OOOO00 =Deque ()#line:7
      O0OOOO00O00000000 .assertTrue (OO0O000OO00OOOO00 .get_size ()==0 )#line:8
   def test_isEmpty (OOO0O00000OO00OOO ):#line:10
      OO0OOO000O0OOOO00 =Deque ()#line:11
      OOO0O00000OO00OOO .assertTrue (OO0OOO000O0OOOO00 .isEmpty ())#line:12
   def test_addFirstToEmpyList (OO0OOO0O0OOO0O00O ):#line:14
      OOO00OOOO00OO0O0O =Deque ()#line:15
      OOO00OOOO00OO0O0O .addFirst (1 )#line:16
      OO0OOO0O0OOO0O00O .assertFalse (OOO00OOOO00OO0O0O .isEmpty ())#line:17
      OO0OOO0O0OOO0O00O .assertTrue (OOO00OOOO00OO0O0O .removeFirst ()==1 )#line:18
   def test_addFirst (O0O0O000OO0000OOO ):#line:20
      O000OOO000OOO0O0O =Deque ()#line:21
      O000OOO000OOO0O0O .addFirst (1 )#line:22
      O000OOO000OOO0O0O .addFirst (2 )#line:23
      O0O0O000OO0000OOO .assertTrue (O000OOO000OOO0O0O .removeFirst ()==2 )#line:24
      O0O0O000OO0000OOO .assertTrue (O000OOO000OOO0O0O .removeFirst ()==1 )#line:25
   def test_addLast (OOOOO0OOOO00O00O0 ):#line:27
      OOO0O00O00000000O =Deque ()#line:28
      OOO0O00O00000000O .addLast (1 )#line:29
      OOO0O00O00000000O .addLast (2 )#line:30
      OOOOO0OOOO00O00O0 .assertTrue (OOO0O00O00000000O .removeLast ()==2 )#line:31
      OOOOO0OOOO00O00O0 .assertTrue (OOO0O00O00000000O .removeLast ()==1 )#line:32
   def test_addLastToEmptyList (OOO00O000000O00OO ):#line:34
      O0OOOOO00O000O00O =Deque ()#line:35
      O0OOOOO00O000O00O .addLast (2 )#line:36
      OOO00O000000O00OO .assertFalse (O0OOOOO00O000O00O .isEmpty ())#line:37
      OOO00O000000O00OO .assertTrue (O0OOOOO00O000O00O .removeLast ()==2 )#line:38
   def test_removeFirst (OO00OO0O00000O0OO ):#line:40
      O0OO000OO00OOO000 =Deque ()#line:41
      O0OO000OO00OOO000 .addFirst (1 )#line:42
      O0OO000OO00OOO000 .addLast (2 )#line:43
      OO00OO0O00000O0OO .assertTrue (O0OO000OO00OOO000 .get_size ()==2 )#line:44
      OO0000O0OO0000OO0 =O0OO000OO00OOO000 .removeFirst ()#line:45
      OO00OO0O00000O0OO .assertTrue (OO0000O0OO0000OO0 ==1 )#line:46
   def test_removeLast (O00OO000OO0OO00O0 ):#line:48
      OOOOOOO0O00OOOOO0 =Deque ()#line:49
      OOOOOOO0O00OOOOO0 .addFirst (1 )#line:50
      OOOOOOO0O00OOOOO0 .addFirst (0 )#line:51
      OOOOOOO0O00OOOOO0 .addLast (2 )#line:52
      OOOOOOO0O00OOOOO0 .addLast (3 )#line:53
      O00OO000OO0OO00O0 .assertEqual (OOOOOOO0O00OOOOO0 .get_size (),4 )#line:54
      OOOOO000OOOOO0OO0 =OOOOOOO0O00OOOOO0 .removeLast ()#line:55
      O00OO000OO0OO00O0 .assertEqual (OOOOO000OOOOO0OO0 ,3 )#line:56
      OOOOO000OOOOO0OO0 =OOOOOOO0O00OOOOO0 .removeLast ()#line:57
      O00OO000OO0OO00O0 .assertEqual (OOOOO000OOOOO0OO0 ,2 )#line:58
      OOOOO000OOOOO0OO0 =OOOOOOO0O00OOOOO0 .removeLast ()#line:59
      O00OO000OO0OO00O0 .assertEqual (OOOOO000OOOOO0OO0 ,1 )#line:60
      OOOOO000OOOOO0OO0 =OOOOOOO0O00OOOOO0 .removeLast ()#line:61
      O00OO000OO0OO00O0 .assertEqual (OOOOO000OOOOO0OO0 ,0 )#line:62
   def test_removeEmpty (OOO00O0OOO000OO00 ):#line:64
      O000OOOOO0O0O0O0O =Deque ()#line:65
      OOO00O0OOO000OO00 .assertEqual (O000OOOOO0O0O0O0O .removeFirst (),None )#line:66
      OOO00O0OOO000OO00 .assertEqual (O000OOOOO0O0O0O0O .removeLast (),None )#line:67
   def test_iterator (OOOOOOOOOO000000O ):#line:69
      OOOO0OOO000000O00 =Deque ()#line:70
      OOOO0OOO000000O00 .addFirst (3 )#line:71
      OOOO0OOO000000O00 .addFirst (2 )#line:72
      OOOO0OOO000000O00 .addFirst (1 )#line:73
      OO0OO0O0O0OOOO000 =OOOO0OOO000000O00 .iterator ()#line:74
      OO000O000OOO0O0OO =1 #line:75
      for OOOO0OOO000000O00 in OO0OO0O0O0OOOO000 :#line:76
         OOOOOOOOOO000000O .assertEqual (OO000O000OOO0O0OO ,OOOO0OOO000000O00 )#line:77
         OO000O000OOO0O0OO +=1 #line:78
   def test_stress_test (O00OO0O0OOOO000O0 ):#line:80
      O000O0O0O0O0O0OO0 =Deque ()#line:81
      O00OOO0O000O0000O =time .time ()#line:82
      OO000O00O0O0OO000 =200000 #line:83
      for OO0OO0O0OOO00O0OO in range (OO000O00O0O0OO000 ):#line:84
         if OO0OO0O0OOO00O0OO %2 ==0 :#line:85
            O000O0O0O0O0O0OO0 .addFirst (OO0OO0O0OOO00O0OO )#line:86
         else :#line:87
            O000O0O0O0O0O0OO0 .addLast (OO0OO0O0OOO00O0OO )#line:88
      for OO0OO0O0OOO00O0OO in range (OO000O00O0O0OO000 +100 ):#line:90
         if OO0OO0O0OOO00O0OO %2 ==0 :#line:91
            O000O0O0O0O0O0OO0 .removeLast ()#line:92
         else :#line:93
            O000O0O0O0O0O0OO0 .removeFirst ()#line:94
      O00OO0O0OOOO000O0 .assertEqual (True ,time .time ()-O00OOO0O000O0000O <1 )#line:95
if __name__ =='__main__':#line:97
   unittest .main ()#line:98
