# -*- coding: utf-8 -*-
from qiniu import QiniuMacAuth, http
import json, time


# 日期转时间戳
def time2timestamp(datetime):
    # 转为时间数组
    timeArray = time.strptime(datetime, "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(timeArray))
    return timeStamp


def recordHistories(access_key, secret_key, namespaceId, streamId, start, end, line=10, marker=None):
    """
    查询录制记录
    https://developer.qiniu.com/qvs/api/6745/query-recordhistories
    :param access_key: 公钥
    :param secret_key: 私钥
    :param offset: 非必填，在全部namespace中的偏移量，时间戳
    :param line: 非必填，一次返回多少条
    :param sortBy: 非必填，asc 表示升序, desc 表示降序, 默认按创建时间降序排列(可参与排序的字段有createdAt, updatedAt).asc:updatedAt表示更新时间从小到大排序, desc:updatedAt表示更新时间从大到小排序
    :param templateType: 非必填，模板类型，取值：0（录制模版）, 1（截图模版）
    :param match: 非必填，模糊匹配查询(模版名称包含match串时返回)

    :return:
        200 { }
    """
    auth = QiniuMacAuth(access_key, secret_key)

    start = time2timestamp(startDate)

    end = time2timestamp(endDate)

    if marker is None:
        # 请求URL
        url = f"http://qvs.qiniuapi.com/v1/namespaces/{namespaceId}/streams/{streamId}/recordhistories?start={start}&end={end}&line={line}"
    else:
        url = f"http://qvs.qiniuapi.com/v1/namespaces/{namespaceId}/streams/{streamId}/recordhistories?start={start}&end={end}&marker={marker}&line={line}"
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

headers, result = recordHistories(access_key, secret_key, namespaceId, streamId, startDate, endDate)
print(f'{headers}\n{result}')
