from extras.scripts import Script, StringVar

class HelloJobsWithInputs(Script):

    username = StringVar(
        label="Username"
    )

    class Meta:
        name = "Hello Jobs with User Inputs"
        description = "Hello Jobs with Different User Inputs"

    def run(self, data, commit):
        username = data["username"]
        self.log_info(f"Hello Jobs with {username}.")
