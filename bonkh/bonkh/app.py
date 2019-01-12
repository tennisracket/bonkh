
import os

from wsgiref.simple_server import make_server
from pyramid.config import Configurator

from colander import (
    Boolean,
    Integer,
    Length,
    MappingSchema,
    OneOf,
    SchemaNode,
    SequenceSchema,
    String
)

from deform import (
    Form,
    ValidationFailure,
    widget
)


here = os.path.dirname(os.path.abspath(__file__))

class UserSchema(MappingSchema):
    name = SchemaNode(String(),
                      description = 'Be comfortable here')
    surname = SchemaNode(String(),
                      description = 'Be comfortable here')
    email = SchemaNode(String(),
                      description = 'Be comfortable here')


def form_view(request):
    schema = UserSchema()
    myform = Form(schema, buttons=('submit',))
    template_values = {}
    template_values.update(myform.get_widget_resources())

    if 'submit' in request.POST:
        controls = request.POST.items()
        try:
            myform.validate(controls)
        except ValidationFailure as e:
            template_values['form'] = e.render()
        else:
            template_values['form'] = 'OK'
        return template_values

    template_values['form'] = myform.render()
    return template_values
