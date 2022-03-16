import pyhop
from pycreate2 import Create2
import time


# -------------------------------- Operators --------------------------------
def drive_to_wall(state, a):
    if state.reached_wall[a] == False:
        state.reached_wall[a] = True
        return state
    else:
        return False


def rotate_from_wall(state, a):
    if state.reached_wall[a] == True:
        state.reached_wall[a] == False
        return state
    else:
        return False


pyhop.declare_operators(drive_to_wall, rotate_from_wall)
print('')
pyhop.print_operators()


# -------------------------------- Methods --------------------------------
def go_to_wall(state, a):
    if state.reached_wall[a] == False:
        return [('drive_to_wall', a), ('rotate_from_wall', a)]
    elif state.reached_wall[a] == True:
        return [('rotate_from_wall', a)]
    else:
        return False


pyhop.declare_methods('drive', go_to_wall)
print('')
pyhop.print_methods()


# -------------------------------- States --------------------------------
state1 = pyhop.State('state1')
state1.reached_wall = {'create2': True}

print('- If verbose=3, Pyhop also prints the intermediate states:')
pyhop.pyhop(state1, [('drive', 'create2')], verbose=1)


# -------------------------------- Functions --------------------------------
def get_state(state, bot):
    sensors = bot.get_sensors()
    light_bumpers = sensors.light_bumper

    # If front light sensors are True
    # set reached_wall state to True
    if light_bumpers.front_left or light_bumpers.front_right:
        state.reached_wall = True
    # Otherwise
    # set reached_wall state to False
    else:
        state.reached_wall = False
    return state


def drive_to_wall_FUNCTION(state, bot):
    # While the robot has not reached the wall
    while state.reached_wall == False:
        # drive straight
        bot.drive_direct(40, 40)
        # check the state again
        state = get_state(state, bot)
    # Stop driving straight once the robot ahs reached the wall
    bot.stop()
    return state


def rotate_from_wall_FUNCTION(state, bot):
    # While the robot still detects the wall
    while state.reached_wall == True:
        # rotate (right)
        bot.drive_direct(-40, 40)
        # check the state again
        state = get_state(state, bot)
    # Stop rotating once the robot no longer detects the wall
    bot.stop()
    return state


# -------------------------------- Main --------------------------------
if __name__ == "__main__":
    # Initialize robot
    port = "/dev/tty.usbserial-DN025ZAZ"
    bot = Create2(port)
    bot.start()
    bot.safe()

    # Read the state
    state = pyhop.state('state')

    # Create initial state
    reached_wall_state = get_state(state, bot)






