# Flask应用通过163邮箱发送邮件演示
[视频链接 | Bilibili](https://www.bilibili.com/video/BV1Ud4y1Q7Me/?share_source=copy_web&vd_source=0aaf8e48f5ea3349e83a6332833325be)

通过 163 邮箱提供的第三方邮件 POP3 / SMTP / IMAP 服务创建自己的本地客户端并通过 Python 在 Flask 网页中发送

## Template 
Template 文件夹中包含网页服务器所需要的html文件。在本样例中，main.html 为发送主页；success.html 为发送成功并显示此template了；如果失败则显示 error.html 的template并载入错误Exception信息。
