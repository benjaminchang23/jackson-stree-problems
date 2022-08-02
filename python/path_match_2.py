from sys import maxsize
from sysconfig import get_path

def get_cam_topic(path: str):
    rfind_slash_res_0 = path.rfind("/")
    rfind_slash_res_1 = path[:rfind_slash_res_0].rfind("/")
    return path[rfind_slash_res_1 + 1: rfind_slash_res_0]

def get_path_timestamp(path: str):
    rfind_peroid_res = path.rfind(".")
    rfind_slash_res = path.rfind("/")
    return float(path[rfind_slash_res + 1 : rfind_peroid_res])

cam_list = []

cam_list.append("s3://bucket/some/s3/path/cam1/1624053543.973300076.jpg")
cam_list.append("s3://bucket/some/s3/path/cam1/1624053544.073143005.jpg")
cam_list.append("s3://bucket/some/s3/path/cam1/1624053544.106466055.jpg")
cam_list.append("s3://bucket/some/s3/path/cam1/1624053544.139755964.jpg")
cam_list.append("s3://bucket/some/s3/path/cam1/1624053544.239768028.jpg")
cam_list.append("s3://bucket/some/s3/path/cam1/1624053544.273108959.jpg")
cam_list.append("s3://bucket/some/s3/path/cam1/1624053544.306571007.jpg")
cam_list.append("s3://bucket/some/s3/path/cam1/1624053544.339740992.jpg")
cam_list.append("s3://bucket/some/s3/path/cam1/1624053544.373106003.jpg")
cam_list.append("s3://bucket/some/s3/path/cam1/1624053544.639657974.jpg")
cam_list.append("s3://bucket/some/s3/path/cam1/1624053544.673021078.jpg")
cam_list.append("s3://bucket/some/s3/path/cam1/1624053544.706377983.jpg")
cam_list.append("s3://bucket/some/s3/path/cam1/1624053544.739775896.jpg")
cam_list.append("s3://bucket/some/s3/path/cam1/1624053544.773024082.jpg")
cam_list.append("s3://bucket/some/s3/path/cam1/1624053544.806375027.jpg")
cam_list.append("s3://bucket/some/s3/path/cam1/1624053544.906409025.jpg")
cam_list.append("s3://bucket/some/s3/path/cam1/1624053544.939626932.jpg")
cam_list.append("s3://bucket/some/s3/path/cam1/1624053544.973072052.jpg")
cam_list.append("s3://bucket/some/s3/path/cam1/1624053545.006361961.jpg")
cam_list.append("s3://bucket/some/s3/path/cam2/1624053543.876003027.jpg")
cam_list.append("s3://bucket/some/s3/path/cam2/1624053544.075928926.jpg")
cam_list.append("s3://bucket/some/s3/path/cam2/1624053544.109287977.jpg")
cam_list.append("s3://bucket/some/s3/path/cam2/1624053544.142564058.jpg")
cam_list.append("s3://bucket/some/s3/path/cam2/1624053544.242569923.jpg")
cam_list.append("s3://bucket/some/s3/path/cam2/1624053544.275943041.jpg")
cam_list.append("s3://bucket/some/s3/path/cam2/1624053544.309273958.jpg")
cam_list.append("s3://bucket/some/s3/path/cam2/1624053544.342508078.jpg")
cam_list.append("s3://bucket/some/s3/path/cam2/1624053544.375942945.jpg")
cam_list.append("s3://bucket/some/s3/path/cam2/1624053544.642474890.jpg")
cam_list.append("s3://bucket/some/s3/path/cam2/1624053544.675848007.jpg")
cam_list.append("s3://bucket/some/s3/path/cam2/1624053544.709172964.jpg")
cam_list.append("s3://bucket/some/s3/path/cam2/1624053544.742455959.jpg")
cam_list.append("s3://bucket/some/s3/path/cam2/1624053544.775701046.jpg")
cam_list.append("s3://bucket/some/s3/path/cam2/1624053544.809158087.jpg")
cam_list.append("s3://bucket/some/s3/path/cam2/1624053544.909204006.jpg")
cam_list.append("s3://bucket/some/s3/path/cam2/1624053544.942493916.jpg")
cam_list.append("s3://bucket/some/s3/path/cam2/1624053544.975824118.jpg")
cam_list.append("s3://bucket/some/s3/path/cam2/1624053545.009516954.jpg")
cam_list.append("s3://bucket/some/s3/path/cam3/1624053543.875010967.jpg")
cam_list.append("s3://bucket/some/s3/path/cam3/1624053544.074892998.jpg")
cam_list.append("s3://bucket/some/s3/path/cam3/1624053544.108381987.jpg")
cam_list.append("s3://bucket/some/s3/path/cam3/1624053544.141648054.jpg")
cam_list.append("s3://bucket/some/s3/path/cam3/1624053544.241525888.jpg")
cam_list.append("s3://bucket/some/s3/path/cam3/1624053544.274868011.jpg")
cam_list.append("s3://bucket/some/s3/path/cam3/1624053544.308345079.jpg")
cam_list.append("s3://bucket/some/s3/path/cam3/1624053544.341608047.jpg")
cam_list.append("s3://bucket/some/s3/path/cam3/1624053544.374803066.jpg")
cam_list.append("s3://bucket/some/s3/path/cam3/1624053544.641565084.jpg")
cam_list.append("s3://bucket/some/s3/path/cam3/1624053544.674841881.jpg")
cam_list.append("s3://bucket/some/s3/path/cam3/1624053544.708074093.jpg")
cam_list.append("s3://bucket/some/s3/path/cam3/1624053544.741399050.jpg")
cam_list.append("s3://bucket/some/s3/path/cam3/1624053544.774694920.jpg")
cam_list.append("s3://bucket/some/s3/path/cam3/1624053544.808099985.jpg")
cam_list.append("s3://bucket/some/s3/path/cam3/1624053544.908274889.jpg")
cam_list.append("s3://bucket/some/s3/path/cam3/1624053544.941382885.jpg")
cam_list.append("s3://bucket/some/s3/path/cam3/1624053544.974781990.jpg")
cam_list.append("s3://bucket/some/s3/path/cam3/1624053545.008025885.jpg")

# get all topics
topic_list = []
for path in cam_list:
    topic = get_cam_topic(path)
    if topic not in topic_list:
        topic_list.append(topic)

print("topic list: {}".format(topic_list))

cam_dict = {}

for topic in topic_list:
    cam_dict[topic] = {}

for path in cam_list:
    cam_topic = get_cam_topic(path)
    if cam_topic in topic_list:
        cam_timestamp = get_path_timestamp(path)
        cam_dict[cam_topic][path] = cam_timestamp

# print(cam_dict)

point_list = []

point_list.append("s3://bucket/some/s3/path/points1/1624053544.000020504.pcd")
point_list.append("s3://bucket/some/s3/path/points1/1624053544.100117207.pcd")
point_list.append("s3://bucket/some/s3/path/points1/1624053544.200195789.pcd")
point_list.append("s3://bucket/some/s3/path/points1/1624053544.299964905.pcd")
point_list.append("s3://bucket/some/s3/path/points1/1624053544.499864101.pcd")
point_list.append("s3://bucket/some/s3/path/points1/1624053544.599949121.pcd")
point_list.append("s3://bucket/some/s3/path/points1/1624053544.700036526.pcd")
point_list.append("s3://bucket/some/s3/path/points1/1624053545.100095749.pcd")
point_list.append("s3://bucket/some/s3/path/points2/1624053543.999921322.pcd")
point_list.append("s3://bucket/some/s3/path/points2/1624053544.100004435.pcd")
point_list.append("s3://bucket/some/s3/path/points2/1624053544.200102806.pcd")
point_list.append("s3://bucket/some/s3/path/points2/1624053544.299882412.pcd")
point_list.append("s3://bucket/some/s3/path/points2/1624053544.599810600.pcd")
point_list.append("s3://bucket/some/s3/path/points2/1624053544.699927807.pcd")
point_list.append("s3://bucket/some/s3/path/points2/1624053544.999863625.pcd")
point_list.append("s3://bucket/some/s3/path/points2/1624053545.099984646.pcd")

print("cam_dict: {}".format(cam_dict))

print("cam_list has {} elements".format(len(cam_list)))
print("cam_dict has {} elements".format(len(cam_dict)))
print("point_list has {} elements".format(len(point_list)))

point_combos = {}

for point in point_list:
    point_timestamp = get_path_timestamp(point)
    # print("point_timestamp: {}".format(point_timestamp))

    combined_image_list = []
    for topic_key in cam_dict:
        # print("checking topic: {}".format(topic_key))
        recent_minimum = maxsize
        recent_minimum_key = None
        for image_key in cam_dict[topic_key]:
            # print("checking dict: {} with value: {}".format(image_key, cam_dict[topic_key][image_key]))
            difference = abs(cam_dict[topic_key][image_key] - point_timestamp)
            if difference < recent_minimum:
                # print("found new: {} - {}".format(cam_dict[topic_key][image_key], image_key))
                recent_minimum = difference
                recent_minimum_key = image_key
        if recent_minimum_key is not None:
            combined_image_list.append(recent_minimum_key)
        # print("point: {} is closest to: {}".format(point, recent_minimum_key))
    point_combos[point] = combined_image_list

print(point_combos)