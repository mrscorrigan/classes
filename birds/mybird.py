class Bird:
    def __init__(self, kind, call):
        self.kind = kind
        self.call = call

    def do_call(self):
        print 'a %s goes %s' % (self.kind, self.call)

    def repeat_bird(self):
        print "This is the bird you have chosen %s" % (self.kind)


# class Parrot(Bird):
#     def __init__(self):
#         Bird.__init__(self, 'Parrot', 'Kawkaw')

class Seabird(Bird):
    def __init__(self, kind, call, depth):
        self.the_diving = depth
        Bird.__init__(self.kind, self.call)

    def diving_bird(self, depth):
        print "also this bird can dive %s meters" % (self.depth)
