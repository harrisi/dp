#!/usr/bin/python
import time

def do_timer(current, f):
  while True:
    _input = raw_input('')
    if _input in 'lL':
      lap_time = time.time() - current
      print('lap time: ' + str(lap_time))
      f.write('  lap time: ' + str(lap_time) + '\n')
      continue
    elif _input in 'sS':
      return time.time()

if __name__ == '__main__':
  _input = raw_input('Press `s` to start, `l` for a lap, or `s` again to stop.\n')
  if _input in 'sS':
    start_time = time.time() # current time
    with open('ignore.timer', 'a') as f:
      print('Timer started at ' + str(start_time))
      f.write('Timer started at ' + str(start_time) + '\n')
      total_time = do_timer(start_time, f)
      print('total time: ' + str(total_time - start_time))
      f.write('total time: ' + str(total_time - start_time) + '\n\n')
