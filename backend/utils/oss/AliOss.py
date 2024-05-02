import oss2
from oss2.credentials import EnvironmentVariableCredentialsProvider


class Oss:
    def __init__(self, filename):
        self.filename = filename
        self.endpoint = 'oss-cn-hangzhou.aliyuncs.com'
        self.bucket_name = 'ruoliii'
        self.auth = oss2.ProviderAuth(EnvironmentVariableCredentialsProvider())
        self.avatar_update_path = 'static/img/' + filename
        self.bucket = oss2.Bucket(self.auth, self.endpoint, self.bucket_name)

    def update_to_oss(self, file):  # file 为二进制字节流
        print("Hello updateToOSS")
        res = self.bucket.put_object(self.avatar_update_path, file)  # 将文件上传到该地址下
        #  头像文件的浏览地址
        storage_avatar_url = 'https://{}.{}/'.format(self.bucket_name, self.endpoint) + self.avatar_update_path

        if res.status == 200:
            return storage_avatar_url
        else:
            return None
