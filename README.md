# 0sec-search
新版零组资料文库离线漏洞名搜索，功能：更新 、查询 （不包含漏洞详情）

当前项目漏洞信息版本20210830

**由于监管零组已于20210901正式停运，“相濡以沫，不如相忘于江湖”**

kali@kali:~$ python3 vs_0sec.py

    零组资料文库离线漏洞名搜索,功能：更新 、查询
        -up:在线更新数据
        -offline:离线更新数据库（根据tree.json文件更新）
        -s [keyword]:查询关键字

# 使用：在线更新数据库
kali@kali:~$ python3 vs_0sec.py -up

    未找到数据库文件vul-0sec.db，将自动创建空库
    tree.json文件下载成功
    开始将json转换到sqlite3数据库
    [Web安全] 转换完成
    [系统安全] 转换完成
    [APP安全] 转换完成
    [IOT安全] 转换完成
    [工控安全] 转换完成
    [云安全] 转换完成
    [域渗透] 转换完成
    [安全技术] 转换完成
    [友情链接] 转换完成
    更新完成

# 使用：查询关键字
kali@kali:~$ python3 vs_0sec.py -s mail

    Web安全|Coremail|Coremail配置文件信息泄漏       https://wiki.0-sec.org/api/wiki/articleInfo/5661
    安全技术|Disable function| mail         https://wiki.0-sec.org/api/wiki/articleInfo/6237

# 使用：离线更新数据库（在线失败）
浏览器访问 https://wiki.0-sec.org/api/wiki/tree 将json数据保存到本地（与脚本同目录下），执行命令更新数据库

kali@kali:~$ python3 vs_0sec.py -offline

    开始将json转换到sqlite3数据库
    [Web安全] 转换完成
    [系统安全] 转换完成
    [APP安全] 转换完成
    [IOT安全] 转换完成
    [工控安全] 转换完成
    [云安全] 转换完成
    [域渗透] 转换完成
    [安全技术] 转换完成
    [友情链接] 转换完成
    更新完成

