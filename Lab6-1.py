names=[("vraj",),"suhani","hetangi",("dhruv",),"khushi"]
boys_count=sum(1 for name in names if isinstance(name,tuple))
girl_count=sum(1 for name in names if isinstance(name,str))
print("number of boys=",boys_count)
print("number of girls=",girl_count)