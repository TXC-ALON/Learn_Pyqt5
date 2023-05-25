# PyQt-Fluent-Widgets跟学



# 0 配置环境



## 使用Anaconda配置环境

参考https://blog.csdn.net/Smalldemons/article/details/127703521

### 基础的pyqt5环境配置

#### 安装包

```python
pip install pyqt5
pip install pyqt5-tools
```

#### 配置环境变量

系统变量下新增

```shell
QT_QPA_PLATFORM_PLUGIN_PATH
C:\Users\Admin\anaconda3\envs\PyQt5\Lib\site-packages\qt5_applications\Qt\plugins\platforms
```

```shell
QT_PLUGIN_PATH
C:\Users\Admin\anaconda3\envs\PyQt5\Lib\site-packages\pyqt5_plugins
```

path下新增

```shell
C:\Users\Admin\anaconda3\envs\PyQt5\Lib\site-packages\pyqt5_tools
```

#### pycharm外部工具

QTDesigner

```python
C:\Users\Admin\anaconda3\envs\PyQt5\Lib\site-packages\qt5_applications\Qt\bin\designer.exe
无实参
$FileDir$
```

Ui2Py

```python
C:\Users\Admin\anaconda3\envs\Pyqt5\python.exe
-m PyQt5.uic.pyuic $FileName$ -o $FileNameWithoutExtension$.py
$FileDir$
```



### 配置PyQt-Fluent-Widgets

这里注意要用[zhiyiYo](https://github.com/zhiyiYo)/**[PyQt-Fluent-Widgets](https://github.com/zhiyiYo/PyQt-Fluent-Widgets)*自己提供的.我一开始用的清华源,结果下载出来的是老的版本.导致router没有,打不开demo.py.

> (PyQt5) C:\Users\Admin>pip install "PyQt-Fluent-Widgets[full]" -i https://pypi.org/simple/
> Looking in indexes: https://pypi.org/simple/
> Requirement already satisfied: PyQt-Fluent-Widgets[full] in c:\users\admin\anaconda3\envs\pyqt5\lib\site-packages (0.8.7)
>
> (PyQt5) C:\Users\Admin>pip install "PyQt-Fluent-Widgets[full]" -i https://pypi.org/simple/
> Looking in indexes: https://pypi.org/simple/
> Collecting PyQt-Fluent-Widgets[full]
>   Downloading PyQt_Fluent_Widgets-0.9.1-py3-none-any.whl (1.4 MB)
>      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.4/1.4 MB 789.9 kB/s eta 0:00:00

```python
pip install "PyQt-Fluent-Widgets[full]" -i https://pypi.org/simple/
```

运行examples/galley/demo.py

![image-20230526012756986](E:\00Learning\PyQt\Learn_Pyqt5\Follow\PyQt-Fluent-Widgets\PyQt-Fluent-Widgets跟学.assets\image-20230526012756986.png)

