from time import gmtime, strftime

def log(source, logtype, message):
    strdate = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    logline = "{date:\"" + strdate + "\",source:\"" + source + "\",logtype:\"" + logtype + "\",message:\"" + message + "\"}"
    print(logline)
