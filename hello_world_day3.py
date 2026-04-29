from extras.scripts import Script

class HelloJobs(Script):

    def run(self):
        self.log_info("Hello, this is my first Nautobot Job.")
