# -*- coding: utf-8 -*-
# @Author : qinlei
# @Time : 2023/1/17 11:34 上午
# @Function:

def handleParameters(url, param):
    if param is None:
        return
    URL_PARAM_INDEX_TAG = '?'
    if url.find(URL_PARAM_INDEX_TAG) == -1:
        url += URL_PARAM_INDEX_TAG
    for key, value in param.items():
        url += '%s%s%s%s' % (key, '=', value, '&')
    return url[:-1]
