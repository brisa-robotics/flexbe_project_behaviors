#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from lona_flexbe_states.tts_state import TTSState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Tue Feb 13 2018
@author: Synapticon GmbH
'''
class ExampleBehaviorSM(Behavior):
    '''
    This is a simple example for a behavior.
    '''


    def __init__(self):
        super(ExampleBehaviorSM, self).__init__()
        self.name = 'Example Behavior'

        # parameters of this behavior

        # references to used behaviors

        # Additional initialization code can be added inside the following tags
        # [MANUAL_INIT]
		
		# [/MANUAL_INIT]

        # Behavior comments:

        # O 411 144 
        # This transition will only be executed if the Autonomy Level is greater than Low during execution, e.g. High



    def create(self):
        # x:617 y:333, x:239 y:358
        _state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
        _state_machine.userdata.undock_backward_dist = 0.5
        _state_machine.userdata.undock_inplace_rot_angle = 0.0

        # Additional creation code can be added inside the following tags
        # [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


        with _state_machine:
            # x:30 y:40
            OperatableStateMachine.add('tts',
                                        TTSState(text='Hello world'),
                                        transitions={'done': 'finished', 'failed': 'failed'},
                                        autonomy={'done': Autonomy.Off, 'failed': Autonomy.Off})


        return _state_machine


    # Private functions can be added inside the following tags
    # [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
