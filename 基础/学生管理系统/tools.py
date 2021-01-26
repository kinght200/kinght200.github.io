# 工具类
import hashlib


def encrypt_password(password, x='afsoijweogj4wiu'):
    h = hashlib.sha256()
    h.update(password.encode('utf8'))
    # 生怕人家加密不靠谱，又加了一成
    h.update(x.encode('utf8'))
    return h.hexdigest()
