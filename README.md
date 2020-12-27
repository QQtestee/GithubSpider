# GithubSpider
----
* Fetch the `spider.py`.
* In the code, config the essential constants at the head: Github Username、password、CSV file path、CHROME Driver path.
* Run `python spider.py`
* View the log in the terminal, that it should be something like this if everthing works out fine:
```
(base) mbp:githubgrabber main$ python spider.py
--开始爬虫操作--
--开始尝试登录--
++登录操作完成++
--开始尝试获取所需信息--
--开始写入test.csv文件的操作--
++已完成写入test.csv文件的操作++
++已完成获取所需信息的操作++
--开始对各个repo进行watch的操作--
--开始对PaddlePaddle / PaddleHub进行watch的操作--
++完成对PaddlePaddle / PaddleHub进行watch的操作++
--开始对Hari-Nagarajan / fairgame进行watch的操作--
++完成对Hari-Nagarajan / fairgame进行watch的操作++
--开始对geohot / tinygrad进行watch的操作--
++完成对geohot / tinygrad进行watch的操作++
--开始对public-apis / public-apis进行watch的操作--
++完成对public-apis / public-apis进行watch的操作++
--开始对vinta / awesome-python进行watch的操作--
++完成对vinta / awesome-python进行watch的操作++
--开始对sherlock-project / sherlock进行watch的操作--
++完成对sherlock-project / sherlock进行watch的操作++
--开始对swisskyrepo / PayloadsAllTheThings进行watch的操作--
++完成对swisskyrepo / PayloadsAllTheThings进行watch的操作++
--开始对geekcomputers / Python进行watch的操作--
++完成对geekcomputers / Python进行watch的操作++
--开始对microsoft / playwright-python进行watch的操作--
++完成对microsoft / playwright-python进行watch的操作++
--开始对ultralytics / yolov5进行watch的操作--
++完成对ultralytics / yolov5进行watch的操作++
++已完成对各个repo进行watch的操作++
++完成爬虫操作++
请输入字母q来退出:q
(base) mbp:githubgrabber main$ 
```
* The .csv file is expected to be as the `test.csv` provided.

---
Contact me at: mrylon@163.com
