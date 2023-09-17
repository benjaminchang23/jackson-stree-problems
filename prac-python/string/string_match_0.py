import re


def get_close_list(needle, stack_0, stack_1, stack_2, stack_3, stack_4):
    # for hay in stack_0:

    return match


pcds = []

pcds.append("some_base_name_1632233374.850.pcd")
pcds.append("some_base_name_1632233374.950.pcd")
pcds.append("some_base_name_1632233375.050.pcd")
pcds.append("some_base_name_1632233375.150.pcd")
pcds.append("some_base_name_1632233375.250.pcd")

cams_0 = []
cams_0.append("cam_left_1632233374.532.jpg")
cams_0.append("cam_left_1632233374.632.jpg")
cams_0.append("cam_left_1632233374.732.jpg")
cams_0.append("cam_left_1632233374.832.jpg")
cams_0.append("cam_left_1632233374.932.jpg")
cams_0.append("cam_left_1632233374.032.jpg")
cams_0.append("cam_left_1632233374.132.jpg")
cams_0.append("cam_left_1632233374.232.jpg")
cams_0.append("cam_left_1632233374.332.jpg")

cams_1 = []
cams_1.append("cam_front_1632233374.602.jpg")
cams_1.append("cam_front_1632233374.702.jpg")
cams_1.append("cam_front_1632233374.802.jpg")
cams_1.append("cam_front_1632233374.902.jpg")
cams_1.append("cam_front_1632233374.002.jpg")
cams_1.append("cam_front_1632233374.102.jpg")
cams_1.append("cam_front_1632233374.202.jpg")
cams_1.append("cam_front_1632233374.302.jpg")
cams_1.append("cam_front_1632233374.402.jpg")

cams_2 = []
cams_2.append("cam_right_1632233374.517.jpg")
cams_2.append("cam_right_1632233374.617.jpg")
cams_2.append("cam_right_1632233374.717.jpg")
cams_2.append("cam_right_1632233374.817.jpg")
cams_2.append("cam_right_1632233374.917.jpg")
cams_2.append("cam_right_1632233374.017.jpg")
cams_2.append("cam_right_1632233374.117.jpg")
cams_2.append("cam_right_1632233374.217.jpg")
cams_2.append("cam_right_1632233374.317.jpg")

cams_3 = []
cams_3.append("cam_back_1632233374.626.jpg")
cams_3.append("cam_back_1632233374.726.jpg")
cams_3.append("cam_back_1632233374.826.jpg")
cams_3.append("cam_back_1632233374.926.jpg")
cams_3.append("cam_back_1632233374.026.jpg")
cams_3.append("cam_back_1632233374.126.jpg")
cams_3.append("cam_back_1632233374.226.jpg")
cams_3.append("cam_back_1632233374.326.jpg")
cams_3.append("cam_back_1632233374.426.jpg")

cams_4 = []
cams_4.append("cam_top_1632233374.517.jpg")
cams_4.append("cam_top_1632233374.617.jpg")
cams_4.append("cam_top_1632233374.717.jpg")
cams_4.append("cam_top_1632233374.817.jpg")
cams_4.append("cam_top_1632233374.917.jpg")
cams_4.append("cam_top_1632233374.017.jpg")
cams_4.append("cam_top_1632233374.117.jpg")
cams_4.append("cam_top_1632233374.217.jpg")
cams_4.append("cam_top_1632233374.317.jpg")

combined = []
for pcd in pcds:
    ex = re.compile('[0-9]{10}\.[0-9]{3}')
    float(ex.findall("cam_top_1632233374.517.jpg")[0])
    match = get_close_list(pcd, cams_0, cams_1, cams_2, cams_3, cams_4)
    print(match)