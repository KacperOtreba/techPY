# sha md5
from hashlib import md5
# print(md5(b"Gruszka1").hexdigest())
# print(md5(b"Hruszka1").hexdigest())
# print(sha256(b"Gruszka1").hexdigest())




for i in range(9999):
  print(md5(str(i).encode("utf-8")).hexdigest())