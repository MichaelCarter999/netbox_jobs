from extras.scripts import Script
from utilities.forms import StringField

class HelloJobs(Script):

    class Meta:
        name = "Hello Jobs"
        description = "Hello World for first Netbox Job"
        
    def run(self, data, commit):
        self.log_info("Hello, this is my first Netbox Job.")

class HelloLoggingJobs(Script):

    class Meta:
        name = "Hello Logging Jobs"
        description = "Hello World for first Netbox Logging Job"
        
    def run(self, data, commit):
        self.log_info("This is an info type log.")
        self.log_debug("This is a debug type log.")
        self.log_warning("This is a warning type log.")
        self.log_failure("This is a failure type log.")


class HelloJobsWithInputs(Script):

    username = StringField()

    class Meta:
        name = "Hello Jobs with User Inputs"
        description = "Hello Jobs with Different User Inputs"

    def run(self, data, commit):
        username = data["username"]
        self.log_info(f"Hello Jobs with {username}.")

