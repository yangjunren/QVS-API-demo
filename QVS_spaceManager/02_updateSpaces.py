# -*- coding: utf-8 -*-
from qiniu import QiniuMacAuth, http
import json


def updateNamespaces(access_key, secret_key, namespaceId, body):
    """
    更新空间
    https://developer.qiniu.com/qvs/api/6728/update-namespace
    :param access_key: 公钥
    :param secret_key: 私钥
    :param namespaceId: 空间ID
    :param body: 请求体
            {
                "operations":[
                    {"key":"recordTemplateApplyAll", // 要修改的参数：name 空间名称;desc 空间描述;callBack 回调地址;recordTemplateId 录制模版ID;snapshotTemplateId 截图模版ID; recordTemplateApplyAll 空间模版是否应用到全局; snapshotTemplateApplyAll 截图模版是否应用到全局
                    "op":"replace", // op操作(目前支持replace和delete)
                    "value":true}， // 要修改的参数对应的value(当op为delete的时候可以忽略)
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
    url = f"http://qvs.qiniuapi.com/v1/namespaces/{namespaceId}"

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

# 需要更新的空间ID
namespaceId = "2xenzw02hisz2"

# 请求体
body = {
    "operations": [
        {"key": "name", "op": "replace", "value": "yjr_test002"}
    ]
}

headers, result = updateNamespaces(access_key, secret_key, namespaceId, body)
print(f'{headers}\n{result}')
