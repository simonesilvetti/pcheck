import numpy as np
class Monitor:
    def __init__(self,tf,acc,acct,s,t,T,p):
        self.T = T
        self.p = p
        self.t = t
        self.s = s
        self.acct = acct
        self.acc = acc
        self.tf = tf

    # def monitorize(self,xnew,tnew):
    #     dt=(tnew-self.t[-1])
    #     self.s.append(xnew)
    #     self.t.append(tnew)
    #
    #     if (tnew-self.ti<self.T):
    #         dtf = tnew - self.tf
    #         self.tf = tnew
    #         self.acc += dtf*xnew
    #         return None,None, self
    #     if (tnew-self.ti>self.T):
    #         self.tf = self.ti+self.T
    #
    #
    #     else:
    #         if(dt<self.t[1]-self.t[0]):
    #             dtf=tnew-self.tf
    #             self.tf = tnew
    #             self.ti+=(self.tf-self.T)
    #             dti=(self.ti-self.t[0])
    #             self.acct +=(self.ti-self.t[0])
    #             self.t[0]=self.ti
    #             accold=self.acc
    #             self.acc+=-self.s[0]*dti+xnew*dtf
    #             if((accold-self.p*self.T)*(self.acc-self.p*self.T)<0):
    #                 return self.acct+ abs(accold-self.p),accold >= self.p, self
    #             else:
    #                 return None,None,self

    def monitorize(self,snew,tnew):
        res = list()
        self.s.append(snew)
        self.t.append(tnew)
        if (tnew - self.t[0]) <= self.T:
            dh=tnew-self.tf
            self.tf = tnew
            self.acc += dh * snew
            return res, self
        while(self.tf<tnew):
            if(self.t[1]-self.t[0]<tnew -self.tf):
                dh=self.t[1]-self.t[0]
                self.tf+=dh
                self.t.pop(0)
                s0 = self.s.pop(0)
            else:
                dh=tnew-self.tf
                self.t[0]=self.t[0]+dh
                self.tf=tnew
                s0=self.s[0]
            accold = self.acc
            self.acc += dh * (snew - s0)
            self.acct += dh
            T=self.tf-self.t[0]
            if (accold - self.p*T) * (self.acc - self.p*T)+1E-15 < 0:
                value = self.acct - abs(self.acc - self.p*T)
                exit = accold > self.p
                res.append([value, exit])

        return res, self

    def monitorizeExp(self,snew,tnew):
        res = list()
        self.s.append(snew)
        self.t.append(tnew)
        if (tnew - self.t[0]) <= self.T:
            dh=tnew-self.tf
            self.tf = tnew
            self.acc += dh * snew
            return res, self
        while(self.tf<tnew):
            if(self.t[1]-self.t[0]<tnew -self.tf):
                dh=self.t[1]-self.t[0]
                self.tf+=dh
                self.t.pop(0)
                s0 = self.s.pop(0)
            else:
                dh=tnew-self.tf
                self.t[0]=self.t[0]+dh
                self.tf=tnew
                s0=self.s[0]
            accold = self.acc
            self.acc += dh * (snew - s0)
            self.acct += dh
            T=self.tf-self.t[0]
            if (accold - self.p*T) * (self.acc - self.p*T)+1E-15 < 0:
                value = self.acct - abs(self.acc - self.p*T)
                exit = accold > self.p
                res.append([value, exit])

        return res, self


m=Monitor(0,0,0,[],[0],1,0.4)
res,m=m.monitorize(0,0.5)
print(res)
res,m=m.monitorize(1,1)
print(res)




# s=[0,1]
# t=[0,0.5,1.0]
# p=0.4
# tf=1
# acct=0
# acc=0.5
# l=list()
# q=Monitor(tf,acc,acct,s,t,1,p)
res,m=m.monitorize(0,1.6)
print(res)
res,m=m.monitorize(1,2.5)
print(res)
res,m=m.monitorize(0,3.7)
print(res)
res,m=m.monitorize(1,4.2)
print(res)
res,m=m.monitorize(0,4.9)
print(res)
res,m=m.monitorize(1,5.7)
print(res)
res,m=m.monitorize(0,5.8)
print(res)
res,m=m.monitorize(1,5.9)
print(res)
res,m=m.monitorize(0,6.9)
print(res)
print(0)
