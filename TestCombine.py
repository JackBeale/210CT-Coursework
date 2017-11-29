Final = {3: {4}, 4: {3, 5}, 5: {4, 6}, 6: {5}}
class Subset():
    def __init__ (self,v,w):
        self.v = v
        self.w = w
        
    def IsPath (v,w):
        Combine = {}
        Combine.update(v)
        Combine.update(w)
        
        if (Combine == Final):
            print("IS A PATH")
        elif v.keys() in w.keys():
            print("IS A PATH")
        else:
            print("NO PATH AVAILABLE")


v = dict((k, Final[k]) for k in (5,6)) #Sub Dic
w = dict((i, Final[i]) for i in (3,4)) #Sub Dic

Subset.IsPath(v,w)
