# -*- coding: utf-8 -*-
from qiniu import QiniuMacAuth, http
import json


def staticStreamDomain(access_key, secret_key, namespaceid, streamid, body):
    """
    静态模式流地址
    https://developer.qiniu.com/qvs/api/6800/static-model
    :param access_key: 公钥
    :param secret_key: 私钥
    :param namespaceid: 空间名称ID
    :param streamid: 流ID
    :param body: 请求体
            {
                "domain": "qvs-live-hdl.qiniu.com", // 必填，域名
                "domainType": "liveHdl", // 必填，域名类型,取值："publishRtmp":rtmp推流, "liveRtmp": rtmp播放, "liveHls": hls播放, "liveHdl": flv播放
                "urlExpireSec": // 非必填，推流地址过期时间(单位为秒)
            }
    :return:
        200 { }
    """
    auth = QiniuMacAuth(access_key, secret_key)

    url = f"http://qvs.qiniuapi.com/v1/namespaces/{namespaceid}/streams/{streamid}/domain"

    # 发起POST请求
    ret, res = http._post_with_qiniu_mac(url, body, auth)
    headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log}

    # 格式化响应体
    Headers = json.dumps(headers, indent=4, ensure_ascii=False)
    result = json.dumps(ret, indent=4, ensure_ascii=False)
    return Headers, result


def dynamicStreamDomain(access_key, secret_key, namespaceid, streamid, body):
    """
    动态模式流地址
    https://developer.qiniu.com/qvs/api/6801/dynamic-model
    :param access_key: 公钥
    :param secret_key: 私钥
    :param namespaceid: 空间名称ID
    :param streamid: 流ID
    :param body: 请求体
            {
                "publishIp": "", // 非必填，推流端对外IP地址
                "playIp": "", // 非必填，拉流端对外IP地址
                "urlExpireSec": // 非必填，推流地址过期时间(单位为秒)
            }
    :return:
        200 { }
    """
    auth = QiniuMacAuth(access_key, secret_key)

    url = f"http://qvs.qiniuapi.com/v1/namespaces/{namespaceid}/streams/{streamid}/urls"

    # 发起POST请求
    ret, res = http._post_with_qiniu_mac(url, body, auth)
    headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log}

    # 格式化响应体
    Headers = json.dumps(headers, indent=4, ensure_ascii=False)
    result = json.dumps(ret, indent=4, ensure_ascii=False)
    return Headers, result


# # 七牛账号 AK、SK
access_key = '<access_key>'
secret_key = '<secret_key>'


# 空间ID
namespaceid = "2xenzw02hisz2"

#  流ID
streamid = "flow_test"

"""静态模式请求体"""
# # 请求体
# body = {
#     "domain": "qvs-publish.qiniu.com",
#     "domainType": "publishRtmp"
# }
#
# headers, result = staticStreamDomain(access_key, secret_key, namespaceid, streamid, body)
# print(f'{headers}\n{result}')

"""动态模式请求体"""
# 请求体
body = {
    "publishIp": "",
    "playIp": "publishRtmp"
}

headers, result = dynamicStreamDomain(access_key, secret_key, namespaceid, streamid, body)
print(f'{headers}\n{result}')
