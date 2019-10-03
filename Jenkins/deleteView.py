import jenkins

server = jenkins.Jenkins('http://localhost:7070', username='admin', password='admin')

server.delete_view('EMPTY')