# -*- coding: utf-8 -*-
from qiniu import QiniuMacAuth, http
import json


def deleteTemplate(access_key, secret_key, templateId):
    """
    删除模板
    https://developer.qiniu.com/qvs/api/6722/delete-template
    :param access_key: 公钥
    :param secret_key: 私钥
    :param templateId: 模板ID

    :return:
            {
                "code": 200
            }
    """
    auth = QiniuMacAuth(access_key, secret_key)

    # 请求URL
    url = f"http://qvs.qiniuapi.com/v1/templates/{templateId}"

    # 发起POST请求
    ret, res = http._delete_with_qiniu_mac(url, params=None, auth=auth)
    headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log}

    # 格式化响应体
    Headers = json.dumps(headers, indent=4, ensure_ascii=False)
    result = json.dumps(ret, indent=4, ensure_ascii=False)
    return Headers, result


# 七牛账号 AK、SK
access_key = '<access_key>'
secret_key = '<secret_key>'


# 模板ID
templateId = "2xenzw02x5pw0"

headers, result = deleteTemplate(access_key, secret_key, templateId)
print(f'{headers}\n{result}')
