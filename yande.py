import os#引入文件模块
import re#正则表达式
import urllib.request

#连接网页并返回源码
def open_url(url):
      try:
            req = urllib.request.Request(url)
            req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36")
            response = urllib.request.urlopen(req)
            status_code = response.code
            html = response.read()
            return html
      except:
            print(url + " 404")
            return 404

def mkdir(path):
    '''
    :param path: 路径
    :return:
    '''
    # 引入模块
    import os

    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')
        return False


def Yande1():
    pages1 = int(input('请输入你要下载的起始页面数：'))
    pages2 = int(input('请输入你要下载的末尾页面数：'))
    mkdir('img')
    for i in range(pages1,pages2+1):
        imgs = 1
        print(i)
        url = 'https://yande.re/post?page='+str(i)
        #print(url)
        floder = "E:\Python\爬虫\yande\img\page"+str(i)
        mkdir(floder)
        os.chdir(floder)

        html = open_url(url)
        html = html.decode('gbk', 'ignore')
        #print(html)
        img_adds = []
        img_adds = re.findall(r'<a class="directlink largeimg" href="([^"]+\.jpg)"', html)
        for i in img_adds:
            filename = str(imgs)+'.jpg'
            imgs += 1
            img_html = open_url(i)
            if img_html == 404:
                continue
            with open(filename, 'wb') as f:
                f.write(img_html)
                print(i+'下载完成....')
        #print(len(img_adds))


if __name__ == '__main__':
    Yande1()