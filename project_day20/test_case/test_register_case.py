import unittest
from comm_modul import myddt
from handle_func.handle_excel import handle_excel_class
from handle_func.handle_path import DATA_DIR
import os
import requests
from handle_func.handle_log import  log
from handle_func.handle_config import conf

@myddt.ddt
class test_register_class(unittest.TestCase):
    excel=handle_excel_class(os.path.join(DATA_DIR,'register_login.xlsx'),'register')
    case=excel.read_excel()
    @myddt.data(*case)
    def test_register(self,case):
        headers = eval(conf.get("header", "headers"))
        url=conf.get("address","url")+case['url']
        params=eval(case['params'])
        expected=eval(case['expected'])
        methods=case['methods']
        rows=case['case_id']+1
        response=requests.request(url=url,json=params,method=methods,headers=headers)
        result=response.json()
        try:
            self.assertEqual(expected['code'],result['code'])
            self.assertEqual(expected['msg'],result['msg'])
        except Exception as E:
            self.excel.write_excel(row=rows,column=7,value="失败")
            log.error(f"{case['title']}执行失败")
            log.exception(E)
            raise E
        else:
            self.excel.write_excel(row=rows,column=7,value='通过')
            log.info(f"{case['title']}执行通过")

