import ctypes

laxzlib = ctypes.CDLL('./laxzlib.so')

laxzlib.dog()

laxzlib.hi_user()