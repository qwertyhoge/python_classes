import datetime

dt = datetime.datetime.now()

with open('data/exec_times.txt', mode='a') as f:
    date_str = dt.strftime('%Y-%m-%d')
    f.write(date_str + '\n')
    print('wrote date: {}'.format(date_str))
    time_str = dt.strftime('%H:%M:%S')
    f.write(time_str + '\n')
    print('wrote time: {}'.format(time_str))

