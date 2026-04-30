from extras.scripts import Script, MultiChoiceVar

class HelloVariables(Script):

    CHOICES = (
        ('h', 'Happy'),
        ('s', 'Sad'),
        ('e', 'Excited'),
        ('b', 'Bored'),
    )    
    
    feelings = MultiChoiceVar(
        choices=CHOICES,
        description="How are you feeling?"
    )
    
    class Meta:
        name = "Hello Variables"
        description = "Scripts Variable Examples"

    def run(self, data, commit):
        feelings = data["feelings"]
        
        self.log_info(f"I am feeling {feelings}!")
