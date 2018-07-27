# Doscom Sharing Time | Python


### 1. Hello World
> Bahasa C
``` 
#include <stdio.h>

int main()
{
  printf("Hello lhur!");
}
```

> Bahasa Python
``` 
python3

print("Hello lhur!")

Output: Hello lhur
```

#### 2. Variable
> Bahasa C
```
#include <stdio.h>

int main()
{
	int a = 90;
	float b = 3.14;
	char nama[10] = "DOSCOM";
}
```

> Bahasa Python
```
a = 90;
b = 3.14;
nama = "DOSCOM"
```
#### 3. Input dan Output
> Bahasa C
```
#include <stdio.h>

int main()
{
	int a,b;
	a = 2;
	b = 3;
	printf("%d + %d = %d", a,b,a+b);
}
```

> Bahasa Python
```
a = 2
b = 3

print("%d + %d = %d" % (a,b,a+b)) 
#output: 2 + 3 = 5

print("{0} + {1} = {2}".format(a,b,a+b))
#output: 2 + 3 = 5
```

#### 4. IF CONDITION
> Bahasa C
```
#include <stdio.h>

int main()
{
	int a,b;
	a = 2;
	b = 3;
	if(a==b)
	{
		printf("Salah\n");
	}
	else
	{
		printf("Benar\n");	
	}	
}
```

> Bahasa Python
```
a = 2
b = 3
if(a==b):
	print("Salah")
else:
	print("Benar")
```
