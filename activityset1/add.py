
''''def f():
  a=10
  def g():
    print(a)
  return g
x = f()
x()'''

#output: 10 //value of x in enclosed scope, called closure. comes from the culture of perl.


''''import sys
print(sys.path) '''

#output: ['/home/runner/python2022/activityset1', '/opt/virtualenvs/python3/lib/python3.8/site-packages', '/usr/lib/python38.zip', '/usr/lib/python3.8', '/usr/lib/python3.8/lib-dynload']


'''def f(*args, **kwargs):
  print(args,kwargs)
f(1,2,3,a=2,b=3) '''

#output:    (1, 2, 3) {'a': 2, 'b': 3}  //arguments by args and dictionary by kwargs 