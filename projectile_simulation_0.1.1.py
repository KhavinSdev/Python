import time
import numpy as np
import turtle


def projection_simulation(initial_velocity, angle, scale_factor, time_factor, acceleration_due_to_g):

    screen = turtle.Screen()
    screen.tracer(0)
    turtle1 = turtle.Turtle()
    turtle2 = turtle.Turtle()
    turtle3 = turtle.Turtle()
    turtle1.goto(0, 0)

    acceleration_g = acceleration_due_to_g
  

    velocity_initial_X = initial_velocity * np.cos(angle)
    velocity_initial_Y = initial_velocity * np.sin(angle)

    velocity_X = velocity_initial_X
    velocity_Y = velocity_initial_Y


    velocity_vector = [velocity_X, velocity_Y]
    position_vector = [0,0]

    time_spent = 0

    def time_of_flight(initial_velocity, angle, acceleration_g):
            return ((2 * initial_velocity * np.sin(angle))/acceleration_g)
    
    timeF = time_of_flight(initial_velocity, angle, acceleration_g)

    def max_height(initial_velocity, angle, acceleration_g):
        return ((initial_velocity ** 2) * np.sin(angle))/(2 * acceleration_g)

    def horizontal_range(initial_velocity, angle, acceleration_g):
        return (velocity_initial_X  * timeF)

    maxH = max_height(initial_velocity, angle, acceleration_g)
    horzR = horizontal_range(initial_velocity, angle, acceleration_g)
    

    print(timeF)
    print(horzR)
    
    
    while time_spent < timeF:
        velocity_vector[1] = velocity_vector[1] - ((acceleration_g) * time_factor)
        position_vector[1] = position_vector[1] + (velocity_vector[1] * time_factor) 
        position_vector[0] = position_vector[0] + (velocity_vector[0] * time_factor) 

        print(position_vector)

        turtle1.goto(position_vector[0] * scale_factor, position_vector[1] * scale_factor)
        turtle2.goto(position_vector[0] * scale_factor, 0)
        turtle3.goto(0, position_vector[1] * scale_factor)

        screen.update()
        time.sleep(1 * time_factor)
        time_spent = time_spent + (1 * time_factor)
        print(time_spent)

    print("reached the surface")





projection_simulation(50, np.pi/2, 0.5, 0.1, 2.2)
