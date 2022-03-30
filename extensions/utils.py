from . import jalali
from django.utils import timezone


jmonths = {
    '01' : 'فروردین',
    '02' : 'اردیبهشت',
    '03' : 'خرداد',
    '04' : 'تیر',
    '05' : 'مرداد',
    '06' : 'شهریور',
    '07' : 'مهر',
    '08' : 'آبان',
    '09' : 'آذر',
    '10' : 'دی',
    '11' : 'بهمن',
    '12' : 'اسفند',
}


def persian_numbers_converter(mystr):
    jnumbers = {
    '0' : '۰',
    '1' : '۱',
    '2' : '۲',
    '3' : '۳',
    '4' : '۴',
    '5' : '۵',
    '6' : '۶',
    '7' : '۷',
    '8' : '۸',
    '9' : '۹', }

    for e, p in jnumbers.items():
        mystr = mystr.replace(e, p)
    return mystr


def jalali_converter(time):
    time = timezone.localtime(time)
    time_to_str = "{},{},{}".format(time.year, time.month, time.day)
    time_to_tuple = jalali.Gregorian(time_to_str).persian_tuple()
    output = "{} {} {} , ساعت {}:{}".format(
        time_to_tuple[2], jmonths[str(time_to_tuple[1])], time_to_tuple[0], time.hour, time.minute
        )
    

    return persian_numbers_converter(output)

