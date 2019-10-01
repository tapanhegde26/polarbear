import jenkins

server = jenkins.Jenkins('http://localhost:7070', username='admin', password='admin')
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))