class Bird:
    def __init__(self, kind, call):
        self.kind = kind
        self.call = call
    def do_call(self):
        print 'a %s goes %s' % (self.kind, self.call)

sam_gull = Bird("Seagull", "Scraaawk")

sam_gull.do_call()

sam_owl = Bird("Owl", "Twit twoo")
sam_owl.do_call()
sam_crow = Bird("Crow", "Craaw")
sam_crow.do_call()



