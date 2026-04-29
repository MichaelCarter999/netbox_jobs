from extras.scripts import Script
from utilities.forms import StringField

class HelloJobsWithInputs(Script):

    username = StringField(
        label="Username"
    )

    class Meta:
        name = "Hello Jobs with User Inputs"
        description = "Hello Jobs with Different User Inputs"

    def run(self, data, commit):
        username = data["username"]
        self.log_info(f"Hello Jobs with {username}.")
