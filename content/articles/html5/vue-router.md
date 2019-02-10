Title: 前端开发之-vue-router
Status: draft
[TOC]
## vue-router

一般通过 vue-cli 创建的相关选择 vue-router 之后是不需要额外的安装配置了，下面就一些基本的路由分发过程讨论之。直接上代码吧：



```js
import Vue from 'vue';
import Router from 'vue-router';
import HomePage from '@/components/HomePage';
import AboutPage from '@/components/AboutPage';
import NotFoundPage from '@/components/NotFoundPage';
import Main from '@/components/main/Main';
import DrawMolecule from '@/components/main/DrawMolecule';

Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'HomePage',
      component: HomePage,
      children: [
        {
          path: '',
          component: Main,
        },
        {
          path: 'draw',
          component: DrawMolecule,
        },
      ],
    },
    {
      path: '/about',
      name: 'AboutPage',
      component: AboutPage,
    },
    {
      path: '*',
      component: NotFoundPage,
    },
  ],
});

```

```js
import Vue from 'vue';
import Router from 'vue-router';
import HomePage from '@/components/HomePage';
import AboutPage from '@/components/AboutPage';
import NotFoundPage from '@/components/NotFoundPage';
import Main from '@/components/main/Main';
import DrawMolecule from '@/components/main/DrawMolecule';
```

这个引入一些对象，其中 `@` 是指 src 文件夹，就是一个别名罢了。

```
  mode: 'history',
```

默认的路由是带个 `#` ，这个一般人们是不太喜爱的，我们也可以让url成为常见的那种，也就是如上开启 history 模式。

开启了之后一般点没问题，但如果刷新的会报 404 错误，也就是后端需要额外做些配置，下面以nginx为例子说明之，参看了 [这篇文章](https://www.jianshu.com/p/0a9077d8714d) ，简单来说就是nginx要加上这样一行：

```
  try_files $uri $uri/ @rewrites;

  location @rewrites{
    rewrite ^(.+)$ /index.html last;
  }
```

因为默认的location就是 `/` ，这里就直接放外面了，`try_files`  这里的逻辑是先根据uri来查找文件夹，或者目录，都找不到再@rewrites那边，简单来说就是一切都重定向到index.html哪里。

这个我喜欢简单点的解决方案，我看到 vue-router官方文档的解决方案就是：

```
try_files $uri $uri/ /index.html;
```

所以推荐就加上一行就OK了。



```js
routes: [
    {
      path: '/',
      name: 'HomePage',
      component: HomePage,
      children: [
        {
          path: '',
          component: Main,
        },
        {
          path: 'draw',
          component: DrawMolecule,
        },
      ],
    },
    {
      path: '/about',
      name: 'AboutPage',
      component: AboutPage,
    },
    {
      path: '*',
      component: NotFoundPage,
    },
  ],
```

这段代码就是在做路由分发到目标组件的工作，有两个重要点要说一下：

1. `path: '*'` 这种表达通常写在最后面，拦截所有未知的路由到404组件，或者说404页面吧。

2. APP.vue 组件哪里放着 `<router-view></router-view>` ，想 `/what` 的一级分发最后会在这里渲染。而我们在看到 Main 组件，其属于HomePage组件的子组件，当 `path= ''` 的时候，这个时候会默认渲染Main组件，然后 `/draw` 会把 DrawMolecule 组件渲染到 HomePage组件上，或者说渲染到 HomePage组件的 router-view哪里。然后注意二级组件的path前面是不带 `/` 符号的。

   下面让我再多说几句，把这一块再澄清一下：

   APP 组件 里面有个 router-view ，其如果遇到 `/` 首先会把 HomePage 组件渲染上去，（ 如果遇到 `/about` 会把 AboutPage 组件渲染上去），如果遇到 `/` ，把HomePage组件渲染上去之后，发现HomePage组件上还有个 router-view，然后再找HomePage组件的child 组件，因为是 `/` ，那么就把默认的 Main组件渲染上去，如果是 `/draw` ，那么把 DrawMolecule 子组件渲染上去。