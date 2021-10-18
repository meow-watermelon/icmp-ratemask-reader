# ICMP Rate Mask Reader

## Intro

ICMP Rate Mask Reader is a small utility to read ICMP ratemask string and covert it into ICMP code number(s) which are enabled for ICMP rate limiting.

## Python Module Dependencies

Following Python modules is needed to run this utility:

```
sys
```

## Usage

```
$ icmp-ratemask-reader.py [icmp_ratemask_string] [icmp_ratemask_string] ...
```

If no argument is supplied, the utility will return the current OS ICMP rate mask code(s). Otherwise, user can add multiple ICMP rate masks to get their results. If there's an error occurs during the coversion procedure, the offending entry will be skipped silently.

## Example

```
$ ./icmp-ratemask-reader.py 
6168:3 4 11 12

$ ./icmp-ratemask-reader.py 6000 5000
6000:3 5 6 7 9 10 11
5000:3 6 7 8 12
```
