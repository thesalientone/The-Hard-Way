import web

urls = (
  '/', 'Index',
  '/index.html', 'Index',
  '/foo.html', 'Foo',
  '/test.html', 'Test',
  '/hello', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class Index(object):
    def GET(self):
        return render.hello_form()

    def POST(self):
        form = web.input(name="Nobody", greet="Hello")
        greeting = "%s, %s" % (form.greet, form.name)


        return render.index(greeting = greeting)

class Foo(object):
    def GET(self):
        return render.foo()
class Test(object):
    def GET(self):
        return render.test()

if __name__ == "__main__":
    app.run()
