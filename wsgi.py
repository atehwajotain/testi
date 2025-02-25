
def application(env, start_response):
    start_response('200 OK', [('Content-type', 'text/plain; charset=utf-8')])
    yield "Hello w€rld😞!".encode('utf-8')

