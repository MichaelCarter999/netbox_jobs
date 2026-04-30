from extras.scripts import Script

class Test(Script):
    class Meta:
        name = "Script Test"

    def run(self, data, commit):
        self.log_info("Hello")
