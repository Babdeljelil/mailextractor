import urllib.request
from urllib.error import URLError, HTTPError


fn=0
kfn="*"
def mailfinder(targeturl):

    global fn
    global kfn
    fp = urllib.request.urlopen(targeturl)
    mybytes = fp.read()

    mystr = mybytes.decode("utf8")
    fp.close()
    k=str(mystr)
    k=k.replace('"',"")
    k2=k.split()






    for l in k2:
       if "mailto" in l and (kfn not in l):
                                  fn=1
                                  print(l)


       if ("@" in l) and ("." in l) and ("<" not in l) and (">" not in l) and ("style" not in l) and (kfn not in l) and ("," not in l) and ("}" not in l):


                fn=1
                print(l)



#************************************************** end of mailfinder function*****************************************


trurl=input("enter the site url: ")

urltype=0   #check if the url have a extesion like .php .html .....
if (".shtml" in trurl) or (".html" in trurl) or (".php" in trurl) or (".asp" in trurl) or (".jsp" in trurl):
                                                                                                            urltype=1

if (trurl[len(trurl)-1] != "/" ) and urltype==0 : #checking if the target url dont finsih with /
    trurl=trurl+"/"


try:
    html = urllib.request.urlopen(trurl)

except HTTPError as e :

    e1=e.read().decode('utf-8')
    e2=e1.split()
    if "Cloudflare" in e2:
        print("the site is protected by Cloudflare")


    else:
        print("the site blocked my Resquest\nthe following is the site Response\n\n\n\n")
        print(e1)
    exit()
except URLError :
    print("Error cant deal with that site , try other one")
    exit()

except ValueError:
    print("Error cant deal with that site , try other one")
    exit()

except Exception:      # that is a general exception handeling
     print("Error cant deal with that site , try other one")
     exit()


print("Please wait until the Search finish:")





fp = html
mybytes = fp.read()

try:
       mystr = mybytes.decode("utf8")
except Exception:
    print("Error cant deal with that site , try other one")
    exit()

fp.close()
k=str(mystr)
h=str(mystr)


k=k.replace('"',"")

k2=k.split()






for l in k2:

    if "mailto" in l:
                         fn=1
                         kfn=l
                         print(l)

    if ("@" in l) and ("." in l) and ("<" not in l) and (">" not in l) and ("style" not in l) and ("," not in l) and ("}" not in l):


                           fn=1
                           kfn=l
                           print(l)







if urltype==1:      #that code is to remove last filename
                for i in range(-1,-1*len(trurl),-1) :
                                                       if trurl[i]=="/":
                                                                              slashid=i
                                                                              break


                Rslashid=len(trurl)+slashid
                newrurl=""
                for i in range(0,Rslashid+1):
                                               newrurl+=trurl[i]





h2=h.split("<a")
h3=str(h2)
h4=h3.split(">")
h5=str(h4)
h6=h5.split()

repet=[] # to check if the href we found is new or already found
for l2 in h6:
    if ("href" in l2) and (".php" in l2 or ".html" in l2 or ".asp" in l2 or ".aspx" in l2  ) and ("http" not in l2):
        l3=l2.split('"')
        if urltype==1:
                            utt=newrurl+l3[1]
        else:
                            utt=trurl+l3[1]  #storing the website link
        try:
            html = urllib.request.urlopen(utt)
        except HTTPError :
            continue
        except URLError:
            continue
        except ValueError:
            continue
        except Exception:
            continue

        mailfinder(utt)
    if ("href" in l2) and (trurl in l2) and (".php" in l2 or ".html" in l2 or ".asp" in l2 or ".aspx" in l2  ):
        l3=l2.split('"')
        utt=l3[1]  #storing the website link
        if utt not in repet:
            try:
                html = urllib.request.urlopen(utt)
            except HTTPError :
                continue
            except URLError:
                continue
            except ValueError:
                continue
            except Exception:
                continue

            mailfinder(utt)
            repet.append(utt)





if fn==0:
    print("sorry no email found ")