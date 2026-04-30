from extras.scripts import Script, StringVar, IntegerVar

class HelloVariables(Script):

    message = StringVar(
        description="Message to display"
    )

    days = IntegerVar(
        description="Number of days",
        default=10
    )

    class Meta:
        name = "Hello Variables"
        description = "Scripts Variable Examples"

    def run(self, data, commit):
        message = data["message"]
        days = data["days"]
        
        self.log_info(f"Please give the message: {message} in {days} days.")
