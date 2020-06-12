# -*- coding: utf-8 -*-
from qiniu import QiniuMacAuth, http, urlsafe_base64_encode
import json


def createTemplate(access_key, secret_key, body):
    """
    创建模板
    https://developer.qiniu.com/qvs/api/6721/create-template
    :param access_key: 公钥
    :param secret_key: 私钥
    :param body: 请求体
        {
            "name": 必填，模版名称，格式为 1 ~ 100个字符，可包含小写字母、数字、中划线
            "desc"：非必填，模板描述
            "bucket": 必填，模版对应的对象存储的bucket
            "deleteAfterDays": 必填，存储过期时间,默认永久不过期
            "fileType": 必填，文件存储类型,取值：0（普通存储）,1（低频存储）
            "recordFileFormat": 非必填，录制文件存储格式,取值：0（m3u8格式存储）
            "templateType": 必填，模板类型,取值：0（录制模版）, 1（截图模版）
            "recordType"：templateType为0时须指定，录制模式, 0（不录制）,1（实时录制）
            "jpgOverwriteStatus": templateType为1时须指定，开启覆盖式截图(一般用于流封面)
            "jpgSequenceStatus"：templateType为1时须指定，开启序列式截图
            "jpgOnDemandStatus"：templateType为1时须指定，开启按需截图
            "recordInterval"：非必填，录制文件时长 单位为秒,600~3600
            "snapInterval": 非必填，截图间隔, 单位为秒, 10~600
        }

    :return:
        {

        }
    """
    auth = QiniuMacAuth(access_key, secret_key)

    # 请求URL
    url = "http://qvs.qiniuapi.com/v1/templates"

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
    "name": "test0013",
    "desc": "this is a test",
    "delateAfterDays": 7,
    "interval": 5,
    "templateType": 1,
    "bucket": "yangjunren",
    "jpgOverwriteStatus": True,
    "jpgSequenceStatus": True,
    "jpgOnDemandStatus": True
}

headers, result = createTemplate(access_key, secret_key, body)
print(f'{headers}\n{result}')
