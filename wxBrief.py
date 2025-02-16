#wxBrief class file



class WxBrief:

    def __init__(self, metar, taf, aptName):
        #initializes WxBriefing

        self.metar = metar
        self.taf = taf
        self.aptName = aptName
        self.pirep = {}
        self.airmet = {}


    def output(self):
        #print outputs to test variables are correctly assigned

        print(f"{self.metar}")
        print(f"{self.taf}")
        print(f"{self.aptName}")
        print(f"{self.pirep}")
        print(f"{self.airmet}")

        return
    
    def updateData(self,pireps,airmets):
        self.pirep.update(pireps)
        self.airmet.update(airmets)