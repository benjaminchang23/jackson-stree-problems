import operator

class widget(object):
    def __init__(self, path):
        self.path = path

widget_list = [
    widget("s3://one/two"),
    widget("s3://one"),
    widget("s3://one/two/three"),
]

widget_list.sort(key=operator.attrgetter("path"))

for m_widget in widget_list:
    print(m_widget.path)