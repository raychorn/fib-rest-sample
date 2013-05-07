"""
As part of your screening, please provide a sample project for review:
1. The project should provide a RESTful web service.
  a. The web service accepts a number, n, as input and returns the first n Fibonacci numbers, starting from 0. I.e. given n = 5, appropriate output would represent the sequence "0 1 1 2 3".
  b. Given a negative number, it will respond with an appropriate error.
  c. The service should return the values in an XML document.  Create an XSD that can be used to validate the output.

<fibonacci>
            <value index="0">0</value>
            <value index="1">1</value>
            <value index="2">1</value>
            <value index="3">2</value>
</fibonacci>

2. Set this project up on Github.  Include whatever instructions are necessary to build and deploy/run the project, where "deploy/run" means the web service is accepting requests and responding to them as appropriate.
3. While this project is admittedly trivial, approach it as representing a more complex problem that you'll have to put into production and maintain for 5 years.
"""
import web

urls = (
    '/', 'Index',
    '/(\d+)', 'View',
    '/XML/(\d+)', 'ViewXML',
)

### Templates
render = web.template.render('templates', base='base')

web.template.Template.globals.update(dict(
    datestr = web.datestr,
    render = render
))

def notfound():
    return web.notfound("Sorry, the page you were looking for was not found.  This message may be seen whenever someone tries to issue a negative number as part of the REST URL Signature and this is just not allowed at this time.")

class Index:

    def GET(self):
        """ Show page """
        return render.index()

class View:

    def GET(self, num):
        from utils import get_fibonacci_nums
        items = get_fibonacci_nums(num)
        return render.view(items)

class ViewXML:

    def __render__(self, values):
        __items__ = ['<fibonacci>']
        count = 0
        for v in values:
            __items__.append('<value index="%s">%s</value>' % (count,v))
            count += 1
        __items__.append('</fibonacci>')
        return ''.join(__items__)
    
    def GET(self, num):
        from utils import get_fibonacci_nums
        items = get_fibonacci_nums(num)
        web.header('Content-Type', 'application/xml')
        return self.__render__(items)

app = web.application(urls, globals())
app.notfound = notfound

if __name__ == '__main__':
    app.run()
  
