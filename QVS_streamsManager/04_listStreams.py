# -*- coding: utf-8 -*-
from qiniu import QiniuMacAuth, http
import json


def listStreams(access_key, secret_key, namespaceid, offset=None, line=10, qtype=0, prefix=None,
                   sortBy="desc:createdAt"):
    """
    获取流列表
    https://developer.qiniu.com/qvs/api/6737/query-list-flow
    :param access_key: 公钥
    :param secret_key: 私钥
    :param namespaceid: 空间名称ID
    :param offset: 在全部namespace中的偏移量，时间戳
    :param line: 一次返回多少条
    :param qtype: 查询流类型， 0:全部,1:在线流,2:离线流
    :param prefix: 流ID 前缀，可以流ID 前缀进行检索查询
    :param sortBy: asc 表示升序, desc 表示降序, 默认按创建时间降序排列(可参与排序的字段有createdAt, updatedAt).asc:updatedAt表示更新时间从小到大排序, desc:updatedAt表示更新时间从大到小排序

    :return:
        200 { }
    """
    auth = QiniuMacAuth(access_key, secret_key)
    if offset is None and prefix is None:
        # 请求URL
        url = f"http://qvs.qiniuapi.com/v1/namespaces/{namespaceid}?line={line}&sortBy={sortBy}&qtype={qtype}"
    else:
        url = f"http://qvs.qiniuapi.com/v1/namespaces/{namespaceid}?offset={offset}&line={line}&qtype={qtype}&prefix={prefix}&sortBy={sortBy}"
    # 发起GET请求
    ret, res = http._get_with_qiniu_mac(url, params=None, auth=auth)
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

headers, result = listStreams(access_key, secret_key, namespaceid, )
print(f'{headers}\n{result}')
