# You work for a travel agent.
# They want you to write a function that takes two times as strings, and adds them together. For example:
# "10:15:00" + "04:20:25" = "14:35:25"
from datetime import datetime, timedelta


def add_timestring(time1, time2):
    # convert string 1 to time
    try:
        converted_time1 = datetime.strptime(time1, "%H:%M:%S")
    except ValueError:
        raise Exception(f"time1 argument incorrectly formatted: {time1=}")

    # convert string 2 to time
    try:
        converted_time2 = datetime.strptime(time2, "%H:%M:%S")
    except ValueError:
        raise Exception(f"time1 argument incorrectly formatted: {time2=}")

    # add the two times
    return (
        converted_time1
        + timedelta(
            hours=converted_time2.hour,
            minutes=converted_time2.minute,
            seconds=converted_time2.second,
        )
    ).strftime("%H:%M:%S")


if __name__ == "__main__":
    result = add_timestring("10:15:00", "04:20:25")
    print(result)
