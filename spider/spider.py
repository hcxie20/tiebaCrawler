# coding:utf-8
import urllib.request
import re
import os
import timeit

class tiebaCrawler(object):
    def __init__(self):
        if not os.path.exists("./download"):
            os.makedirs("./download")
        pass

    @staticmethod
    def get_url(url):
        print("Getting url...")
        headers = {
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
            }
        request = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(request)
        return response

    def download_imgs(self, url):
        page = self.get_url(url).read().decode("utf-8")
        pattern2 = "(<title>)(.*)(</title>)"
        title = re.search(pattern2, page).groups()[1]
        print(title)
        pattern = '(<img class="BDE_Image".*?)(src=")(.+?jpg)'
        imgs = re.findall(pattern, page)
        
        folder = "./download/" + title
        if not os.path.exists(folder):
            os.mkdir(folder)

        num = len(imgs)
        for i in range(len(imgs)):
            print("Downloading img {0}/{1}".format(i + 1, num))
            img_name = folder + "/" + "{0:0>2d}.jpg".format(i+1)
            if not os.path.exists(img_name):
                img = urllib.request.urlopen(imgs[i][2]).read()
                with open(img_name, "wb") as f:
                    f.write(img)
            else:
                print("File exists")
        pass


if __name__ == "__main__":
    # url = input("URL: ")  # 目标网页URL\
    url = "https://tieba.baidu.com/p/6402970484?"
    a = tiebaCrawler()
    a.download_imgs(url)
