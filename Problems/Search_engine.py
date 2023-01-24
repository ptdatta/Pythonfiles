# Sentences=["This is good","Python is good","Python is not python snake"]
# a=input("Enter quary string" ).lower()
# for i in Sentences:
#     list=i.lower().split()
#     if(a in list):
#         print(i)
#


# Harry's solution-->
def matchingwords(sentence1,sentence2):
    word1=sentence1.split(" ")
    word2=sentence2.split(" ")
    score=0
    for i in word1:
        for j in word2:
            # print(f"Matching {i} with {j}")
            if i.lower()==j.lower():
                score+=1
    return score

if __name__ == '__main__':
   sentences=["python is a good","this is snake",
              "harry is a good boy","Subscibe to code with harry"]

   quary=input("enter input string")
   scores=[matchingwords(quary,sentence) for sentence in sentences]
   # print(scores)
   sortedsentscore=[sentscore for sentscore in sorted(zip(scores,sentences),reverse=True)]
   # print(sortedsentscore)
   print(f"{len(sortedsentscore)} results found:")
   for score,item in sortedsentscore:
       print(f"\"{item}\" with a score of {score}")