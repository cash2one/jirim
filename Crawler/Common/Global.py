import sys

# Path
HomePath    = None
SystemPath  = None
LogFilePath = None
XmlFilePath = None
INIFilePath = None

# File
XmlFileName = None

# Data
RankListCount = None
RelationCount = None
RelationDepth = None

# Option
ServerIP    = None
CycleTime   = None

class Global(object):
    
    # Home
    @staticmethod
    def GetHomePath():
        global HomePath
        return HomePath

    @staticmethod
    def SetHomePath(strH):
        global HomePath
        HomePath = strH
    
    # System
    @staticmethod
    def GetSystemPath():
        global SystemPath
        return SystemPath

    @staticmethod
    def SetSystemPath(strS):
        global SystemPath
        SystemPath = strS
    
    # Log - path    
    @staticmethod
    def GetLogFilePath():
        global LogFilePath
        return LogFilePath

    @staticmethod
    def SetLogFilePath(strL):
        global LogFilePath
        LogFilePath = strL

    # Xml - path
    @staticmethod
    def GetXmlFilePath():
        global XmlFilePath
        return XmlFilePath

    @staticmethod
    def SetXmlFilePath(strX):
        global XmlFilePath
        XmlFilePath = strX

    # INI - path
    @staticmethod
    def GetINIFilePath():
        global INIFilePath
        return INIFilePath

    @staticmethod
    def SetINIFilePath(strI):
        global INIFilePath
        INIFilePath = strI
    
    # Xml - name    
    @staticmethod
    def GetXmlFileName():
        global XmlFileName
        return XmlFileName

    @staticmethod
    def SetXmlFileName(strX):
        global XmlFileName
        XmlFileName = strX
    
    # Rank - count
    @staticmethod
    def GetRankListCount():
        global RankListCount
        return RankListCount

    @staticmethod
    def SetRankListCount(strR):
        global RankListCount
        RankListCount = strR

    # Relation - count
    @staticmethod
    def GetRelationCount():
        global RelationCount
        return RelationCount

    @staticmethod
    def SetRelationCount(strR):
        global RelationCount
        RelationCount = strR

    # Relation - depth
    @staticmethod
    def GetRelationDepth():
        global RelationDepth
        return RelationDepth

    @staticmethod
    def SetRelationDepth(strR):
        global RelationDepth
        RelationDepth = strR

    @staticmethod
    def SetServerIP(strI):
        global ServerIP
        ServerIP = strI

    @staticmethod
    def GetServerIP():
        global ServerIP
        return ServerIP

    @staticmethod
    def SetCycleTime(strC):
        global CycleTime
        CycleTime = strC

    @staticmethod
    def GetCycleTime():
        global CycleTime
        return CycleTime

    #################### Func #################### 
    def progressbar(it, prefix = "", size = 60):
        count = len(it)
        def _show(_i):
            x = int(size*_i/count)
            sys.stdout.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), _i, count))
            sys.stdout.flush()
        
        _show(0)
    
        for i, item in enumerate(it):
            yield item
            _show(i+1)
        sys.stdout.write("\n")
        sys.stdout.flush()