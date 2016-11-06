import time
import tweepy
import random
import os.path
from security import OAUTH_TOKEN,OAUTH_SECRET,CONSUMER_KEY,CONSUMER_SECRET

#candidate twitter handles
candidates=[]
candidates.append("realDonaldTrump")
candidates.append("HillaryClinton")

#construct all of our list of proxy 
#accounts for each 'concept' we want
#to track

#conservative
conservative=[]
conservative.append("yrnf")
conservative.append("arepublicantx")
conservative.append("amconmag")

#liberal
liberal=[]
liberal.append("youngdemocrat")
liberal.append("LiberalEffects")
liberal.append("HomelandDems")

#men's rights
mra=[]
mra.append("sjw_nonsense")
mra.append("mensrightsblogs")
mra.append("mensrightsrdt")

#racism
racism=[]
racism.append("ANP14") #nazi party 
racism.append("kkkofficial")
racism.append("TGSNTtv")

#9/11 inside job
conspiracy=[]
conspiracy.append("911truthnews")
conspiracy.append("AE911Truth")
conspiracy.append("FalseFlag_911")

#ufos/aliens
ufos=[]
ufos.append("JM_Ashley")
ufos.append("UFOChronicles")
ufos.append("AncientAliens")

#climate change skeptics
climate=[]
climate.append("climateoftruth")
climate.append("Carbongate")
climate.append("ClimateTruthNow")

#paranormal
paranormal=[]
paranormal.append("ghostsnhaunts")
paranormal.append("Jchawes")

#chemtrails
chemtrail=[]
chemtrail.append("Chemtrails_818")
chemtrail.append("ChemtrailsWorld")
chemtrail.append("OpChemtrails")

#flatearth
flatearth=[]
flatearth.append("FlatEarthToday")
flatearth.append("flatearth_truth")
flatearth.append("FlatEarthOrg")

#homophobe
homophobe=[]
homophobe.append("WBCFredJr")
homophobe.append("burn_rainbows")

#creationism
creationism=[]
creationism.append("DiscoveryInst1")
creationism.append("crevinfo")
creationism.append("behe2810")

#homeopathy
homeopathy=[]
homeopathy.append("honatur_en") #homeopathy
homeopathy.append("ilovehomeopathy") #homeopathy
homeopathy.append("homeopathyinfo")
homeopathy.append("HomeopathyWorld")
homeopathy.append("HomeopathyWFM")

#vaxxer
vaxxer=[]
vaxxer.append("vaxxedthemovie")
vaxxer.append("ceestave")
vaxxer.append("TannersDad")
vaxxer.append("AutismMedia")
vaxxer.append("VaccineXchange")

to_check = conservative+liberal+chemtrail+flatearth+climate+vaxxer+homeopathy+creationism+conspiracy+racism+mra+ufos+paranormal+homophobe
to_check +=candidates

if __name__=='__main__':
 #scrape twitter for all the follower data for our proxy accounts and candidate accounts
 auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
 auth.set_access_token(OAUTH_TOKEN, OAUTH_SECRET)

 api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

 #for each individual screen name
 for sn in to_check:
  print sn
  ids = []
  
  #if we already have downloaded it, skip...
  fn ="data/%s.dat"%sn
  if os.path.exists(fn):
   continue 
 
  #otherwise grab page after page of followers from twitter api
  for page in tweepy.Cursor(api.followers_ids, screen_name=sn).pages():
    ids.extend(page)
    a=open(fn,"w")
    import json
    json.dump(ids,a)
    a.close()
    print len(ids)
    time.sleep(random.randint(30,90))
