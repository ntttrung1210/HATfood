from hfdb import*

s1 = u'ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝàáâãèéêìíòóôõùúýĂăĐđĨĩŨũƠơƯưẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẲẳẴẵẶặẸẹẺẻẼẽẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộỚớỜờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỲỳỴỵỶỷỸỹ'
s0 = u'AAAAEEEIIOOOOUUYaaaaeeeiioooouuyAaDdIiUuOoUuAaAaAaAaAaAaAaAaAaAaAaAaEeEeEeEeEeEeEeEeIiIiOoOoOoOoOoOoOoOoOoOoOoOoUuUuUuUuUuUuUuYyYyYyYy'
def remove_accents(input_str):
	s = ''
	for c in input_str:
		if c in s1:
			s += s0[s1.index(c)]
		else:
			s += c
	return s

def dk1(a,b):
    a=remove_accents(a)
    b=remove_accents(b)
    dem=0
    l1=len(a)
    l2=len(b)
    if l1>l2:
        l=l2
    else:
        l=l1
    for v in range(l):
        if a[v].lower()==b[v].lower():
            dem=dem+1
        else:
            break
    if float(dem/l)>0.75:
        return 1
    else:
        return 0

def search_by_key(food):
    ls = []
    ls_f = get_all_food()
    ls_f1= get_all_food()
    for i in range(len(ls_f)):
        ls_f[i]['name']=remove_accents(ls_f[i]['name'])
    food=remove_accents(food)
    dk=0
    for i in range(len(ls_f)):
        new1=ls_f[i]['name'].split()
        new2=food.split()
        for j in range(len(new2)):
            for k in range(len(new1)):
                if dk1(new1[k],new2[j])==1:
                    ls.append(ls_f1[i])
                break            
    return ls
