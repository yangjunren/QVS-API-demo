# -*- coding: utf-8 -*-
from qiniu import QiniuMacAuth, http
import json


def updateTemplate(access_key, secret_key, templateId, body):
    """
    更新模板
    https://developer.qiniu.com/qvs/api/6723/modify-the-template
    :param access_key: 公钥
    :param secret_key: 私钥
    :param templateId: 模板ID
    :param body: 请求体
            {
                "operations":[
                    {"key":"recordTemplateApplyAll", // 要修改的参数：name 模板名称;desc 模板描述;bucket 模版对应的对象存储的bucket;deleteAfterDays 存储过期时间,默认永久不过期;fileType 文件存储类型,取值：0（普通存储）,1（低频存储）; recordType 录制模式, 0（不录制）,1（实时录制）; jpgOverwriteStatus 开启覆盖式截图(一般用于流封面); recordInterval 录制文件时长 单位为秒, 600~3600; snapInterval 截图间隔, 单位为秒, 10~600; jpgSequenceStatus 开启序列式截图
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
    url = f"http://qvs.qiniuapi.com/v1/templates/{templateId}"

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

# 模板ID
templateId = "2xenzw02xy1h6"

# 请求体
body = {
    "operations": [
        {"key": "deleteAfterDays", "op": "replace", "value": 0}
    ]
}

headers, result = updateTemplate(access_key, secret_key, templateId, body)
print(f'{headers}\n{result}')
