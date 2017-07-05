from math import sin, cos
from copy import copy

def get(b_arr):
    ha_arr = [0x12340FFE, 0xA3B2EF56, 0xCD53CA23, 0xE57EB124]
    length = len(ha_arr)
    unit = 0xFFFFFFFF
    result_length = unit*length

    for byte in b_arr:
        curr_ind = byte % length
        #print 5 * byte + 2
        #print byte >> 1
        ha_arr[curr_ind] *= byte >> 1| int(85.0*sin((5*byte+2)/BYTE))
        #print ha_arr[curr_ind]
        #print 7*byte - 3
        #print ~byte >> 2
        ha_arr[curr_ind] += ~byte >> 2 ^ int(97.0*cos((7*byte-3)/BYTE))* unit / 2**8
        #print ha_arr[curr_ind]
        ha_arr[curr_ind] %= unit
        ha_arr[0], ha_arr[1], ha_arr[2], ha_arr[3] = ha_arr[2], ha_arr[3], ha_arr[0], ha_arr[1]
        #print ha_arr

    return reduce(lambda x, y: (x*x+y*y) % result_length, ha_arr)


BYTE = 0x100

def int_to_bytes(value):
    result = []
    value = copy(value)

    while value > 0:
        result.append(value % BYTE)
        value /= BYTE

    result.reverse()

    return result



def main():
    #print get(int_to_bytes(0x55))
    #print 'SHLOMO'
    #print get(int_to_bytes(0x59))
    #exit()
    achieved_hashes = {}

    n = 10000
    for i in xrange(n):
        hash_value = get(int_to_bytes(i))
        if hash_value not in achieved_hashes:
            achieved_hashes[hash_value] = i
        else:
            # print the first collusion:
            print '{0} : {1}, {2}'.format(hex(hash_value), hex(achieved_hashes[hash_value]), hex(i))
            break


if __name__ == '__main__':
    main()