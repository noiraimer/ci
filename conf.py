# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
#template = {
#    "name": "Maverick-Theme-Galileo",
#    "type": "local",
#    "path": "../Maverick-Theme-Galileo"
#}
template = {
    "name": "Galileo",
    "type": "git",
    "url": "https://github.com/noiraimer/Galileo-custom.git",
    "branch": "latest"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "noiraimer/Blog-With-GitHub-Boilerplate@gh-pages"
}

# 站点设置
site_name = "解语知音"
site_logo = "${static_prefix}logo.png"
site_build_date = "2020/1/31 16:51"
author = "无尽藏海"
email = "liushu1187419589"
author_homepage = "https://noiramr.cn"
description = "温故而知新"
key_words = ['blog']
language = 'zh-CN'
external_links = [
    {
        "name": "友情链接",
        "url": "${site_prefix}friends/",
        "brief": "山水会知音",
        "target": "_self"
    },
    {
        "name": "解语知音",
        "url": "https://noiramr.cn",
        "brief": "温故而知新",
        "target": "_self"
    },
    {
        "name": "解语知识",
        "url": "https://wiki.noiramr.cn",
        "brief": "学而时习之",
        "target": "_blank"
    }

]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "RSS",
        "url": "https://noiramr.cn/feed/index.xml",
        "icon": ""
    },
    {
        "name": "GitHub",
        "url": "https://github.com/noiraimer",
        "icon": ""
    },
        {
        "name": "邮件",
        "url": "mailto:liushu1187419589@live.com",
        "icon": ""
    },
    {
        "name": "语雀",
        "url": "https://www.yuque.com/blancaimer",
        "icon": ""
    },
]

valine = {
    "enable": True,
    "el": '#vcomments',
    "appId": "KgL1pm7KXVOK7PlT4SFO8vYJ-9Nh9j0Va",
    "appKey": "dkFFObbxzdOEUUccBaq0Oxsp",
    "placeholder": "想破脑袋也不知道提示语写啥",
    "comment_count": "true",
    "visitor":  "true"
}

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
<link rel="dns-prefetch" href="//noiramr.cn" />
<link rel="shortcut icon" href="${static_prefix}favicon.ico?v=yyLyaqbyRG">
'''

footer_addon = r'''

'''

body_addon = r'''
<script src="https://cdn.jsdelivr.net/gh/noiraimer/Blog-With-GitHub-Boilerplate@gh-pages/js/instant.js" type="module" defer integrity="sha384-OeDn4XE77tdHo8pGtE1apMPmAipjoxUQ++eeJa6EtJCfHlvijigWiJpD7VDPWXV1"></script>
<script src="https://cdn.jsdelivr.net/gh/noiraimer/Blog-With-GitHub-Boilerplate@gh-pages/js/email-decode.min.js"></script>
'''
main_addon = r'''

'''
