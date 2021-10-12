# -*- coding: utf-8 -*-
""" 
@Time    : 2021/10/11 15:08
@Author  : MaSai
@FileName: json_demo.py
@SoftWare: PyCharm
"""
# def get_json():
#     with open("./quote.json") as f:
#         dates=f.read()
#         print(dates)
#         return dates

# def test_json():
#     date=get_json()["data"]
#     print(date)

jsons={
	"data": {
		"items": [{
			"market": {
				"status_id": 5,
				"region": "CN",
				"status": "交易中",
				"time_zone": "Asia/Shanghai",
				"time_zone_desc": "null",
				"delay_tag": 0
			},
			"quote": {
				"symbol": "SZ000002",
				"code": "000002",
				"exchange": "SZ",
				"name": "万科A",
				"type": 11,
				"sub_type": "1",
				"status": 1,
				"current": 22.3,
				"currency": "CNY",
				"percent": 4.99,
				"chg": 1.06,
				"timestamp": 1633921776000,
				"time": 1633921776000,
				"lot_size": 100,
				"tick_size": 0.01,
				"open": 21.28,
				"last_close": 21.24,
				"high": 22.51,
				"low": 21.25,
				"avg_price": 22.069,
				"volume": 90534608,
				"amount": 1.997996587E9,
				"turnover_rate": 0.93,
				"amplitude": 5.93,
				"market_capital": 2.59246049263E11,
				"float_market_capital": 2.1670143781E11,
				"total_shares": 11625383375,
				"float_shares": 9717553265,
				"issue_date": 665078400000,

			},
			"others": {
				"cyb_switch": "true"
			},
			"tags": []
		}, {
			"market": {
				"status_id": 5,
				"region": "CN",
				"status": "交易中",
				"time_zone": "Asia/Shanghai",
				"time_zone_desc": "null",
				"delay_tag": 0
			},
			"quote": {
				"symbol": "SH601899",
				"code": "601899",
				"exchange": "SH",
				"name": "紫金矿业",
				"type": 11,
				"sub_type": "ASH",
				"status": 1,
				"current": 11.1,
				"currency": "CNY",
				"percent": 8.19,
				"chg": 0.84,
				"timestamp": 1633921777180,
				"time": 1633921777180,
				"lot_size": 100,
				"tick_size": 0.01,
				"open": 10.73,
				"last_close": 10.26,
				"high": 11.19,
				"low": 10.62,
				"avg_price": 10.917,
				"volume": 387561288,
				"amount": 4.231166432E9,
				"turnover_rate": 1.89,
				"amplitude": 5.56,
				"market_capital": 2.92236384864E11,
				"float_market_capital": 2.27490966204E11,
				"total_shares": 26327602240,
				"float_shares": 20494681640,
				"issue_date": 1209052800000,
				"lock_set": "null",
				"current_year_percent": 20.98,
				"high52w": 14.8148,
				"low52w": 6.0741,
				"limit_up": 11.29,
				"limit_down": 9.23,
				"volume_ratio": 4.8,
				"eps": 0.41,
				"pe_ttm": 27.22,
				"pe_forecast": 21.976,
				"pe_lyr": 44.9,
				"navps": 2.37,
				"pb": 4.684,
				"dividend": 0.12,
				"dividend_yield": 1.081,
				"profit": 6.508553913E9,
				"profit_four": 1.0736195836E10,
				"profit_forecast": 1.3298056796E10,
				"pledge_ratio": 0.3,
				"goodwill_in_net_assets": 0.4696748471476844,

			},
			"others": {
				"cyb_switch": "true"
			},
			"tags": []
		}, {
			"market": {
				"status_id": 5,
				"region": "CN",
				"status": "交易中",
				"time_zone": "Asia/Shanghai",
				"time_zone_desc": "null",
				"delay_tag": 0
			},
			"quote": {
				"symbol": "SH601919",
				"code": "601919",
				"exchange": "SH",
				"name": "中远海控",
				"type": 11,
				"sub_type": "ASH",
				"status": 1,
				"current": 16.98,
				"currency": "CNY",
				"percent": 1.07,
				"chg": 0.18,
				"timestamp": 1633921775100,
				"time": 1633921775100,
				"lot_size": 100,
				"tick_size": 0.01,
				"open": 17.45,
				"last_close": 16.8,
				"high": 17.46,
				"low": 16.72,
				"avg_price": 17.055,
				"volume": 172960249,
				"amount": 2.949883223E9,
				"turnover_rate": 1.53,
				"amplitude": 4.4,
				"market_capital": 2.71912665479E11,
				"float_market_capital": 1.9239709707E11,
				"total_shares": 16013702325,
				"float_shares": 11330806659,
				"issue_date": 1182787200000,
				"lock_set": "null",
				"current_year_percent": 80.82,
				"high52w": 25.6881,
				"low52w": 4.507,
				"limit_up": 18.48,
				"limit_down": 15.12,
				"volume_ratio": 1.25,
				"eps": 2.87,
				"pe_ttm": 5.926,
				"pe_forecast": 3.665,
				"pe_lyr": 27.391,
				"navps": 5.04,
				"pb": 3.369,
				"dividend": 0.0,
				"dividend_yield": 0.0,
				"profit": 9.92709823901E9,
				"profit_four": 4.588777746038E10,
				"profit_forecast": 7.4195686297E10,
			},
			"others": {
				"cyb_switch": "true"
			},
			"tags": []
		}, {
			"market": {
				"status_id": 5,
				"region": "CN",
				"status": "交易中",
				"time_zone": "Asia/Shanghai",
				"time_zone_desc": "null",
				"delay_tag": 0
			},
			"quote": {
				"symbol": "SH601318",
				"code": "601318",
				"exchange": "SH",
				"name": "中国平安",
				"type": 11,
				"sub_type": "ASH",
				"status": 1,
				"current": 52.4,
				"currency": "CNY",
				"percent": 0.58,
				"chg": 0.3,
				"timestamp": 1633921776680,
				"time": 1633921776680,
				"lot_size": 100,
				"tick_size": 0.01,
				"open": 52.1,
				"last_close": 52.1,
				"high": 53.39,
				"low": 51.94,
				"avg_price": 52.743,
				"volume": 96386990,
				"amount": 5.083755957E9,
				"turnover_rate": 0.89,
				"amplitude": 2.78,
				"market_capital": 9.57884649884E11,
				"float_market_capital": 5.67631619695E11,
				"total_shares": 18280241410,
				"float_shares": 10832664498,
				"issue_date": 1172678400000,
				"lock_set": "null",
				"current_year_percent": -38.62,
				"high52w": 92.8649,
				"low52w": 47.3,
				"limit_up": 57.31,
				"limit_down": 46.89,
				"volume_ratio": 2.24,
				"eps": 7.24,
				"pe_ttm": 7.234,
				"pe_forecast": 8.257,
				"pe_lyr": 6.694,
				"navps": 43.32,
				"pb": 1.21,
				"dividend": 2.2800000000000002,
				"dividend_yield": 4.351,
				"profit": 1.43099E11,
				"profit_four": 1.32421E11,
				"profit_forecast": 1.1601E11,
				"pledge_ratio": 3.26,
				"goodwill_in_net_assets": 2.946064589132093,
			},
			"others": {
				"cyb_switch": "true"
			},
			"tags": []
		}],
		"items_size": 4
	},
	"error_code": 0,
	"error_description": ""
}


def test_json():
    date=jsons["data"]
    print(date)


import json
def test_json_dumps():

	# json.dumps	将 Python 对象编码成 JSON 字符串
	data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]
	print(type(data))
	data2 = json.dumps(data)
	print(type(data2))
	print(data2)

	print("____________________________________________")
	# json.loads 用于解码 JSON 数据。该函数返回 Python 字段的数据类型
	jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}';
	# jsonData={'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
	print(type(jsonData))
	text = json.loads(jsonData)
	print(type(text))
	print(text)

