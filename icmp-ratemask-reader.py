#!/usr/bin/env python3

import sys

def get_icmp_rate_bits(string):
    icmp_rate_bits_code = []
    icmp_rate_bin = bin(int(string))[2:].zfill(16)

    for i in range(len(icmp_rate_bin)):
        if icmp_rate_bin[i] == '1':
            icmp_rate_bits_code.append(str(i))

    return ' '.join(icmp_rate_bits_code)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        # return current OS ICMP rate mask if no argument
        try:
            with open('/proc/sys/net/ipv4/icmp_ratemask', 'r') as f:
                output = f.readlines()
        except Exception as e:
            print('Failed to read /proc/sys/net/ipv4/icmp_ratemask: %s' %(e))
        else:
            icmp_rate_mask_string = output[0].strip()
            print(icmp_rate_mask_string+':'+get_icmp_rate_bits(icmp_rate_mask_string))
    else:
        # return input rate mask
        args = sys.argv[1:]

        for m in args:
            try:
                icmp_rate_mask_string = get_icmp_rate_bits(m)
            except:
                pass
            else:
                print(m+':'+icmp_rate_mask_string)
