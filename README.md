# 0sec-search
新版零组资料文库离线漏洞名搜索，功能：更新 、查询 （不包含漏洞详情）

项目日志20200707：网站需翻墙，增加离线更新方式 

项目日志20200709：网站更新大量工控和物联网文章

项目日志20201013：网站封闭不再对外开放，上传tree.json文件是最新版本（10-8），请自行离线更新数据库

以后漏洞数据库文件会“季更”或“年更”，请各位自行更新

kali@kali:~$ python3 vs_0sec.py

    零组资料文库离线漏洞名搜索,功能：更新 、查询
        -up:在线更新数据
        -offline:离线更新数据库（根据tree.json文件更新）
        -s [keyword]:查询关键字

# 使用：更新数据库
kali@kali:~$ python3 vs_0sec.py -up

    未找到数据库文件vulsearch-database.db，将自动创建空库

# 使用：查询关键字
kali@kali:~$ python3 vs_0sec.py -s mail

    Web安全|Coremail|Coremail配置文件信息泄漏       https://wiki.0-sec.org/api/wiki/articleInfo/5661
    安全技术|Disable function| mail         https://wiki.0-sec.org/api/wiki/articleInfo/6237

# 使用：离线更新
浏览器访问 https://wiki.0-sec.org/api/wiki/tree 将json数据保存到本地（与脚本同目录下），执行命令更新数据库

kali@kali:~$ python3 vs_0sec.py -offline

    更新完成


当前项目漏洞信息版本20200709

