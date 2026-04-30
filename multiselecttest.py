from extras.scripts import Script, ChoiceVar

class HelloVariables(Script):

    CHOICES = (
        ('Happy', 'Happy'),
        ('Sad', 'Sad'),
        ('Excited', 'Excited'),
        ('Bored', 'Bored'),
    )    
    
    feelings = ChoiceVar(
        choices=CHOICES,
        description="How are you feeling?"
    )
    
    class Meta:
        name = "Hello Variables"
        description = "Scripts Variable Examples"

    def run(self, data, commit):
        feelings = data["feelings"]
        
        self.log_info(f"I am feeling {feelings}!")
