from extras.scripts import Script, StringVar, IntegerVar, MultiSelectVar

class HelloVariables(Script):

    message = StringVar(
        description="Message to display"
    )

    days = IntegerVar(
        description="Number of days",
        default=10
    )


    CHOICES = (
        ('h', 'Happy'),
        ('s', 'Sad'),
        ('e', 'Excited'),
    )    
    
    feelings = MultiSelectVar(
        choices=CHOICES,
        description="How are you feeling?"
    )
    
    class Meta:
        name = "Hello Variables"
        description = "Scripts Variable Examples"

    def run(self, data, commit):
        message = data["message"]
        days = data["days"]
        feelings = data["feelings"]
        
        self.log_info(f"Please give the message: {message} in {days} days.")
        self.log_info(f"I am feeling {feelings}!")
