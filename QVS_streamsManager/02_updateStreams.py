# -*- coding: utf-8 -*-
from qiniu import QiniuMacAuth, http
import json


def updateStreams(access_key, secret_key, namespaceId, streamId, body):
    """
    更新流
    https://developer.qiniu.com/qvs/api/6758/update-the-flow
    :param access_key: 公钥
    :param secret_key: 私钥
    :param namespaceId: 空间ID
    :param streamId: 流名ID
    :param body: 请求体
                {
                    "operations":[
                        {"key":"desc", //  必填，要修改的参数：desc 流描述;recordTemplateId 录制模版ID;snapshotTemplateId 截图模版ID; disabled 流是否被禁用
                        "op":"replace", // 必填，op操作(目前支持replace和delete)
                        "value":true}， // 必填，要修改的参数对应的value(当op为delete的时候可以忽略)
                        { },
                        .....
                ]
                }

    :return:
            {
                "code": 200
            }
    """
    auth = QiniuMacAuth(access_key, secret_key)

    # 请求URL
    url = f"http://qvs.qiniuapi.com/v1/namespaces/{namespaceId}/streams/{streamId}"

    # 发起PATCH请求
    ret, res = http._patch_with_qiniu_mac(url, body, auth)
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

# 请求体
body = {
    "operations": [
        {"key": "desc", "op": "replace", "value": "ceshi121212"}
    ]
}

headers, result = updateStreams(access_key, secret_key, namespaceId, streamId, body)
print(f'{headers}\n{result}')
