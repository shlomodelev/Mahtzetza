from math import sin


def get(b_arr):
    ha_arr = [0x12340FFE, 0xA3B2EF56, 0xCD53CA23, 0xE57EB124]
    length = len(ha_arr)
    unit = 0xFFFFFFFF
    result_length = unit*length

    for i, byte in enumerate(b_arr):
        curr_ind = (length - i) % length
        ha_arr[curr_ind] *= (byte | int(100.0*sin(i)))
        ha_arr[curr_ind] %= unit
        ha_arr[0], ha_arr[1], ha_arr[2], ha_arr[3] = ha_arr[2], ha_arr[3], ha_arr[0], ha_arr[1]

    return reduce(lambda x, y: (x*x+y*y) % result_length, ha_arr)


def main():
    s_list = ['Shlomo Modelevsky', 'Rhlomo Modelevsky', 'Rhlomo modelevskz', 'Rglomo modelevskz',
			  'Rglomo modelevslz', 'Rgkomo modelevslz']
    for s in s_list:
		print '{0} : {1}'.format(s, format(get(bytearray(s, 'utf-8')), '02x'))
		print [x for x in bytearray(s, 'utf-8')]


if __name__ == '__main__':
    main()