import math
import sys
from transition_cal import *
from datafile import * 



class Tree:
    def __init__(self,cat = None, children = None, value=0.0, name = 'home1',ispresent=False):
        self.cat = cat
        self.name = name
        self.ispresent = ispresent
        self.children = []
        self.value = value
        if children is not None:
            for child in children:
                self.children.append(child)

    
    def eminmax(self, k, goals, prob, took, maxh, dist, adj):
    
        if k==0:
            #print('sign taken')
            self.value = dist
            return dist
        if maxh==0 and k<>0 and self.cat=='mx':
            #print('not enough ppl') 
            self.value = 9999+dist
            return (9999+dist)
        
        if(self.cat=='mx'):
            self.value = sys.maxsize
            self.children = []
            for g in goals:
                if took[g]==False:
                    mk = Tree('ch',None,sys.maxsize,g,False)
                    self.children.append(mk)
            for child in self.children:
                #print('child :' ,child.name)
                took[child.name] = True
                #print('checking goal par :',child.name,self.name)
                '''sx = adj[self.name][0]
                sy = adj[self.name][1]
                dx = adj[child.name][0]
                dy = adj[child.name][1]'''
                val = data[order[self.name]][order[child.name]]
                #val = math.sqrt((sx-dx)**2+(sy-dy)**2)
                self.value = min(self.value, child.eminmax(k, goals, prob, took, maxh-1,val+dist, adj))
                took[child.name] = False
        elif(self.cat=='ch'):
            self.value = sys.maxsize
            self.children = []
            for i in range(1,3):
                mk = Tree('mx',None,sys.maxsize,self.name,False)
                self.children.append(mk)
            child = self.children[0]
            child.ispresent = True
            pic1 = (prob[self.name]*child.eminmax(k-1, goals, prob, took, maxh,dist, adj))
            child = self.children[1]
            pic2 = ((1-prob[self.name])*(child.eminmax(k,goals, prob, took, maxh, dist, adj)))
            self.value = pic1+pic2
        return self.value

    def run(self, k, goals, prob, took, h, adj):
        cal_transition()
        val = sys.maxsize
        node = self
        self.value = self.eminmax( k, goals, prob, took, h, 0, adj)
        return self.value

    def bfs(self):
        root = self
        queue = [root]
        explored = []
        while queue:
            node = queue.pop(0)
            #print(node.name , node.value, node.ispresent)
            if node not in explored:
                explored.append(node)
                for child in node.children:
                    queue.append(child)


