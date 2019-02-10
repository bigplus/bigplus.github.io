# 数据库事务
1. 事务是什么？四要素
2. 事务的并发，如果不加以控制，会出现脏读，不可重复读，幻读, 丢失更新
3. 通过4个级别，来依次解决这些问题。 (四个级别：读未提交 ur，读提交cs，可重复读rs，序列化rr（缩写来自db2）)
	4个隔离级别是3个问题的解决方案。
4. 4个级别的实现方式，有3种：a. 锁，b. mvcc，c. snapshot。
	ps : 用锁的机制加以控制：读锁，写锁. https://comedsh.iteye.com/blog/698733
	解决方案，依据：时间(读取到数据时的瞬间，还是事务发生到结束)，锁类型(共享锁，排他锁)，锁粒度(行，表). 
#### from :
	https://www.hollischuang.com/archives/943, 
	https://my.oschina.net/HuQingmiao/blog/518101
	问题与锁实现
	https://comedsh.iteye.com/blog/698733

# 事务的概念
ACID
事务保证了一个操作序列可以全部都执行或者全部都不执行（原子性）

# [参考]
事务隔离级别
https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/tr-95-51.pdf
隔离级别与锁
https://zhuanlan.zhihu.com/p/34742600
https://zhuanlan.zhihu.com/p/35195449

db2
https://blog.csdn.net/yxh0823/article/details/5858574
https://baijiahao.baidu.com/s?id=1611918898724887602&wfr=spider&for=pc
https://baijiahao.baidu.com/s?id=1611918898724887602&wfr=spider&for=pc
https://zhuanlan.zhihu.com/p/37447670
https://www.cnblogs.com/fjdingsd/p/5273008.html
https://www.cnblogs.com/protected/p/6526857.html

https://www.cnblogs.com/huanongying/p/7021555.html

https://www.cnblogs.com/phpper/p/6937650.html
http://www.nosqlnotes.com/technotes/mvcc-snapshot-isolation/
https://blog.csdn.net/xgbjmxn/article/details/6200740

