import jenkins

server = jenkins.Jenkins('http://localhost:7070', username='admin', password='admin')
user = server.get_whoami()
version = server.get_version()

# Create new jenkins job , name of job : batman!!
server.create_job('batman', jenkins.EMPTY_CONFIG_XML)
jobs = server.get_jobs()
print (jobs)

# Get config.xml of created jenkins job, name of job : batman
batman_job = server.get_job_config('batman')
print(batman_job) # prints XML configuration

# Build jenkins job , name of job : batman
server.build_job('batman')

# Copy job from existing job , source : batman ,target : joker
server.copy_job('batman', 'joker')

# Enable new copied job, name of job : joker
server.enable_job('joker')

# Get config.xml of created jenkins job, name of job : joker
joker_job = server.get_job_config('joker')
print(joker_job) # prints XML configuration

# Re-configure new copied job , name of job : joker
server.reconfig_job('joker', jenkins.RECONFIG_XML)
