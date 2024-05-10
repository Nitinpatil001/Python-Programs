#print continenet wise country name
cont=["asia","australia","north america","south america","europe"]
cnt={"india":"asia","srilanka":"asia","australia":"australia","china":
     "asia"
     ,"america":"north america","london":"europe","pakistan":"asia",
     "germeny":"europe"}
popu={"india":140,"srilanka":10,"australia":15,"china":130,
      "america":22,"london":40,"pakistan":10,"germeny":12}
for i in cont:
    print(i)
    for j in cnt:
        if i==cnt[j]:
            print("",j)
