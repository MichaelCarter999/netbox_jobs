from extras.scripts import Script

class HelloJobs(Script):

    class Meta:
        name = "Hello Jobs"
        description = "Hello World for first Netbox Job"
        
    def run(self, data, commit):
        self.log_info("This is an info type log.")
        self.log_debug("DEBUG: This is a debug type log.")
        self.log_warning("This is a warning type log.")
        self.log_failure("This is an error type log.")
        self.log_failure("This is a critical type log.")
