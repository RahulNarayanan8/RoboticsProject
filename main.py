#Rahul Narayanan rn2374
#Kevin Glenn kg3165

import asyncio
import math
from viam.robot.client import RobotClient
from viam.rpc.dial import Credentials, DialOptions
from viam.components.base import Base
from viam.components.motor import Motor

import time
import numpy as np

height = 400
width = 300
velocity = 150
right = True
left = False

async def connect():
    creds = Credentials(
        type="robot-location-secret",
        payload='4rhyn1u0thr1tsmwej4suehfkf251gk4h055h5124qvav2hp')
    opts = RobotClient.Options(
        refresh_interval=0,
        dial_options=DialOptions(credentials=creds)
    )
    return await RobotClient.at_address('karthak2-main.pwhzcgtu9r.viam.cloud', opts)
async def rotate(clockwise, angle, motor):
    #angle in degrees
    value = 1
    if clockwise:
        value*=-1
    await motor.go_for(rpm = 60, revolutions = (((value*angle)/360)*7.12))
    await motor.reset_zero_position(offset=0.0)

async def write_a(motor, base):
    await base.move_straight(velocity = velocity, distance = height)
    await rotate(left, 90, motor)
    await base.move_straight(velocity = velocity, distance = width)
    await rotate(left, 90, motor)
    await base.move_straight(velocity = velocity, distance = height)
    await base.move_straight(velocity = -velocity, distance = math.floor((2/3)*height))
    await rotate(left, 90, motor)
    await base.move_straight(velocity = velocity, distance = width)
    await rotate(right, 90, motor)
    await base.move_straight(velocity = velocity, distance = math.floor((2/3)*height))

async def write_b(motor, base):
    await rotate(right, 90, motor)
    await base.move_straight(velocity = velocity, distance = width)
    await rotate(left, 90, motor)
    await base.move_straight(velocity = velocity, distance = height/2)
    await rotate(left, 90, motor)
    await base.move_straight(velocity = velocity, distance = width)
    await base.move_straight(velocity = -velocity, distance = math.floor(width*2/3))
    await rotate(right, 90, motor)
    await base.move_straight(velocity = velocity, distance = height/2)
    await rotate(left, 90, motor)
    await base.move_straight(velocity = velocity, distance = math.floor(width*2/3))
    await rotate(left, 90, motor)
    await base.move_straight(velocity = velocity, distance = height)

async def write_c(motor, base):
    await base.move_straight(velocity = velocity, distance = height)
    await rotate(left, 90, motor)
    await base.move_straight(velocity = velocity, distance = width)
    await base.move_straight(velocity = -velocity, distance = width)
    await rotate(left, 90, motor)
    await base.move_straight(velocity = velocity, distance = height)
    await rotate(right, 90, motor)
    await base.move_straight(velocity = velocity, distance = width)
    await base.move_straight(velocity = -velocity, distance = width)
    await rotate(left, 90, motor)

async def write_d(motor, base):
    await rotate(right, 90, motor)
    await base.move_straight(velocity = velocity, distance = math.floor(0.9*width))
    await rotate(left, 90, motor)
    await base.move_straight(velocity = velocity, distance = math.floor(0.075*height))
    await rotate(right, 90, motor)
    await base.move_straight(velocity = velocity, distance = math.floor(0.1*width))
    await rotate(left, 90, motor)
    await base.move_straight(velocity = velocity, distance = math.floor(0.85*height))
    await rotate(left, 90, motor)
    await base.move_straight(velocity = velocity, distance = math.floor(0.1*width))
    await rotate(right, 90, motor)
    await base.move_straight(velocity = velocity, distance = math.floor(0.075*height))
    await rotate(left, 90, motor)
    await base.move_straight(velocity = velocity, distance = math.floor(0.9*width))
    await rotate(left, 90, motor)
    await base.move_straight(velocity = velocity, distance = height)

async def write_e(motor, base):
    await base.move_straight(velocity = velocity, distance = height)
    await rotate(right, 90, motor)
    await base.move_straight(velocity = velocity, distance = width)
    await base.move_straight(velocity = -velocity, distance = width)
    await rotate(right, 90, motor)
    await base.move_straight(velocity = velocity, distance = height/2)
    await rotate(left, 90, motor)
    await base.move_straight(velocity = velocity, distance = width)
    await base.move_straight(velocity = -velocity, distance = width)
    await rotate(right, 90, motor)
    await base.move_straight(velocity = velocity, distance = height/2)
    await rotate(left, 90, motor)
    await base.move_straight(velocity = velocity, distance = width)
    await base.move_straight(velocity = -velocity, distance = width)
    await rotate(right, 90, motor)


async def write_f(motor, base):
    await base.move_straight(velocity = velocity, distance = height)
    await rotate(right, 90, motor)
    await base.move_straight(velocity = velocity, distance = width)
    await base.move_straight(velocity = -velocity, distance = width)
    await rotate(right, 90, motor)
    await base.move_straight(velocity = velocity, distance = height/2)
    await rotate(left, 90, motor)
    await base.move_straight(velocity = velocity, distance = width)
    await base.move_straight(velocity = -velocity, distance = width)
    await rotate(right, 90, motor)
    await base.move_straight(velocity = velocity, distance = height/2)

async def write_g(motor, base):
    await base.move_straight(velocity = velocity, distance = height)
    await rotate(right, 90, motor)
    await base.move_straight(velocity = velocity, distance = width)
    await base.move_straight(velocity = -velocity, distance = width)
    await rotate(right, 90, motor)
    await base.move_straight(velocity = velocity, distance = height)
    await rotate(left, 90, motor)
    await base.move_straight(velocity = velocity, distance = width)
    await rotate(left, 90, motor)
    await base.move_straight(velocity = velocity, distance = height/2)
    await rotate(left, 90, motor)
    await base.move_straight(velocity = velocity, distance = width)
    await base.move_straight(velocity = -velocity, distance = width)
    await rotate(left, 90, motor)
    await base.move_straight(velocity = velocity, distance = height/2)
    await rotate(right, 90, motor)
    await base.move_straight(velocity = velocity, distance = width)
    await rotate(left, 90, motor)

async def write_h(motor, base):
    await base.move_straight(velocity = velocity, distance = height)
    await base.move_straight(velocity = -velocity, distance = math.floor(height/2))
    await rotate(right, 90, motor)
    await base.move_straight(velocity = velocity, distance = width)
    await rotate(right, 90, motor)
    await base.move_straight(velocity = velocity, distance = math.floor(height/2))
    await base.move_straight(velocity = -velocity, distance = height)
    await base.move_straight(velocity = velocity, distance = math.floor(height/2))
    await rotate(right, 90, motor)
    await base.move_straight(velocity = velocity, distance = width)
    await rotate(left, 90, motor)
    await base.move_straight(velocity = velocity, distance = math.floor(height/2))

async def write_i(motor, base):
    await base.move_straight(velocity = velocity, distance = height)
    await base.move_straight(velocity = -velocity, distance = height)
    await rotate(left, 180, motor)

async def write_j(motor, base):
    await rotate(right, 90, motor)
    await base.move_straight(velocity = velocity, distance = width/2)
    await rotate(left, 90, motor)
    await base.move_straight(velocity = velocity, distance = height)
    await rotate(left, 90, motor)
    await base.move_straight(velocity = velocity, distance = width/2)
    await base.move_straight(velocity = -velocity, distance = width)
    await base.move_straight(velocity = velocity, distance = width/2)
    await rotate(left, 90, motor)
    await base.move_straight(velocity = velocity, distance = height)
    await rotate(right, 90, motor)
    await base.move_straight(velocity = velocity, distance = width/2)
    await rotate(left, 90, motor)

async def write_k(motor, base):
    await base.move_straight(velocity = velocity, distance = height)
    await base.move_straight(velocity = -velocity, distance = height/2)
    await rotate(right, 45, motor)
    await base.move_straight(velocity = velocity, distance = 360)
    await base.move_straight(velocity = -velocity, distance = 360)
    await rotate(right, 90, motor)
    await base.move_straight(velocity = velocity, distance = 360)
    await base.move_straight(velocity = -velocity, distance = 360)
    await rotate(right, 45, motor)
    await base.move_straight(velocity = velocity, distance = height/2)

async def write_l(motor, base):
    await base.move_straight(velocity = velocity, distance = height)
    await base.move_straight(velocity = -velocity, distance = height)
    await rotate(right, 90, motor)
    await base.move_straight(velocity = velocity, distance = width)
    await base.move_straight(velocity = -velocity, distance = width)
    await rotate(right, 90, motor)


async def write_m(motor, base):
    await base.move_straight(velocity = velocity, distance = height)
    await rotate(right, 90, motor)
    await base.move_straight(velocity = velocity, distance = width/2)
    await rotate(right, 90, motor)
    await base.move_straight(velocity = velocity, distance = height*0.75)
    await base.move_straight(velocity = velocity, distance = height*0.75)
    await rotate(left, 90, motor)
    await base.move_straight(velocity = velocity, distance = width/2)
    await rotate(right, 90, motor)
    await base.move_straight(velocity = velocity, distance = height)
    await base.move_straight(velocity = -velocity, distance = height)
    await rotate(right, 90, motor)
    await base.move_straight(velocity = velocity, distance = width)
    await rotate(left, 90, motor)
    await base.move_straight(velocity = velocity, distance = height)

async def write_n(motor, base):
    await base.move_straight(velocity = velocity, distance = height)
    await rotate(right, (90-48)+90, motor)
    await base.move_straight(velocity = velocity, distance = 500)
    await rotate(left, 90-48+90, motor)
    await base.move_straight(velocity = velocity, distance = height)
    await base.move_straight(velocity = -velocity, distance = height)
    await rotate(left, 42, motor)
    await base.move_straight(velocity = velocity, distance = 500)
    await rotate(right, 42, motor)
    await base.move_straight(velocity = -velocity, distance = height)
    await rotate(right, 180, motor)

async def write_o(motor, base):
    await base.move_straight(velocity = velocity, distance = height)
    await rotate(right, 90, motor)
    await base.move_straight(velocity = velocity, distance = width)
    await rotate(right, 90, motor)
    await base.move_straight(velocity = velocity, distance = height)
    await rotate(right, 90, motor)
    await base.move_straight(velocity = velocity, distance = width)
    await rotate(left, 90, motor)

async def write_p(motor, base):
    await base.move_straight(velocity = velocity, distance = height)
    await rotate(right, 90, motor)
    await base.move_straight(velocity = velocity, distance = width)
    await rotate(right, 90, motor)
    await base.move_straight(velocity = velocity, distance = math.floor(height/2))
    await rotate(right, 90, motor)
    await base.move_straight(velocity = velocity, distance = width)
    await rotate(left, 90, motor)
    await base.move_straight(velocity = velocity, distance = math.floor(height/2))

async def write_q(motor, base):
    await base.move_straight(velocity = velocity, distance = height)
    await rotate(right, 90, motor)
    await base.move_straight(velocity = velocity, distance = width)
    await rotate(right, 90, motor)
    await base.move_straight(velocity = velocity, distance = height)
    await rotate(right, 90, motor)
    await rotate(right, 45, motor)
    await base.move_straight(velocity = velocity, distance = 75)
    await base.move_straight(velocity = -velocity, distance = 150)
    await base.move_straight(velocity = velocity, distance = 75)
    await rotate(left, 45, motor)
    await base.move_straight(velocity = velocity, distance = width)
    await rotate(left, 90, motor)

async def write_r(motor, base):
    await base.move_straight(velocity = velocity, distance = height)
    await rotate(right, 90, motor)
    await base.move_straight(velocity = velocity, distance = width)
    await rotate(right, 90, motor)
    await base.move_straight(velocity = velocity, distance = height/2)
    await rotate(right, 90, motor)
    await base.move_straight(velocity = velocity, distance = width)
    await rotate(left, 135, motor)
    await base.move_straight(velocity = velocity, distance = 150)
    await base.move_straight(velocity = -velocity, distance = 150)
    await rotate(right, 45, motor)
    await ase.move_straight(velocity = velocity, distance = height/2)

async def write_s(motor, base):
    await rotate(right, 90, motor)
    await base.move_straight(velocity = velocity, distance = width)
    await rotate(left, 90, motor)
    await base.move_straight(velocity = velocity, distance = height/2)
    await rotate(left, 90, motor)
    await base.move_straight(velocity = velocity, distance = width)
    await rotate(right, 90, motor)
    await base.move_straight(velocity = velocity, distance = height/2)
    await rotate(right, 90, motor)
    await base.move_straight(velocity = velocity, distance = width)
    await base.move_straight(velocity = -velocity, distance = width)
    await rotate(left, 90, motor)
    await base.move_straight(velocity = -velocity, distance = height/2)
    await rotate(left, 90, motor)
    await base.move_straight(velocity = velocity, distance = width)
    await rotate(right, 90, motor)
    await base.move_straight(velocity = velocity, distance = height/2)
    await rotate(left, 90, motor)
    await base.move_straight(velocity = velocity, distance = width)
    await rotate(left, 90, motor)

async def write_t(motor, base):
    #go backwards x distance
    await base.move_straight(velocity = -velocity, distance = 100)
    
    await rotate(right, 90, motor)
    await base.move_straight(velocity = velocity, distance = math.floor(width/2))
    await rotate(left, 90, motor)
    await base.move_straight(velocity = velocity, distance = 100+height)
    await rotate(left, 90, motor)
    await base.move_straight(velocity = velocity, distance = math.floor(width/2))
    await base.move_straight(velocity = -velocity, distance = width)
    await base.move_straight(velocity = velocity, distance = math.floor(width/2))
    await rotate(left, 90, motor)
    await base.move_straight(velocity = velocity, distance = 100+height)
    await rotate(right, 90, motor)
    await base.move_straight(velocity = velocity, distance = math.floor(width/2))
    await rotate(left, 90, motor)
    await base.move_straight(velocity = -velocity, distance = 100)

async def write_u(motor, base):
    await base.move_straight(velocity = velocity, distance = height)
    await base.move_straight(velocity = -velocity, distance = height)
    await rotate(right, 90, motor)
    await base.move_straight(velocity = velocity, distance = width)
    await rotate(left, 90, motor)
    await base.move_straight(velocity = velocity, distance = height)
    await base.move_straight(velocity = -velocity, distance = height)
    await rotate(left, 90, motor)
    await base.move_straight(velocity = velocity, distance = width)
    await rotate(left, 90, motor)
    

async def write_v(motor, base):
    #go backwards x distance
    await base.move_straight(velocity = -velocity, distance = 100)

    await rotate(right, 90, motor)
    await base.move_straight(velocity = velocity, distance = width/2)
    await rotate(left, 90, motor)
    await base.move_straight(velocity = -velocity, distance = 100+height)
    await rotate(left, 20.5, motor)
    await base.move_straight(velocity = velocity, distance = 427)
    await base.move_straight(velocity = -velocity, distance = 427)
    await rotate(right, (180-(2*20.5)), motor)
    await base.move_straight(velocity = velocity, distance = 427)
    await base.move_straight(velocity = -velocity, distance = 427)
    await rotate(left, 20.5, motor)
    await base.move_straight(velocity = -velocity, distance = 100)
    await rotate(left, 90, motor)
    await base.move_straight(velocity = velocity, distance = width/2)
    await rotate(left, 90, motor)
    await base.move_straight(velocity = -velocity, distance = 100)

async def write_w(motor, base):
    await base.move_straight(velocity = velocity, distance = height)
    await base.move_straight(velocity = -velocity, distance = height)
    await rotate(right, 90, motor)
    await base.move_straight(velocity = velocity, distance = width/2)
    await rotate(left, 90, motor)
    await base.move_straight(velocity = velocity, distance = height/2)
    await base.move_straight(velocity = -velocity, distance = height/2)
    await rotate(right, 90, motor)
    await base.move_straight(velocity = velocity, distance = width/2)
    await rotate(left, 90, motor)
    await base.move_straight(velocity = velocity, distance = height)
    await base.move_straight(velocity = -velocity, distance = height)
    await rotate(left, 90, motor)
    await base.move_straight(velocity = velocity, distance = width)
    await rotate(left, 90, motor)




async def write_x(motor, base):
    await rotate(right, 53, motor)
    await base.move_straight(velocity = velocity, distance = 500)
    await base.move_straight(velocity = -velocity, distance = 250)
    await rotate(right, 104, motor)
    await base.move_straight(velocity = velocity, distance = 250)
    await base.move_straight(velocity = -velocity, distance = 500)
    await base.move_straight(velocity = velocity, distance = 250)

    await rotate(right, 76, motor)
    await base.move_straight(velocity = velocity, distance = 250)
    await rotate(left, 37, motor)

async def write_y(motor, base):
    await rotate(right, 90, motor)
    await base.move_straight(velocity = velocity, distance = width)
    await rotate(left, 90, motor)
    await base.move_straight(velocity = velocity, distance = height)
    await base.move_straight(velocity = -velocity, distance = math.floor(height/3))
    await rotate(left, 90, motor)
    await base.move_straight(velocity = velocity, distance = width)
    await rotate(right, 90, motor)
    await base.move_straight(velocity = velocity, distance = math.floor(height/3))
    await base.move_straight(velocity = -velocity, distance = math.floor(height/3))
    await rotate(right, 90, motor)
    await base.move_straight(velocity = velocity, distance = width)
    await rotate(right, 90, motor)
    await base.move_straight(velocity = velocity, distance = math.floor(height/3*2))
    await rotate(right, 90, motor)
    await base.move_straight(velocity = velocity, distance = width)
    await rotate(left, 90, motor)

async def write_z(motor, base):
    await rotate(right, 90, motor)
    await base.move_straight(velocity = velocity, distance = width)
    await base.move_straight(velocity = -velocity, distance = width)
    await rotate(left, 53, motor)
    await base.move_straight(velocity = velocity, distance = 500)
    await rotate(left, 127, motor)
    await base.move_straight(velocity = velocity, distance = width)
    await base.move_straight(velocity = -velocity, distance = width)
    await rotate(left, 53, motor)
    await base.move_straight(velocity = velocity, distance = 500)
    await rotate(left, 37, motor)






async def move_to_next(motor, base):
    #pointing down at the start of this
    await base.move_straight(velocity = velocity, distance = 100)
    await rotate(False, 96, motor)
    await base.move_straight(velocity = velocity, distance = math.floor(width * 1.5))
    await rotate(False, 96, motor)
    await base.move_straight(velocity = velocity, distance = 100)
    
def handwriting_recognition(image_path):
    import easyocr
    reader = easyocr.Reader(['en'])
    result = reader.recognize(image_path)
    return ((result[0][-2]).strip())

async def main():

    #starting direction is up for all letters

    robot = await connect()

    roverBase = Base.from_robot(robot, 'viam_base')
    right = Motor.from_robot(robot, "right")
    
    #Writing PINTO
    letter_dict = {"a": write_a, "b": write_b, "c": write_c, "d": write_d, "e": write_e, "f": write_f, "g": write_g, "h": write_h, "i": write_i, "j": write_j, "k": write_k, "l": write_l,
    "m": write_m, "n": write_n, "o": write_o, "p": write_p, "q": write_q, "r": write_r, "s": write_s, "t": write_t, "u": write_u, "v": write_v, "w": write_w, "x": write_x,"y": write_y, "z": write_z}



    string_to_write = handwriting_recognition("final_img.jpg")
    string_to_write = string_to_write.lower()

    for char in string_to_write:
        await letter_dict[char].__call__(right, roverBase)
        await move_to_next(right, roverBase)

    await robot.close()


if __name__ == '__main__':
    asyncio.run(main())
