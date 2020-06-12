# -*- coding: utf-8 -*-
from qiniu import QiniuMacAuth, http
import json


def disableNamespaces(access_key, secret_key, namespaceId):
    """
    启用空间
    https://developer.qiniu.com/qvs/api/6760/enable-the-space
    :param access_key: 公钥
    :param secret_key: 私钥
    :param namespaceId: 空间ID

    :return:
            {
                "code": 200
            }
    """
    auth = QiniuMacAuth(access_key, secret_key)

    # 请求URL
    url = f"http://qvs.qiniuapi.com/v1/namespaces/{namespaceId}/enabled"

    # 发起POST请求
    ret, res = http._post_with_qiniu_mac(url, None, auth=auth)
    headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log}

    # 格式化响应体
    Headers = json.dumps(headers, indent=4, ensure_ascii=False)
    result = json.dumps(ret, indent=4, ensure_ascii=False)
    return Headers, result


# 七牛账号 AK、SK
access_key = '<access_key>'
secret_key = '<secret_key>'

# 需要查询的空间ID
namespaceId = "2xenzw02hisz2"

headers, result = disableNamespaces(access_key, secret_key, namespaceId)
print(f'{headers}\n{result}')
