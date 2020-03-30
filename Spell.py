class Spell:
    #Parent Class
    def __init__(self, incantation, name):
        #Base Class
        self.name = name
        self.incantation = incantation
    def __str__(self):
        #Base Class
        return self.name + ' ' + self.incantation + '\n' + self.get_description()

    def get_description(self):
        #Base Class
        return 'No description'

    def execute(self):
        #Base Class
        print (self.incantation)

class Accio(Spell):
    #Child Class
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')

class Confundo(Spell):
    #Child Class
    def __init__(self):
        Spell.__init__(self, 'Confundo', 'Confundus Charm')
    #Sub Class
    def get_description(self):
        return 'Causes the victim to become confused and befuddled.'

def study_spell(spell):
    print (spell)

spell = Accio()
spell.execute()
study_spell(spell)
study_spell(Confundo())

#Estimate Output
# Accio
# Summoning Charm Accio
# No Description
# Confundus Charm Confundo
# Causes the victim to become confused and befuddled.

# When study_spell(Confundo()) executes...what get_description method gets called and why?
# The get_description of the Confundo Class because it overloads the parent class

# Add to the Accio Class
#   def get_description(self):
#        return 'This charm summons an object to the caster, potentially over a significant distance'