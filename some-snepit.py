
'''
 - from https://www.toptal.com/python/python-design-patterns
 
  chekc the interface , also check the lib version (new version does not break something)
'''
try:
    bird.quack()
except AttributeError:
    self.lol()
    
    
    
'''
class User(Object):
    pass
'''
class User(Object):
    _persist_methods = ['get', 'save', 'delete']

    def __init__(self, persister):
        self._persister = persister

    def __getattr__(self, attribute):
        if attribute in self._persist_methods:
            return getattr(self._persister, attribute)
            

'''
 chain
'''
class ContentFilter(object):
    def __init__(self, filters=None):
        self._filters = list()
        if filters is not None:
            self._filters += filters

    def filter(self, content):
        for filter in self._filters:
            content = self.filter(content)
        return content

aContentFilter = ContentFilter([
                offensive_filter,
                ads_filter,
                porno_video_filter])
filtered_content = aContentFilter.filter(content)



'''
command
'''
class RenameFileCommand(object):
    def __init__(self, from_name, to_name):
        self._from = from_name
        self._to = to_name

    def execute(self):
        os.rename(self._from, self._to)

    def undo(self):
        os.rename(self._to, self._from)

class History(object):
    def __init__(self):
        self._commands = list()

    def execute(self, command):
        self._commands.append(command)
        command.execute()

    def undo(self):
        self._commands.pop().undo()

history = History()
history.execute(RenameFileCommand('docs/cv.doc', 'docs/cv-en.doc'))
history.execute(RenameFileCommand('docs/cv1.doc', 'docs/cv-bg.doc'))
history.undo()
history.undo()


'''
sigleton
These are the alternatives to using a Singleton in Python:

Use a module.
Create one instance somewhere at the top-level of your application, perhaps in the config file.
Pass the instance to every object that needs it. That’s a dependency injection and it’s a powerful and easily mastered mechanism
'''
class Logger(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_logger'):
            cls._logger = super(Logger, cls
                    ).__new__(cls, *args, **kwargs)
        return cls._logger
        
'''
Dependency Injection
'''

class Command:

    def __init__(self, authenticate=None, authorize=None):
        self.authenticate = authenticate or self._not_authenticated
        self.authorize = authorize or self._not_autorized

    def execute(self, user, action):
        self.authenticate(user)
        self.authorize(user, action)
        return action()

if in_sudo_mode:
    command = Command(always_authenticated, always_authorized)
else:
    command = Command(config.authenticate, config.authorize)
command.execute(current_user, delete_user_action)



'''
faced
'''
class Car(object):

    def __init__(self):
        self._tyres = [Tyre('front_left'),
                             Tyre('front_right'),
                             Tyre('rear_left'),
                             Tyre('rear_right'), ]
        self._tank = Tank(70)

    def tyres_pressure(self):
        return [tyre.pressure for tyre in self._tyres]

    def fuel_level(self):
        return self._tank.level
        
        
'''
adaptor
'''

import socket

class SocketWriter(object):

    def __init__(self, ip, port):
        self._socket = socket.socket(socket.AF_INET,
                                     socket.SOCK_DGRAM)
        self._ip = ip
        self._port = port

    def write(self, message):
        self._socket.send(message, (self._ip, self._port))

def log(message, destination):
    destination.write('[{}] - {}'.format(datetime.now(), message))

upd_logger = SocketWriter('1.2.3.4', '9999')
log('Something happened', udp_destination)


'''
Decorator
'''

def autheticated_only(method):
    def decorated(*args, **kwargs):
        if check_authenticated(kwargs['user']):
            return method(*args, **kwargs )
        else:
            raise UnauthenticatedError
    return decorated


def authorized_only(method):
    def decorated(*args, **kwargs):
        if check_authorized(kwargs['user'], kwargs['action']):
            return method(*args, **kwargs)
        else:
            raise UnauthorizedError
    return decorated


@authorized_only
@authenticated_only
def execute(action, *args, **kwargs):
    return action()
    
'''
It is important to note that you are not limited to functions as decorators. A decorator may involve entire classes. The only requirement is that they must be callables. But we have no problem with that; we just need to define the __call__(self) method.

You may also want to take a closer look at Python’s functools module. There is much to discover there!
'''

'''
content management
'''

class CustomOpen(object):
    def __init__(self, filename):
        self.file = open(filename)

    def __enter__(self):
        return self.file

    def __exit__(self, ctx_type, ctx_value, ctx_traceback):
        self.file.close()

with CustomOpen('file') as f:
    contents = f.read()
  

'''
use generator and context lib
'''
from contextlib import contextmanager

@contextmanager
def custom_open(filename):
    f = open(filename)
    try:
        yield f
    finally:
        f.close()

with custom_open('file') as f:
    contents = f.read()

  
'''
Python is dynamically typed, which means that variables do not have a fixed type. 

'''
a= 1
a = []

'''
The enumerate() function adds a counter to an iterable.
>>> elements = ('foo', 'bar', 'baz')
>>> for elem in elements:
...     print elem
... 
foo
bar
baz
>>> for count, elem in enumerate(elements):
...     print count, elem
... 
0 foo
1 bar
2 baz
'''

'''
Comprehensions are constructs that allow sequences to be built from other sequences. Python 2.0 introduced list comprehensions and Python 3.0 comes with dictionary and set comprehensions.

List Comprehensions
A list comprehension consists of the following parts:

An Input Sequence.
A Variable representing members of the input sequence.
An Optional Predicate expression.
An Output Expression producing elements of the output list from members of the Input Sequence that satisfy the predicate.
'''


'''
class method decorator
'''

from pageutils import formatHeader

myPage(object):
   def __init__(self):
      self.PageName = ''

   def createPage(self):
      pageHeader = self.createHeader()

   @formatHeader   #<----- decorator
   def createHeader(self):
       return "Page Header ",self.PageName

if __name__=="__main__":
   page = myPage()
   page.PageName = 'My Page'
   page.createPage()

#------- pageutils.py --------------------

def formatHeader(fn):
   def wrapped(self=None):
       return '<div class="page_header">'+fn(self)+'</div>'
   return wrapped
  
  
  
# generator version
def fibon(n):
    a = b = 1
    for i in xrange(n):
        yield a
        a, b = b, a + b
      
      
 '''
  set behave mostly like lists with the distinction that they can not contain duplicate values.
 '''
 
 
 '''
 generator .send  === coroutine
 
 '''
 
 def grep(pattern):
    print("Searching for", pattern)
    while True:
        line = (yield)
        if pattern in line:
            print(line)

search = grep('coroutine')
next(search)
# Output: Searching for coroutine
search.send("I love you")
search.send("Don't you love me?")
search.send("I love coroutines instead!")
# Output: I love coroutines instead!
search.close()
