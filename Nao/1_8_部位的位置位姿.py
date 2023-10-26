# -*- coding: UTF-8 -*-
from naoqi import ALProxy
import motion
import almath
import qi

# 创建与NAO机器人的会话

# # IP
# robotIP = "192.168.8.207"
# # 端口
# port = 9559

robotIP = "127.0.0.1"
port = 49917
# 连接到 NAO 机器人
# nao_ip = "127.0.0.1"  # 替换为你的 NAO 机器人的 IP 地址
# nao_port = 49917
session = qi.Session()
session.connect("tcp://" + robotIP + ":" + str(port))

# 初始化代理
motionProxy  = ALProxy("ALMotion", robotIP, port)
postureProxy = ALProxy("ALRobotPosture", robotIP, port)
ttsProxy     = ALProxy("ALTextToSpeech", robotIP, port)
audioProxy   = ALProxy("ALAudioPlayer", robotIP, port)
isAbsolute   = True # isAbsolute变量用于函数需要布尔参数的任何位置


# 获取头部摄像头的当前位置
cameraAngle = motionProxy.getAngles("HeadPitch", True)  # True 表示使用弧度

# 打印摄像头角度
print("print:")

print("Camera Angle:", cameraAngle)

# 获取所有关节名称
jointNames = motionProxy.getJointNames("Body")
print(jointNames)