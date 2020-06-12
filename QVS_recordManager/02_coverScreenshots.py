# -*- coding: utf-8 -*-
from qiniu import QiniuMacAuth, http
import json, time


# 日期转时间戳
def time2timestamp(datetime):
    # 转为时间数组
    timeArray = time.strptime(datetime, "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(timeArray))
    return timeStamp


def streamSnapshotss(access_key, secret_key, namespaceId, streamId):
    """
    获取直播封面截图
    https://developer.qiniu.com/qvs/api/6814/the-cover-for-screenshots
    :param access_key: 公钥
    :param secret_key: 私钥
    :param namespaceId: 必填项，空间ID
    :param streamId: 必填项，流ID

    :return:
        200
            {
                "url": "http://prlghu509.test.bkt.clouddn.com/snapshot/jpg/2akrarrzns76w/t0.jpg?e=1588124787&token=Ves3WTXC8XnEHT0I_vacEQQz-9jrJZxNExcmarzQ:bH8s5m5N5Ugp2wo6ACRUVeIK280"
            }
    """
    auth = QiniuMacAuth(access_key, secret_key)

    # 请求URL
    url = f"http://qvs.qiniuapi.com/v1/namespaces/{namespaceId}/streams/{streamId}/cover"

    # 发起GET请求
    ret, res = http._get_with_qiniu_mac(url, params=None, auth=auth)
    result = json.loads(res.text_body)
    if res.status_code == 401:
        headers = {"code": res.status_code, "reqid": res.req_id, "error": result["error"]}
    elif res.status_code != 401 and res.text_body:
        headers = {"code": result["code"], "reqid": res.req_id, "xlog": result["error"]}
    else:
        headers = {"code": res.text_body, "reqid": res.req_id, "xlog": res.x_log}

    # 格式化响应体
    Headers = json.dumps(headers, indent=4, ensure_ascii=False)
    result = json.dumps(ret, indent=4, ensure_ascii=False)
    return Headers, result


# 七牛账号 AK、SK
access_key = '<access_key>'
secret_key = '<secret_key>'

# 空间ID
namespaceId = "2xenzw02hisz2"

# 流ID
streamId = "flow_test"

headers, result = streamSnapshotss(access_key, secret_key, namespaceId, streamId)
print(f'{headers}\n{result}')
