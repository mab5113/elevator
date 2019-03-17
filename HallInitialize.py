#!/usr/bin/python3

from HallButtonInitialize import HallButtonInitialize
from HallLampInitialize import HallLampInitialize
from udpListener import myListener
from HallManager import HallManager

def HallInitialize(id):
	HallLampInitialize(id)
	HallButtonInitialize(id)
	myListener(id)
	HallManager(id)
