# first version, no child nodes, only string names

class TransformNode:
    def __init__(self, frame_id, child_frame_id) -> None:
        self.frame_id = frame_id
        self.child_frame_id = child_frame_id
        self.translation = {}
        self.rotation = {}

    frame_id = ""
    child_frame_id = ""
    translation = {}
    rotation = {}

transform_0 = {"header": {"frame_id": "front_sensor"}, "child_frame_id": "front_lidar", "transform": {}}
transform_1 = {"header": {"frame_id": "imu_front"}, "child_frame_id": "front_sensor", "transform": {}}
transform_2 = {"header": {"frame_id": "vehicle_front"}, "child_frame_id": "imu_front", "transform": {}}
transform_3 = {"header": {"frame_id": "vehicle_front"}, "child_frame_id": "pose_ref", "transform": {}}
transform_4 = {"header": {"frame_id": "odom"}, "child_frame_id": "app_link", "transform": {}}

transform_5 = {"header": {"frame_id": "rear_sensor"}, "child_frame_id": "rear_lidar", "transform": {}}
transform_6 = {"header": {"frame_id": "imu_rear"}, "child_frame_id": "rear_sensor", "transform": {}}
transform_7 = {"header": {"frame_id": "vehicle_rear"}, "child_frame_id": "imu_rear", "transform": {}}
