from nose.tools import *
from bin.app import app
from tests.tools import assert_response

def test_index():
    #check that we get a 404 on the / url
    resp = app.request("/")
    assert_response(resp, status="404")

def test_hello():
    #test our first GEET request to /hello
    resp = app.request("/hello")
    assert_response(resp)
def test_form():
    #make sure default values work for the form
    resp = app.request("/hello", method="POST")
    assert_response(resp, contains="Nobody")
def test_data():
    #test that we get expected values
    data = {'name': 'Zed', 'greet': 'Hola'}
    resp = app.request("/hello", method="POST", data=data)
    assert_response(resp, contains="Zed")
