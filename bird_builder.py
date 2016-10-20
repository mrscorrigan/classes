from birds.mybird import Bird, Seabird


sam_gull = Bird("Seagull", "Scraaawk")
sam_gull.do_call()
sam_owl = Bird("Owl", "Twit twoo")
sam_owl.do_call()
sam_crow = Bird("Crow", "Craaw")
sam_crow.do_call()


sam_owl.repeat_bird()



gull = Seabird("Seagull", "Jarp", 10)
print gull.do_call()