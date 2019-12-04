# python-LSTM-Beijing-Air-Quality
test file and python


Background
=====

这个是我在实习期间完成的项目，也就是北京空气质量AQI（Air Quality）预测，业务场景更多是针对pm2.5，所以我不能放上关于pm2.5的数据作分享。

但是爬取的AQI数据，我认为SO2指标是值得分享的。但示例代码中没有过多调参。目的是希望学习的朋友能尝试一下。

这份代码 最初灵感来自于 一份飞机乘客的 LSTM预测代码。作者在那部分展示了带有周期规律的时间序列数据，如何操作及预测。

然而可惜的是，时至今日，我已找不到那个原作者，毕竟是17年底我做的这个项目。但仍需要向他致敬。



直接修改代码中的.csv文件名，写绝对路径也可以，注意需要将csv还代码放在同一个文件夹中。另外  history_loss.txt也需要放在同一文件夹中。
然后运行代码  pychar 也好  直接用命令行也可以

> f
libraries
=====
 
pandas，numpy，matplotlib，math，keras，sklearn

如果你知道如何安装，请打开你的cmd（或其它命令行）

for example

>pip install pandas

Run codes
=====

你只需要运行keras_testpages.py 即可

如果你需要替换文件，请注意你的格式
