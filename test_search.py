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

def search_by_key(food):
    ls = []
    ls_f = get_all_food()
    ls_f1= get_all_food()
    for i in range(len(ls_f)):
        ls_f[i]['name']=ls_f[i]['name'].lower()
        ls_f[i]['name']=remove_accents(ls_f[i]['name'])
    food=remove_accents(food).lower()
    for i in range(len(ls_f)):
        if ls_f[i]['name'].find(food)!=-1:
            ls.append(ls_f1[i])
    for i in range(len(ls_f)):
        new1=ls_f[i]['name'].split()
        new2=food.split()
        for j in range(len(new2)):
            for k in range(len(new1)):
                if new1[k]==new2[j]:
                    ls.append(ls_f1[i])
                break            
    return ls
