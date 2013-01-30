import pyramid_jinja2
from ipaddress import ip_address
from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from .models import DBSession, Base
from .resources import RootFactory
from .formatters import format_text


def remote_addr(request):
    """Similar to built-in ``request.remote_addr`` but will fallback to
    ``HTTP_X_FORWARDED_FOR`` if defined and ``REMOTE_ADDR`` is private or
    loopback address.
    """
    ipaddr = ip_address(request.environ.get('REMOTE_ADDR', '255.255.255.255'))
    if ipaddr.is_private or ipaddr.is_loopback:
        return request.environ.get('HTTP_X_FORWARDED_FOR', str(ipaddr))
    return str(ipaddr)


def main(global_config, **settings):  # pragma: no cover
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings, root_factory=RootFactory)
    config.set_request_property(remote_addr)
    config.include(pyramid_jinja2)

    jinja2_env = config.get_jinja2_environment()
    jinja2_env.filters['format_text'] = format_text

    config.add_static_view('static', path='static', cache_max_age=3600)
    config.add_view('.views.root_view',
                    context='.resources.RootFactory',
                    renderer='root.jinja2')
    config.add_view('.views.board_view',
                    context='.interfaces.IBoardResource',
                    renderer='boards/show.jinja2')
    config.add_view('.views.new_board_view',
                    context='.interfaces.IBoardResource',
                    renderer='boards/new.jinja2',
                    name='new')
    config.add_view('.views.topic_view',
                    context='.interfaces.ITopicResource',
                    renderer='topics/show.jinja2')

    config.scan()
    return config.make_wsgi_app()
