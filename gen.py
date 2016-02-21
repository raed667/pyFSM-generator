# -*- coding: utf-8 -*-

"""
-------------------------------------------------------------------------------
 Name:          <gen.py>
 Model:         A generated Python FSM DEVS model
 Authors:       Raed Chammam
 Organization:  unice Polytech Sophia
 Date:          21/02/2016 13:50:39
 License:       GPL
-------------------------------------------------------------------------------
"""

### Specific import ------------------------------------------------------------
from DomainInterface.DomainBehavior import DomainBehavior
from DomainInterface.Object import Message


### Model class ----------------------------------------------------------------
class MiddleSample(DomainBehavior):
    ''' DEVS Class for MiddleSample model
    '''

    def __init__(self):
        ''' Constructor.
        '''
        DomainBehavior.__init__(self)

        self.state = {'status': 'IDLE', 'sigma': INFINITY}
        self.proc = 0
        self.x = {}
        self.y = {}
        self.pos = [-1] * 100

        ''' The object '''
        self.objectName = ClassName()
        # The states go below
        states = [
			State(name='off'),
			State(name='on')
		]

        # The transition go below
        transitions = [
			{'trigger': '1', 'source': 'off', 'dest': 'on'},
			{'trigger': '0', 'source': 'on', 'dest': 'off'}
		]

        # Initialize below
        machine = Machine(self.objectName, states=self.states, transitions=self.transitions, initial='off')

    def extTransition(self):
        ''' DEVS external transition function.
        '''
        for i in xrange(len(self.IPorts)):
            msg = self.peek(self.IPorts[i])
            if msg:
                print "---- EXTERNAL " + str(msg) + " ----"
                self.x[i] = msg
                if self.state['status'] == 'ACTIVE':
                    self.state['sigma'] = 0
                else:
                    self.state = {'status': 'ACTIVE', 'sigma': self.proc}

        self.y = self.x

        # print "STATUS : " , str(self.state['status'])
        # print "SIGMA : " , str(self.state['sigma'])

    def outputFnc(self):
        ''' DEVS output function.
        '''
        print "---- OUTPUT ----"
        n = len(self.y)
        print "N : " + str(n)

        '''INSERT strategy here [Change the state of the FMS (self.lump)]'''

        ''' End of strategy '''

        self.poke(self.OPorts[0], Message('''PUT_RETURN_VALUE_HERE !'''))
        print "---- END OUTPUT ----"

    def intTransition(self):
        ''' DEVS internal transition function.
        '''
        print "---- INTERNAL | Status " + str(self.state['status']) + " ----"
        if self.state['status'] == 'ACTIVE':
            self.state = {'status': 'IDLE', 'sigma': INFINITY}

    def timeAdvance(self):
        ''' DEVS Time Advance function.
        '''
        # print "---- TIME "+ str(self.state['sigma'])+" ----"
        return self.state['sigma']

    def finish(self, msg):
        ''' Additional function which is lunched just before the end of the simulation.
        '''
        print "---- FINISH ----"


# The Class Goes Here
class ClassName(object):
	pass
