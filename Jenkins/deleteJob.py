import jenkins

server = jenkins.Jenkins('http://localhost:7070', username='admin', password='admin')
user = server.get_whoami()
version = server.get_version()

# Delete jobs
server.delete_job('batman')
server.delete_job('joker')