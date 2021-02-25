import sys
import argparse
import math

def solution(file,file_out):
    #If the street name is not present in intersection conguration it means its trac light is always red. 
    #If an intersection conguration is not present in the submission le then all of its traffic lights are always red.

    f=open(file,"r")
    #first line
    line=f.readline()
    #D=duration
    #I= number of intersections
    D,I,S,V,F=line.split(" ")

    #streets array
    #each street has B,E,NAME,L
    #B=start node (intersection)
    #E=end node
    #L=length
    streets={}
    intersections=[[] for i in range(int(I))]
    #streets
    for i in range (int(S)):
        line=f.readline()
        line=line.rstrip()
        B,E,name,L=line.split(" ")
        streets[name] = {"B":int(B),"E":int(E),"L":int(L), "occurrences":0, "seconds":0, "score":0}
        intersections[int(E)].append(name)
    #car
    paths=[]
    for k in range(int(V)):
        line=f.readline()
        line=line.rstrip()
        path=line.split(" ")
        path[0]=int(path[0])
        
        paths.append(path)
        #per ogni strada che la macchina percorre
        idx=1
        for street in path[1:]:
            #prima strada di una macchina
            if(idx==1): streets[street]["score"]+=1
            streets[street]["occurrences"]+= ( 1 ) 
            idx+=1

    #per ongi intersezione, calcolo  quante occorrenze ha ogni strada
    #per ognuna di qeuste strade, in quale percentuale appare rispetto al numero di strade totali dell'intersezione 
    #assegno ad ogni strada una percentuale del tempo totale rispetto alla percentuale della strada
    #questo tempo viene suddiviso in intearvalli dipendenti dal tempo totale


    considered_intersections=0


    for i in range(len(intersections)):
        intersection=intersections[i]
        somma = 0
        #occorrence di tutte le strade (per calcolo percentuale rispetto a questo numero)
        for street in intersection:
            somma += streets[street]["occurrences"]
        if(somma==0): 
            continue
        else:
            considered_intersections+=1

        #per ongi strada ora calcolo la percentuale
        int_T= int(D)* 1/100
        for street in intersection:
            # *********************** CONTROLLA ARROTONDAMENTI **********************************
            streets[street]["seconds"] = int( ((streets[street]["occurrences"]) / somma) * int_T)
            if(streets[street]["seconds"]==0): streets[street]["seconds"]=1
        #sort in base al numero di occorrenze
        
        intersections[i]=sorted(intersections[i],key=lambda x: streets[x]["score"],reverse=True)
        
    
    sol = open(file_out, "w")
    #intersection that we considered
    sol.write("{}\n".format(considered_intersections))

    for i in range(len(intersections)):
        street_buffer=""
        considered_streets = 0
        for street in intersections[i]:
            seconds=streets[street]["seconds"]
            if(seconds!=0): considered_streets+=1
            #output per questa strada
            out_street="{} {}\n".format(street,seconds)
            street_buffer=street_buffer+out_street
        if(considered_streets==0):
            street_buffer="" 
            continue
        else:
            sol.write("{}\n{}\n{}".format(str(i),str(considered_streets),street_buffer))
    sol.flush()


file_names=["a.txt","b.txt","c.txt","d.txt","e.txt","f.txt"]
file_out_names=["a_sol.txt","b_sol.txt","c_sol.txt","d_sol.txt","e_sol.txt","f_sol.txt"]
for i in range(len(file_names)):
    solution(file_names[i],file_out_names[i])
