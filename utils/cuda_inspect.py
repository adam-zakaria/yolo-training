import torch

a=torch.cuda.is_available()
b=torch.cuda.device_count()
c=torch.cuda.current_device()
d=torch.cuda.device(0)
e=torch.cuda.get_device_name(0)
print(a,b,c,d,e)
