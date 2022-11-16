# books

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).


#  VUE3.0: 从后端读取数据，展示页面

## axios : 让vue从后端读取数据

## 我踩过的一些坑

> 问题1：只有主页home可以显示，路由到其他页面浏览器控制台报错 Uncaught SyntaxError: Unexpected token ‘＜‘ (at chunk-vendors.js:1:1) app.j
> 这是因为在build时候把vue.config.js中 module.exports = { publicPath: "/", ... } 的 publicPath改成了 "./" ，这个改动主要是为了在生产环境build时候解决路径问题，注意这里如果在开发环境下 "npm run serve" 的时候需要再改回来。

> 问题2：本地navicat访问不到服务器mysql的3306端口，非常难搞。
> 这是因为mysql初始生成的root虽然是最高权限但是为了安全考虑，只有内网访问权限。

可以进入服务器mysql后使用下面代码把mysql表里的root记录修改一下，开放全域访问权限。

```
mysql -u root -p <your mysql password>
mysql> use mysql; 
mysql> update user set host = '%' where user = 'root'; 
mysql> select host, user from user; 
mysql> flush privileges;
```

> 问题3 宝塔的pm2运行flask后端脚本的时候，无法正常加入虚拟环境导致找不到flask，pymysql之类的包，而这些包都是安装在某个虚拟环境里的。
> 那就直接ssh连接一下，在命令行里让pm2运行脚本即可。

``` 
可以通过pm2 start <program name>来启动某个js脚本或python程序，之后就能看到这个进程的监听状态；
可以通过pm2 log来查看正在运行的进程所有log；
```

> 问题4 宝塔的nginx因为80端口冲突无法启动，用netstat查看占用端口之后发现是被系统进程system占用
> 我总不能kill系统进程吧，查看占用80端口的详细信息后发现是Alibaba Apache Cloud服务占用，那就是阿里云初始化时候配套自带的Apache服务了，那就没办法，直接卸载nginx...

> 问题5 如何部署到服务器上？
> 首先记得把本地开发(development)模式换成生产(production)模式，再用npm run build(或者vue ui面板的build)把文件打包生成，把打包生成好的文件连同.htaccess文件打包到线上web服务器(apache/nginx/...)设置的目录下，这就部署好了前端部分