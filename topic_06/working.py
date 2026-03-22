def enumerate_ips(start_ip, n):
    '''
    Return a list containing the next `n` IPs beginning with `start_ip`.

    >>> list(enumerate_ips('192.168.1.0', 2))
    ['192.168.1.0', '192.168.1.1']

    >>> list(enumerate_ips('8.8.8.8', 10))
    ['8.8.8.8', '8.8.8.9', '8.8.8.10', '8.8.8.11', '8.8.8.12', '8.8.8.13', '8.8.8.14', '8.8.8.15', '8.8.8.16', '8.8.8.17']

    # This test ensures that you are properly handling "wrap around"
    #
    >>> list(enumerate_ips('192.168.0.255', 2))
    ['192.168.0.255', '192.168.1.0']

    The following tests ensure that the correct number of ips get returned.

    >>> len(list(enumerate_ips('8.8.8.8', 10)))
    10
    >>> len(list(enumerate_ips('8.8.8.8', 1000)))
    1000
    >>> len(list(enumerate_ips('8.8.8.8', 100000)))
    100000
    '''
    parts = [int(p) for p in start_ip.split('.')]
    result = []
    for _ in range(n):
        result.append('.'.join(str(p) for p in parts))
        for i in range(3, -1, -1):
            if parts[i] < 255:
                parts[i] += 1
                break
            else:
                parts[i] = 0
    return result
