# -*- coding: utf-8 -*-
from qiniu import QiniuMacAuth, http
import json, time


# 日期转时间戳
def time2timestamp(datetime):
    # 转为时间数组
    timeArray = time.strptime(datetime, "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(timeArray))
    return timeStamp


def listNamespaces(access_key, secret_key, namespaceId, streamId, startDate, endDate, offset=None, line=10):
    """
    获取推流记录
    https://developer.qiniu.com/qvs/api/6742/query-flow-records
    :param access_key: 公钥
    :param secret_key: 私钥
    :param offset: 非必填，在全部namespace中的偏移量，时间戳
    :param line: 非必填，一次返回多少条
    :param start: 必填，推流开始时间(unix timestamp in second)
    :param end: 必填，推流结束时间(unix timestamp in second)

    :return:
        200 { }
    """
    auth = QiniuMacAuth(access_key, secret_key)

    start = time2timestamp(startDate)

    end = time2timestamp(endDate)

    if offset is None:
        # 请求URL
        url = f"http://qvs.qiniuapi.com/v1/namespaces/{namespaceId}/streams/{streamId}/pubhistories?start={start}&end={end}&line={line}"
    else:
        url = f"http://qvs.qiniuapi.com/v1/namespaces?start={start}&end={end}&line={line}&offset={offset}"
    # 发起POST请求
    ret, res = http._get_with_qiniu_mac(url, params=None, auth=auth)
    headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log}

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

# 推流开始时间（Unix 时间戳）
startDate = "2020-06-08 00:00:00"

# 推流结束时间（Unix 时间戳）
endDate = "2020-06-09 00:00:00"

headers, result = listNamespaces(access_key, secret_key, namespaceId, streamId, startDate, endDate)
print(f'{headers}\n{result}')
