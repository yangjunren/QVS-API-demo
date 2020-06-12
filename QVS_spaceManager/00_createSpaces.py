# -*- coding: utf-8 -*-
from qiniu import QiniuMacAuth, http, urlsafe_base64_encode
import json


def createNamespaces(access_key, secret_key, body):
    """
    创建空间
    https://developer.qiniu.com/qvs/api/6726/create-namespace
    :param access_key: 公钥
    :param secret_key: 私钥
    :param body: 请求体
        {
            "name": 必填，空间名称(格式"^[a-zA-Z0-9_-]{1,100}$")
            "desc"：非必填，空间描述
            "accessType": 必填，接入类型(rtmp或者gb28181)
            "rtmpUrlType": accessType为“rtmp”时 必填，推拉流地址计算方式，1:static, 2:dynamic
            "domains": rtmpUrlType为1时必填，直播域名，列表格式
            "callBack"：非必填，回调地址，可用于获取空间内设备/流状态更新时的信息
            "recordTemplateId": 非必填，录制模版ID，需要录制功能时输入对应的模板ID，录制模板ID可以模板管理中获取
            "snapshotTemplateId"：非必填，截图模版ID，需要截图功能时输入对应的模板ID，截图模板ID可以模板管理中获取
            "recordTemplateApplyAll"：非必填，空间模版是否应用到全局
            "snapshotTemplateApplyAll"：非必填，截图模版是否应用到全局
        }

    :return:
        {

        }
    """
    auth = QiniuMacAuth(access_key, secret_key)

    # 请求URL
    url = "http://qvs.qiniuapi.com/v1/namespaces"

    # 发起POST请求
    ret, res = http._post_with_qiniu_mac(url, body, auth)
    headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log}

    # 格式化响应体
    Headers = json.dumps(headers, indent=4, ensure_ascii=False)
    result = json.dumps(ret, indent=4, ensure_ascii=False)
    return Headers, result


# 七牛账号 AK、SK
access_key = '<access_key>'
secret_key = '<secret_key>'
# 请求体
body = {
    "name": "test00",
    "accessType": "rtmp",
    "rtmpUrlType": 2,
    # "domains": ["tests6.com"],
    # "recordTemplateId": "2akrarrzr7rh5"
}

headers, result = createNamespaces(access_key, secret_key, body)
print(f'{headers}\n{result}')
