# -*- coding: utf-8 -*-
from qiniu import QiniuMacAuth, http
import json, time


# 日期转时间戳
def time2timestamp(datetime):
    # 转为时间数组
    timeArray = time.strptime(datetime, "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(timeArray))
    return timeStamp


def streamSnapshotss(access_key, secret_key, namespaceId, streamId, startDate, endDate, type, line=30, marker=None):
    """
    获取截图列表
    https://developer.qiniu.com/qvs/api/6749/list-stream-snapshots
    :param access_key: 公钥
    :param secret_key: 私钥
    :param namespaceId: 必填项，空间ID
    :param streamId: 必填项，流ID
    :param type: 必填项，1:实时截图对应的图片列表
    :param line: 非必填，限定返回截图的个数，只能输入1-100的整数，不指定默认返回30个
    :param startDate:  必填项，查询开始时间(unix时间戳,单位为秒)
    :param endDate: 必填项，查询结束时间(unix时间戳,单位为秒)
    :param marker: 非必填，上一次查询返回的标记，用于提示服务端从上一次查到的位置继续查询，不指定表示从头查询

    :return:
        200 { }
    """
    auth = QiniuMacAuth(access_key, secret_key)

    start = time2timestamp(startDate)

    end = time2timestamp(endDate)

    if marker is None:
        # 请求URL
        url = f"http://qvs.qiniuapi.com/v1/namespaces/{namespaceId}/streams/{streamId}/snapshots?type={type}&start={start}&end={end}&line={line}"
    else:
        url = f"http://qvs.qiniuapi.com/v1/namespaces/{namespaceId}/streams/{streamId}/snapshots?type={type}&start={end}&end={end}&line={line}&marker={marker}"
    # 发起POST请求
    ret, res = http._get_with_qiniu_mac(url, params=None, auth=auth)
    if res.text_body:
        result = json.loads(res.text_body)
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

# 1:实时截图对应的图片列表
type = 1

# 推流开始时间（Unix 时间戳）
startDate = "2020-06-08 00:00:00"

# 推流结束时间（Unix 时间戳）
endDate = "2020-06-09 00:00:00"

headers, result = streamSnapshotss(access_key, secret_key, namespaceId, streamId, startDate, endDate, type)
print(f'{headers}\n{result}')
