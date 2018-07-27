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
	print("a = ");
	scanf("%d", &a);
	print("b = ");
        scanf("%d", &b);
	printf("%d + %d = %d", a,b,a+b);
}
```

> Bahasa Python
```
a = input("a = ")
b = input("b = ")

print("%d + %d = %d" % (a,b,a+b)) 

print("{0} + {1} = {2}".format(a,b,a+b))

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

#### 5. Loop/Perulangan

> Bahasa C
```
#include <stdio.h>

int main()
{
	int i;
	for(i=0; i<10; i++)
	{
	    printf("%d ", i);
	}
    i=0
    while(i<10)
    {
        i++;
        printf("%d ", i); 
    }
}
```

> Bahasa Python
```
for i in range(0,10):
	print(i, end=' ')

i=0
while i < 10:
    i+=1
    print(i)
```

#### 6. Struktur Data (List)
> Bahasa C
```
#include <stdio.h>

int main()
{
    int arr[4] = {10, 20, 30, 40};
    int i;
    for(i=0; i<4; i++)
    {
        printf("%d ", arr[i]);
    }
}
```