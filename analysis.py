import csv
import random
import json 
from downloader import conservative,liberal,chemtrail,vaxxer,homeopathy,conspiracy,racism,mra,ufos,paranormal,creationism,flatearth,homophobe

#create all the different heuristics
target_list=[]
target_list.append((conservative,"Conservative"))
target_list.append((liberal,"Liberal"))
target_list.append((ufos,"Aliens"))
target_list.append((paranormal,"Ghosts"))
target_list.append((vaxxer,"Anti-Vaccination"))
target_list.append((homeopathy,"Homeopathy"))
target_list.append((conspiracy,"9/11 Truth"))
target_list.append((racism,"White Supremicist"))
target_list.append((homophobe,"Anti-Gay"))
target_list.append((flatearth,"Flat Earth"))
target_list.append((chemtrail,"Chemtrails"))
target_list.append((mra,"Men's Rights"))
target_list.append((creationism,"Intelligent Design"))


#follower size at time of collection: 11/5/16 
#hillary 10.2 million (collected approx 5 million)
#donald 13.0 million (collected approx 4.5 million)
candidates=["realDonaldTrump","HillaryClinton"]
follower_count = [13000000,10200000]
follower_count_by_candidate = dict(zip(candidates,follower_count))

#helper function to load in lists of twitter follower ids
def load(name,cap=None):
 arr= json.load(open("data/"+name+".dat"))
 #print name,len(arr)
 random.shuffle(arr)
 if cap==None:
  return arr
 return arr[:cap] 


outfile = open("data.csv","w")
csvwriter = csv.writer(outfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
csvwriter.writerow(["Concept","Value","Hue"])


#load in candidate followers
#note: we load in max of 1/3 of a candidate's total followers
#      so that statistically there's not a bias towards 
#      over/under-estimating the overlap between candidate
#      followers. wouldn't have to do this if scraping 
#      twitter for 10 million users didn't take a few days
candidate_followers = {}
candidate_observe_pct = {}
for idx,candidate in enumerate(candidates):
  candidate_followers[candidate] = set(load(candidate,cap=follower_count[idx]/3))
  candidate_observe_pct[candidate] = float(len(candidate_followers[candidate]))/follower_count[idx]

from collections import defaultdict

#loop over all the target concepts
for targets,title in target_list:
 hits = defaultdict(set)

 #aggregate the proxy twitter accounts for that target
 target_ids = set()
 for target in targets:
  target_ids = target_ids.union(set(load(target)))
 
 #a hit for each candidate is when a follower of a candidate
 #follows one of the proxy twitter accounts
 for candidate in candidates:
  intersect = candidate_followers[candidate].intersection(target_ids)
  hits[candidate] = intersect

 candidate1 = candidates[0]
 candidate2 = candidates[1]
 ratio = {}

 #calculate how many people are following both candidates in the sample of target hits
 #the idea is that if someone follows both candidates, we're not sure who they support
 c1hits = hits[candidate1]
 c2hits = hits[candidate2]
 sample_overlap = len(c1hits.intersection(c2hits))

 #print len(c1hits),len(c2hits)
 #print sample_overlap

 for candidate in candidates: #[candidate1,candidate2]:
  raw_hits = len(hits[candidate])

  #adjusted hits corrects for people who follow both candidates
  adjusted_hits = raw_hits - sample_overlap

  ratio[candidate] = float(adjusted_hits) / len(candidate_followers[candidate])
 
  #print candidate,raw_hits,adjusted_hits,ratio[candidate]

 #don over hil ratio
 don_over_hil = ratio[candidate1]/ratio[candidate2]

 #recenter around 0
 #positive numbers means that concept leans donald
 #negative numbers means that concept leans trump
 if don_over_hil > 1.0:
  hue="Trump"
  out = don_over_hil - 1.0
 else:
  hue="Clinton"
  out = - ((1.0/don_over_hil)-1.0)
 
 csvwriter.writerow([title,out,hue])
 print title,out

