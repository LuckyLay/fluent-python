"""
    集合推导
"""

from unicodedata import name

if __name__ == '__main__':
    set_a = {chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), "")}
    print(set_a)