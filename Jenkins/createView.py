import jenkins

server = jenkins.Jenkins('http://localhost:7070', username='admin', password='admin')
server.create_view('EMPTY', jenkins.EMPTY_VIEW_CONFIG_XML)
view_config = server.get_view_config('EMPTY')
views = server.get_views()
print (views)