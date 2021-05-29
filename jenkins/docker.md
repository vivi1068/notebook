### 下载一个镜像
```shell
docker pull nginx
```

### 查看镜像列表
```shell
docker images
```

### 启动一个容器
```shell
docker run --name tmp-nginx-container -d nginx
```


### 查看容器列表
```shell
docker ps -a
```


### 停止一个容器
```shell
container_id=`docker ps | awk '/tmp-nginx-container/{print $1}'`
docker stop $container_id
```

### 删除一个容器
```shell
container_id=`docker ps | awk '/tmp-nginx-container/{print $1}'`
docker rm $container_id
```

### 删除一个镜像
```shell
image_id=`docker images | awk '/nginx/{print $3}'`
docker rmi $image_id
```