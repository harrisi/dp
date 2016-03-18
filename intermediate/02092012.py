#!/usr/bin/python
from pprint import pprint
# global list of events
events = []

def do_edit():
  global events
  which = int(raw_input('which would you like to edit? (number): '))
  if which < len(events):
    print('old #' + str(which) + ':')
    print('event: ' + str(events[which][0]))
    print('time: ' + str(events[which][1]))
    #print('change to:')
    event = raw_input('change event:\n')
    time = raw_input('change time: ')
    events[which] = [event, time]
  else:
    print('out of range')

def do_add():
  global events
  event = raw_input('enter event: ')
  time = raw_input('enter time for event: ')
  events.append([event, time])

def do_delete():
  global events
  which = int(raw_input('delete which? '))
  if which < len(events):
    temp_l = events[:which]
    temp_r = events[which+1:]
    events = temp_l + temp_r
  else:
    print('out of range')

def do_list():
  global events
  pprint(events)

if __name__ == '__main__':
  while True:
    func = raw_input('(e)dit, (a)dd, (d)elete, (l)ist, (q)uit; ')
    if func not in 'eEaAdDlLqQ':
      print('unknown command "' + func + '"')
      continue
    if func in 'eE':
      do_edit()
    elif func in 'aA':
      do_add()
    elif func in 'dD':
      do_delete()
    elif func in 'lL':
      do_list()
    elif func in 'qQ':
      print('quitting')
      break
    else:
      print('somehow unknown error')
