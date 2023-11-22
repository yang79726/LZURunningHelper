# LZURunningHelper

兰大悦跑模拟

本项目改写自 [PKURunningHelper](https://github.com/RinCloud/PKURunningHelper)，所做的工作仅仅是在这个项目的基础之上修改了地图路径数据，直接适配于 LZU

鉴于本校二手群中有人使用类似项目盈利，打着人工代跑的旗号，实际上利用虚拟定位提供路径严重偏差的低劣服务，因此将这个自己用的小工具开源

~~是一个不想跑步不会写代码的卑微大学生低创项目~~

目前本文档仍待完善，暂时没有时间去写具体的食用说明，如果有感兴趣的同学可以自行研究使用~

用户配置位于 `config.ini` 文件内，使用 `start.bat` 一键启动

`config.ini` 文件内 `record_type:` 配置为使用的地图路径，可以设置以下的值：

```
record_type:
- dongcao: 东操
- xicao: 西操
- random (默认): 随机
```
