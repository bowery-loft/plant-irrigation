import hassapi as hass
import time
from datetime import datetime

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
    self.log('Feed me Seymore!')

  ##################
  # Button Actions #
  ##################

  def on(self):
    self.turn_on(self.args['entity'])

  def off(self):
    self.turn_off(self.args['entity'])

  ####################
  # Input Validation #
  ####################

  # def validate(self):

  #   # sensor
  #   if type(self.args.get('sensor', False)) != str:
  #     raise ValueError('sensor must be a defined string')
  #   if self.args['sensor'].split('.')[0] != 'sensor':
  #     raise ValueError('sensor is invalid, example: sensor.my_pico')