import datetime

# The first value in each tuple is for distances <= 50km
# The second value is for distances > 50km
MIN_CHARGE = (59.400, 89.000)
CHARGE_PER_SEC = (0.759, 1.761)
OFFPEAK_DISCOUNT = (0.4, 0.5)
SHARECALL_DISCOUNT = (0.0, 0.5)

NEAR, FAR = 0, 1

OFF_PEAK_START = datetime.time(19, 0, 0)
HOUR_BEFORE_OFF_PEAK_START = datetime.time(18, 0, 0)
OFF_PEAK_END = datetime.time(7, 0, 0)
HOUR_BEFORE_OFF_PEAK_END = datetime.time(6, 0, 0)

VAT_RATE = 0.14

def price_estimate(start_str, duration_str, destination_str, share_call_str):
    start = datetime.datetime.strptime(start_str, "%H:%M:%S").time()
    d_m, d_s = [int(p) for p in duration_str.split(":")]
    duration = datetime.timedelta(minutes=d_m, seconds=d_s).total_seconds()
    # We set the destination to an index value we can use with the tuple constants
    destination = FAR if destination_str.lower() == 'y' else NEAR
    share_call = True if share_call_str.lower() == 'y' else False

    peak_seconds = 0
    off_peak_seconds = 0

    if start >= OFF_PEAK_END and start <= HOUR_BEFORE_OFF_PEAK_START:
        # whole call fits in peak time
        peak_seconds = duration
    elif start >= OFF_PEAK_START or start <= HOUR_BEFORE_OFF_PEAK_END:
        # whole call fits in off-peak time
        off_peak_seconds = duration
    else:
        # call starts within hour of peak/off-peak boundary
        secs_left_in_hour = 3600 - start.minute * 60 + start.second

        if start < OFF_PEAK_END:
            # call starts in off-peak time
            if duration > secs_left_in_hour:
                peak_seconds = duration - secs_left_in_hour
            off_peak_seconds = duration - peak_seconds
        else:
            # call starts in peak time
            if duration > secs_left_in_hour:
                off_peak_seconds = duration - secs_left_in_hour
            peak_seconds = duration - off_peak_seconds

    basic = CHARGE_PER_SEC[destination] * duration
    offpeak_discount = OFFPEAK_DISCOUNT[destination] * CHARGE_PER_SEC[destination] * off_peak_seconds
    if share_call:
        share_call_discount =  SHARECALL_DISCOUNT[destination] * (basic - offpeak_discount)
    else:
        share_call_discount = 0
    net = basic - offpeak_discount - share_call_discount

    if net < MIN_CHARGE[destination]:
        net = MIN_CHARGE[destination]

    vat = VAT_RATE * net
    total = net + vat

    return basic, offpeak_discount, share_call_discount, net, vat, total

if __name__ == "__main__":
    start_str = input("Please enter the starting time of the call (HH:MM:SS): ")
    duration_str = input("Please enter the duration of the call (MM:SS): ")
    destination_str = input("Was the destination more than 50km away? (Y/N): ")
    share_call_str = input("Was the call a share-call? (Y/N): ")

    results = price_estimate(start_str, duration_str, destination_str, share_call_str)

    print("""Basic cost: %g
    Off-peak discount: %g
    Share-call discount: %g
    Net cost: %g
    VAT: %g
    Total cost: %g
    """ % results)
