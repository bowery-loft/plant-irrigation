import hassapi as hass
import time
from datetime import datetime
from croniter import croniter

#
# App to control a plant irrigation system
#
# 
#
# State IDs

class PlantIrrigation(hass.Hass):

  ##############
  # Initialize #
  ##############

  def initialize(self):
    # self.validate()
    while True:
      self.time_trigger()
      time.sleep(1)

  ###########
  # Handler #
  ###########

  def time_trigger(self):
    switch       = self.args['switch']
    cron         = self.args['cron']
    duration     = self.args['duration']
    base         = datetime(2010, 1, 25, 4, 46)
    itr          = croniter(cron, base)
    prev_time    = itr.get_prev(datetime)
    end_time     = prev_time + datetime.timedelta(seconds=duration)
    current_time = datetime.now()
    
    if current_time >= prev_time and current_time <= end_time:
      self.turn_on(switch)
    else:
      self.turn_off(switch)

  ##################``
  # Button Actions #
  ##################

  ####################
  # Input Validation #
  ####################

  # def validate(self):

  #   # sensor
  #   if type(self.args.get('sensor', False)) != str:
  #     raise ValueError('sensor must be a defined string')
  #   if self.args['sensor'].split('.')[0] != 'sensor':
  #     raise ValueError('sensor is invalid, example: sensor.my_pico')