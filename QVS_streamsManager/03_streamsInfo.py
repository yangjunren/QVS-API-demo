# -*- coding: utf-8 -*-
from qiniu import QiniuMacAuth, http
import json


def streamsInfo(access_key, secret_key, namespaceId, streamId):
    """
    查询流信息
    https://developer.qiniu.com/qvs/api/6736/query-information-flow
    :param access_key: 公钥
    :param secret_key: 私钥
    :param namespaceId: 空间ID
    :param streamId: 流名ID

    :return:
            {
                "code": 200
            }
    """
    auth = QiniuMacAuth(access_key, secret_key)

    # 请求URL
    url = f"http://qvs.qiniuapi.com/v1/namespaces/{namespaceId}/streams/{streamId}"

    # 发起GET请求
    ret, res = http._get_with_qiniu_mac(url, params=None, auth=auth)
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

# 流名ID
streamId = "flow_test"

headers, result = streamsInfo(access_key, secret_key, namespaceId, streamId)
print(f'{headers}\n{result}')
