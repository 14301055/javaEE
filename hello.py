#hello.py

def application(environ,start_response):
    p=environ['PATH_INFO'][1:]

    #判断静态还是动态资源
    if ".html" in p:
        BASE_DIR=os.path.dirname(__file__)
        path=os.path.join(BASE_DIR, p)

        if os.path.exists(path):
            f=open(path,'r')
            start_response('200 OK',[('Content-Type','text/html')])
            body=f.read()
            f.close()
            return [body.encode('utf-8')]
        else:
            start_response('404 not found',[('Content-Type','text/html')])
            body='<h1>%s</h1>'%path
            return [body.encode('utf-8')]
    else:
        start_response('200 OK',[('Content-Type','text/html')])
        body='<h1>hello %s!</h1>' % (environ['PATH_INFO'][1:])
        return[body.encode('utf-8')]


            
          
