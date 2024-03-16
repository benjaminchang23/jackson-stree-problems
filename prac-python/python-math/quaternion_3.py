import math
import numpy
import quaternion

def q_mult(q1, q2):
    x1, y1, z1, w1 = q1
    x2, y2, z2, w2 = q2
    x = w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2
    y = w1 * y2 + y1 * w2 + z1 * x2 - x1 * z2
    z = w1 * z2 + z1 * w2 + x1 * y2 - y1 * x2
    w = w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2

    return x, y, z, w

def q_conjugate(q):
    x, y, z, w = q
    return (-x, -y, -z, w)

def qv_mult(q1, v1):
    q2 = v1 + (0.0,)
    return q_mult(q_mult(q1, q2), q_conjugate(q1))[:-1]

def normalize(v, tolerance=0.00001):
    mag2 = sum(n * n for n in v)
    if abs(mag2 - 1.0) > tolerance:
        mag = math.sqrt(mag2)
        v = tuple(n / mag for n in v)
    return v

def axisangle_to_q(v, theta):
    v = normalize(v)
    x, y, z = v
    theta /= 2
    w = math.cos(theta)
    x = x * math.sin(theta)
    y = y * math.sin(theta)
    z = z * math.sin(theta)
    return x, y, z, w

def q_to_axisangle(q):
    v, w = q[:-1], q[3]
    theta = math.acos(w) * 2.0
    return normalize(v), theta

def simple_vec_add(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1], v1[2] + v2[2])

def print_point_pretty(p):
    x, y, z = p
    print(f"{x:.15f}, {y:.15f}, {z:.15f}")

# imagine a robot that starts from some known position and heading
# it does the following motions
# 1) drives forward 1 unit and up 1 unit (y, z)
# 2) turns 90 deg to the right
# 3) drives forward another 2 units (x)

# we get the position as
robot_position = (2, 1, 1)
print(f"robot_position: {robot_position}")

# we get the orientation as the quaternion x, y, z, w
z_axis_unit = (0, 0, 1)
robot_orientation = axisangle_to_q(z_axis_unit, -numpy.pi / 2)
print(f"robot_orientation: {robot_orientation}")
print(f"{axisangle_to_q(z_axis_unit, numpy.pi)}")
# if there are two lasers mounted 1 unit above the pose center
laser_mount_position = (0, 0, 1)
# with an orientation pointed left with the quaternion x, y, z, w
laser_orientation_0 = axisangle_to_q(z_axis_unit, numpy.pi / 2)
# laser_orientation_0 = (0, 0, 1, 1)
print(f"laser_orientation_0: {laser_orientation_0}")

# with an orientation pointed right with the quaternion x, y, z, w
laser_orientation_1 = axisangle_to_q(z_axis_unit, -numpy.pi / 2)
print(f"laser_orientation_1: {laser_orientation_1}")

# the points that the robot detects are in a 3x3 grid of points that form a square 1 unit apart
point_list = []
# first row
point_list.append((-1, 1, 1))
point_list.append((0, 1, 1))
point_list.append((1, 1, 1))
# second row
point_list.append((-1, 1, 0))
point_list.append((0, 1, 0))
point_list.append((1, 1, 0))
# third row
point_list.append((-1, 1, -1))
point_list.append((0, 1, -1))
point_list.append((1, 1, -1))

laser_position = simple_vec_add(robot_position, laser_mount_position)
print(f"laser_position: {laser_position}")

# translate the laser points to the local global pose by rotating the reverse of the orientations of the laser then robot
count = 0
for point in point_list:
    p_laser = simple_vec_add(qv_mult(laser_orientation_0, point), laser_mount_position)
    p_odom = simple_vec_add(qv_mult(robot_orientation, p_laser), robot_position)
    print_point_pretty(p_odom)
    count+=1
    if count % 3 == 0:
        print("------")

print("------------")

count = 0
for point in point_list:
    p_laser = simple_vec_add(qv_mult(laser_orientation_1, point), laser_mount_position)
    p_odom = simple_vec_add(qv_mult(robot_orientation, p_laser), robot_position)
    print_point_pretty(p_odom)
    count+=1
    if count % 3 == 0:
        print("------")
