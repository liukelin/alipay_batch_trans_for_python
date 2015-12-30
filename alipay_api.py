#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2015    liukelin
# @author: iiukelin      314566990@qq.com
import time
import alipay_config as alipay_config_class
from lib import alipay_submit_class
from lib import alipay_notify_class

def alipay_pay(data = {}):
    config_ = alipay_config_class.alipay_config()

    time_ = time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))
    date_ = time.strftime("%Y%m%d",time.localtime(time.time()))

    #服务器异步通知页面路径
    notify_url = "http://xxxx.com/notify_url.php";
    #需http://格式的完整路径，不允许加?id=123这类自定义参数

    #付款账号
    email = 'xxxx@126.com'#data['WIDemail']
    #必填

    #付款账户名
    account_name = 'xxxx有限公司' #data['WIDaccount_name']
    #必填，个人支付宝账号是真实姓名公司支付宝账号是公司名称

    #付款当天日期
    pay_date = date_    #data['WIDpay_date'] 
    #必填，格式：年[4位]月[2位]日[2位]，如：20100801

    #批次号
    batch_no = data['WIDbatch_no'];
    #必填，格式：当天日期[8位]+序列号[3至16位]，如：201008010000001

    #付款总金额
    batch_fee = data['WIDbatch_fee'];
    #必填，即参数detail_data的值中所有金额的总和

    #付款笔数
    batch_num = data['WIDbatch_num'];
    #必填，即参数detail_data的值中，“|”字符出现的数量加1，最大支持1000笔（即“|”字符出现的数量999个）

    #付款详细数据
    detail_data = data['WIDdetail_data'];
    #必填，格式：流水号1^收款方帐号1^真实姓名^付款金额1^备注说明1|流水号2^收款方帐号2^真实姓名^付款金额2^备注说明2....


    #构造要请求的参数数组，无需改动
    parameter = {
        "service"      : "batch_trans_notify",
        "partner"     : config_['partner'],
        "notify_url"  : notify_url,
        "email"         : email,
        "account_name" : account_name,
        "pay_date"      : pay_date,
        "batch_no"      : batch_no,
        "batch_fee"     : batch_fee,
        "batch_num"   : batch_num,
        "detail_data"   : detail_data,
        "_input_charset" : config_['input_charset'].lower()
    }

    #建立请求
    alipaySubmit = alipay_submit_class.AlipaySubmit(config_)
    html_text = alipaySubmit.buildRequestForm(parameter, "get", "ok")
    return html_text
