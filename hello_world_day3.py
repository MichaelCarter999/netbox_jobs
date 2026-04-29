from extras.scripts import Script

class HelloJobs(Script):

    def run(self):
        self.logger.debug("Hello, this is my first Nautobot Job.")
