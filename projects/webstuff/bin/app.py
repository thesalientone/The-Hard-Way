import web
import glob
import os
urls = (


  '/hello', 'Index',
  '/', 'Index',
  '/form_test', 'FormTest',
  '/image', 'Image',
  '/uploads/(.*)', 'Files',
  '/inputstests', 'InputsTests',
  '/inputresults', 'InputsTests'
)

render = web.template.render('templates/', base="layout")

class Index(object):
    def GET(self):
        return render.hello_form()

    def POST(self):
        form = web.input(name="Nobody", greet="Hello")
        greeting = "%s, %s" % (form.greet, form.name)


        return render.index(greeting = greeting)
class FormTest(object):
    def GET(self):
        return render.form_test("nothing")

    def POST(self):
        x = web.input(myfile={})
        # web.debug(x['myfile'].filename)
        # web.debug(x['myfile'].value)
        # web.debug(x['myfile'].file.read())
        filedir ='./uploads/'
        if 'myfile' in x:
            filepath = x.myfile.filename.replace('\\','/')
            filename=filepath.split('/')[-1]
            fout = open(filedir +'/' + filename, 'w')
            fout.write(x.myfile.file.read())
            fout.close()
        raise web.seeother('/image')

class Image(object):
    def GET(self):
        images = glob.glob("./uploads/*.jpg")
        print images
        html_snip = ""
        for image in images:
            html_snip += "<img src=%s alt='no image to show' /><br/>" % image

        return render.image(html_snip)

class Files(object):
    def GET(self, name):
        ext = name.split(".")[-1] # Gather extension

        cType = {
            "jpg": "uploads/jpeg",
            "jpeg": "uploads/jpeg"
        }
        if name in os.listdir('uploads'):
            web.header("Content-Type", cType[ext])
            return open('uploads/%s' % name, "rb").read()
        else:
            raise web.notfound()
class Foo(object):
    def GET(self):
        return render.foo()
class Test(object):
    def GET(self):
        return render.test()

class InputsTests(object):
    def GET(self):
        return render.inputstests()
    def POST(self):
        form = web.input(username ="What", password="Nope")
        userinput = "%s, %s" % (form.username, form.password)
        return render.inputresults(userinput = userinput)




if __name__ == "__main__":

    app = web.application(urls, globals())
    app.run()
