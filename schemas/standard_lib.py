from typing import Tuple
import inspect
import pdb
class TagSet(object):
    pass

class Zone_Temperature_Sensor():
    pass
class Zone_Temperature_Setpoint():
    pass
class Occupancy_Command():
    pass
class Supply_Air_Flow_Setpoint():
    pass


def vav(znt_input: Zone_Temperature_Setpoint,
        occ_input: Occupancy_Command,
        ) -> Tuple[
            Supply_Air_Flow_Setpoint,
            Zone_Temperature_Sensor,
        ]:
    frame = inspect.currentframe()
    args, _, _, values = inspect.getargvalues(frame)
    print('function name "%s"' % inspect.getframeinfo(frame)[2])
    for i in args:
        print("    %s = %s" % (i, values[i]))

vav(Zone_Temperature_Setpoint(), Occupancy_Command())
#vav(Zone_Temperature_Setpoint(), Zone_Temperature_Sensor())
