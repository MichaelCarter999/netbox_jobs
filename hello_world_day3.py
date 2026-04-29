from extras.scripts import Script

class HelloJobs(Script):

    class Meta:
        name = "Hello Jobs"
        description = "Hello World for first Netbox Job"
        
    def run(self, data, commit):
        self.log_info("Hello, this is my first Netbox Job.")
