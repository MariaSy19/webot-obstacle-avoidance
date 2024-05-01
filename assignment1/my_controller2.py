from controller import Robot, DistanceSensor, Motor

# time in [ms] of a simulation step
TIME_STEP = 64

MAX_SPEED = 6.28

# create the Robot instance.
robot = Robot()
ps = []
psNames = ['Rsensor','Lsensor']
for i in range(2):
   ps.append(robot.getDevice(psNames[i]))
   # sensor activation
   ps[i].enable(TIME_STEP)

# initialize devices
#left motor wheels
leftMotor = robot.getDevice('Lmotor1')
leftMotor2 = robot.getDevice('Lmotor2')

leftMotor.setPosition(float('inf'))
leftMotor.setVelocity(0.0)

leftMotor2.setPosition(float('inf'))
leftMotor2.setVelocity(0.0)

#right motor wheels
rightMotor = robot.getDevice('Rmotor1')
rightMotor2 = robot.getDevice('Rmotor2')

rightMotor.setPosition(float('inf'))
rightMotor.setVelocity(0.0)

rightMotor2.setPosition(float('inf'))
rightMotor2.setVelocity(0.0)

# feedback loop: step simulation until receiving an exit event
while robot.step(TIME_STEP) != -1:
    psValues = []
    for i in range(2):
       psValues.append(ps[i].getValue())
       
    # detect obstacles
    R_obstacles = psValues[0] < 1000.0
    L_obstacles = psValues[1] < 1000.0
     # initialize motor speeds at 70% of MAX_SPEED.
    leftSpeed = 0.7 * MAX_SPEED
    leftSpeed2 = 0.7 * MAX_SPEED
    rightSpeed = 0.7 * MAX_SPEED
    rightSpeed2 = 0.7 * MAX_SPEED
    
    # Modify speeds according to obstacles
    if L_obstacles:
         # Turn right
        leftSpeed = -0.7 * MAX_SPEED
        leftSpeed2 = -0.7 * MAX_SPEED
        rightSpeed = 0.7 * MAX_SPEED
        rightSpeed2 = 0.7 * MAX_SPEED
    elif R_obstacles:
         # Turn left
        leftSpeed = 0.7 * MAX_SPEED
        leftSpeed2 = 0.7 * MAX_SPEED
        rightSpeed = -0.7 * MAX_SPEED
        rightSpeed2 = -0.7 * MAX_SPEED
   
   
    # write actuators inputs
    leftMotor.setVelocity(leftSpeed)
    leftMotor2.setVelocity(leftSpeed2)
    rightMotor.setVelocity(rightSpeed)
    rightMotor2.setVelocity(rightSpeed2)
