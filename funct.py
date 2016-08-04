import functools,time,uuid
import os
# int2 = functools.partial(int,base=2)
# print int2('1000000')

# def next_id(t=None):
#     '''
#     Return next id as 50-char string.
#
#     Args:
#         t: unix timestamp, default to None and using time.time().
#     '''
#     if t is None:
#         t = time.time()
#         print t
#     return '%015dHHH%s000' % (int(t * 1000), uuid.uuid4().hex)
#
# print next_id()

base_dir = os.path.dirname(os.path.dirname(__file__))
print base_dir

print os.path.join(base_dir,'template')