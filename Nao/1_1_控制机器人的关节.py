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

tts = ALProxy("ALTextToSpeech", robotIP , port)
tts.say("1_1_控制机器人的关节")
# motion = ALProxy("ALMotion", robotIP , port)
# tts    = ALProxy("ALTextToSpeech", robotIP , port)
# motion.setStiffnesses("Body", 1.0)
# motion.moveInit()
# motion.post.moveTo(0.5, 0, 0)
# tts.say("I'm walking")

# postureProxy = ALProxy("ALRobotPosture", robotIP, port)
# #设置NAO的初始姿势
# postureProxy.goToPosture("StandInit", 0.5)

# 初始化代理
motion_proxy = ALProxy("ALMotion", robotIP, port)
# 设置关节名称和目标角度
joint_names = ["LShoulderPitch"]  # 你要控制的具体关节名称
target_angles = [4.0]  # 你要设定的目标角度 提供了每个关节的角度
# 执行关节角度控制
motion_proxy.setAngles(joint_names, target_angles, 0.1) # 最后一个参数是控制速度，可按需调整


# postureProxy = ALProxy("ALRobotPosture", robotIP, port)
# #设置NAO的初始姿势
# postureProxy.goToPosture("StandInit", 0.5)




# All motors 所有电机（关节）
# 头部关节：
# HeadYaw（头部水平转动）
# HeadPitch（头部俯仰转动）
# 左臂关节：
# LShoulderPitch（左肩俯仰转动）
# LShoulderRoll（左肩水平转动）
# LElbowYaw（左肘关节水平转动）
# LElbowRoll（左肘关节俯仰转动）
# LWristYaw（左手腕水平转动）
# 右臂关节：
# RShoulderPitch（右肩俯仰转动）
# RShoulderRoll（右肩水平转动）
# RElbowYaw（右肘关节水平转动）
# RElbowRoll（右肘关节俯仰转动）
# RWristYaw（右手腕水平转动）

# 头部关节：

# HeadYaw（头部水平转动）
# HeadPitch（头部俯仰转动）
# 左臂关节：

# LShoulderPitch（左肩俯仰转动）
# LShoulderRoll（左肩水平转动）
# LElbowYaw（左肘关节水平转动）
# LElbowRoll（左肘关节俯仰转动）
# LWristYaw（左手腕水平转动）
# LHand（左手掌）
# LFinger（左手指）
# 右臂关节：

# RShoulderPitch（右肩俯仰转动）
# RShoulderRoll（右肩水平转动）
# RElbowYaw（右肘关节水平转动）
# RElbowRoll（右肘关节俯仰转动）
# RWristYaw（右手腕水平转动）
# RHand（右手掌）
# RFinger（右手指）
# 腿部关节：

# LHipYawPitch（左髋部水平俯仰转动）
# LHipRoll（左髋部水平转动）
# LHipPitch（左髋部俯仰转动）
# LKneePitch（左膝关节俯仰转动）
# LAnklePitch（左踝关节俯仰转动）
# LAnkleRoll（左踝关节摆动）
# RHipYawPitch（右髋部水平俯仰转动）
# RHipRoll（右髋部水平转动）
# RHipPitch（右髋部俯仰转动）
# RKneePitch（右膝关节俯仰转动）
# RAnklePitch（右踝关节俯仰转动）
# RAnkleRoll（右踝关节摆动）






