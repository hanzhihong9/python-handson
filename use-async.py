'''
con-currency

1 multi processes -- only  Cpython can do
2 multi thread  -- GIL   make concurrency but not make it be fast


aysnc await
'''

'''
suspend and resume

1 Callback
2 generator 
3 async and await
4 greenlets package
5 event loop

'''

import asyncio

loop  = asyncio.get_event_loop()

@asyncio.coroutine
def hello():
  print 1
  yield from asyncio.sleep(3)
  print 'done'


asunc def hello2():
  print 1
  await asyncio.sleep(3)
  print 'done'

if  __name__ == '__main__'
  loop  = asyncio.run_until_complete( hello() )
  
  
  
