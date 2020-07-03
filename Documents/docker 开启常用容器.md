# docker 开启常用容器

## mysql

```
docker run --name=mysql -it -v /home/kain/Docker/mysql/data:/var/lib/mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123456 -d mysql
```

https://blog.csdn.net/wlmvp/article/details/85772396

## redis

```
docker run --name=redis -p 6379:6379 -v /home/kain/Docker/redis/data:/data  -d redis redis-server --appendonly yes
```

连接redis的几种方式：

```
docker exec -ti d0b86 redis-cli

docker exec -ti d0b86 redis-cli -h localhost -p 6379 
docker exec -ti d0b86 redis-cli -h 127.0.0.1 -p 6379 
docker exec -ti d0b86 redis-cli -h 172.17.0.3 -p 6379 
// 注意，这个是容器运行的ip，可通过 docker inspect redis_s | grep IPAddress 查看
```

https://www.cnblogs.com/zhzhlong/p/9465670.html