from extras.scripts import Script, MultiSelectVar

class HelloVariables(Script):

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
        feelings = data["feelings"]
        
        self.log_info(f"I am feeling {feelings}!")
