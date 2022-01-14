from ctypes import cdll
p = cdll.LoadLibrary('D:\python\p.dll')
p.print_hello()