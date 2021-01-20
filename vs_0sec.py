#!/usr/bin/env python3
# coding=utf-8
# python version 3.7
# 零组资料文库离线漏洞名搜索 by 时光难逆

import os, sys
import json, sqlite3, time
import requests


# 功能：更新 、查询
class search_0sec():
    def __init__(self):
        self._db_name = 'vul-0sec.db'  # 数据库文件名
        self._table_name = '0sec'
        if os.path.exists(self._db_name) and os.path.isfile(self._db_name):
            pass
        else:
            print('未找到数据库文件vul-0sec.db，将自动创建空库')

    # 下载漏洞json到本地
    def downloadjson(self):
        u = 'https://wiki.0-sec.org/api/wiki/tree'
        # 循环直到获取成功（有时下载不成功）
        while 1:
            try:
                _res = requests.get(u, verify=False)
                if _res.status_code == 200:
                    json.loads(_res.text)  # 能被json解析表示数据完整
                    with open('tree.json', 'w', encoding='utf-8') as f:
                        f.write(_res.text)
                    break
            except:
                time.sleep(3)
    print('tree.json文件下载成功')

    # 将json转存到sqlit3数据库便于查询
    def dump2sqlit3(self):
        print('开始将json转换到sqlite3数据库')
        # 创建库
        _conn = sqlite3.connect(self._db_name)
        # 创建表,只保留2级目录
        qy = """CREATE TABLE IF NOT EXISTS "%s"(
           count INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
           name1 TEXT,name2 TEXT,data TEXT);"""
        _conn.execute(qy % self._table_name)
        qy = """delete from "%s";"""
        _conn.execute(qy % self._table_name)  # 清空表（偷懒）
        qy = """update sqlite_sequence SET seq = 0 where name ='%s';"""
        _conn.execute(qy % self._table_name)  # 清空自增长
        # 读取数据
        with open('tree.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        # 获取漏洞列表
        for v1 in data['data']:  # 输出大类别
            name1 = v1['name']
            for v2 in v1['treeNode']:  # 输出小类别
                name2 = v2['name']
                vul_list = self.jsontreeNode(v2)
                # 将漏洞信息存到数据库
                cur = _conn.cursor()
                qy_config = "INSERT INTO '%s'(name1,name2,data)VALUES(?,?,?);" % self._table_name
                for vinfo in vul_list:
                    v = (str(name1), str(name2), str(vinfo))
                    cur.execute(qy_config, v)
                _conn.commit()
            print("[{}] 转换完成".format(name1))
        _conn.close()

    # 从2级节点中循环提取子节点
    def jsontreeNode(self, v2=json):
        result = []
        v3_list = v2['treeNode']
        if type(v3_list) is not list:  # 直到没有子节点，返回漏洞信息
            result.append(v2)
            return result
        else:  # 如果有子节点就循环获取内部信息
            for v3 in v3_list:
                result.extend(self.jsontreeNode(v3))
        return result

    # 查询数据库返回格式化结果
    def searchsqlit3(self, keyword=str):
        _conn = sqlite3.connect(self._db_name)
        _nodes = list(_conn.execute("SELECT * FROM '{0}' WHERE data like '%{1}%'".format(self._table_name, keyword)))
        for node in _nodes:
            vinfo = eval(node[3])
            # 根据命令规则拼接url
            http_h = 'https://wiki.0-sec.org/api/wiki/articleInfo/' + str(vinfo['id'])
            name = node[1] + '|' + node[2] + '|' + vinfo['name']
            print('{0}\t{1}'.format(name, http_h))
        _conn.close()


if __name__ == '__main__':
    if sys.argv.__len__() < 2:
        print("""零组资料文库离线漏洞名搜索,功能：更新 、查询
        -up:在线更新数据
        -offline:离线更新数据库（根据tree.json文件更新）
        -s [keyword]:查询关键字
        """)
        exit(0)
    _0sec = search_0sec()
    if sys.argv[1] == '-up':
        _0sec.downloadjson()
        _0sec.dump2sqlit3()
        print('更新完成')
    if sys.argv[1] == '-s':
        _0sec.searchsqlit3(sys.argv[2])
    if sys.argv[1] == '-offline':
        _0sec.dump2sqlit3()
        print('更新完成')
