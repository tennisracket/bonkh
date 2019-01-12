from bonkh.app import *
import os

form = os.path.dirname(os.path.abspath(__file__))+"\\templates\\forms\\form.pt"

if __name__ == '__main__':
    settings = dict(reload_templates=True)
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_view(form_view, renderer=os.path.join(here, form))
    config.add_static_view('static', 'deform:static')
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
