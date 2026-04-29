from extras.scripts import Script

class HelloJobs(Script):

    def run(self):
        self.log_debug("Hello, this is my first Nautobot Job.")
