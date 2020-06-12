# -*- coding: utf-8 -*-
from qiniu import QiniuMacAuth, http
import json


def createStreams(access_key, secret_key, namespaceId, body):
    """
    创建流
    https://developer.qiniu.com/qvs/api/6734/create-flow
    :param access_key: 公钥
    :param secret_key: 私钥
    :param namespaceId: 空间ID
    :param body： 请求体
            {
                "streamId":"device009", // 必填，流名称, 流名称在空间中唯一，可包含 字母、数字、中划线、下划线；1 ~ 100 个字符长；创建后将不可修改
                "desc":"流说明信息", // 非必填，关于流的描述信息
                "recordTemplateId":"d102sns2mwhd", // 非必填，录制模版ID，配置流维度的录制模板
                "snapshotTemplateId":"截图模板ID" // 非必填，截图模版ID，配置流维度的截图模板
            }

    :return:
           200 { }
    """
    auth = QiniuMacAuth(access_key, secret_key)

    # 请求URL
    url = f"http://qvs.qiniuapi.com/v1/namespaces/{namespaceId}/streams"

    # 发起POST请求
    ret, res = http._post_with_qiniu_mac(url, body, auth=auth)
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

# 请求体
body = {
    "streamId": "flow_test",
    "desc": "创建流测试"
    # "recordTemplateId": "d102sns2mwhd"
}

headers, result = createStreams(access_key, secret_key, namespaceId, body)
print(f'{headers}\n{result}')
