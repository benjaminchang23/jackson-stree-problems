import datetime
import pytz

fmt = '%Y-%m-%d %H:%M:%S %Z%z'
utc_dt = datetime.datetime(2022, 2, 22, 5, 0, 0, tzinfo=pytz.utc)
eastern = pytz.timezone('US/Eastern')
local_dt = utc_dt.astimezone(eastern)

print(local_dt.strftime(fmt))
