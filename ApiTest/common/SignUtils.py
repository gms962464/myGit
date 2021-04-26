from jpype import *
import os
from jpype._core import isJVMStarted, startJVM, shutdownJVM
from jpype._jvmfinder import getDefaultJVMPath


def getSignJarPath():
    rootPath = os.path.abspath(os.curdir)
    return rootPath + os.sep + "tools" + os.sep + "citylife-sign.jar"


def getSignString(timstamp,data):
    """
    调用jar包获取签名后的字符串
    :param timstamp:
    :param data:
    :return:
    """
    jvmPath = getDefaultJVMPath()
    if not isJVMStarted():
        signJarPath = getSignJarPath()
        startJVM(jvmPath,"-ea","-Djava.class.path=%s" % (signJarPath))
    signClass = JClass("com.citylife.signature.SignUtils")

    return str(signClass.getSignStr(timstamp,data))

