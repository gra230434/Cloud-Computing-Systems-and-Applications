all:
	gcc pthread_setaffinity_np_test.c -o pthread_setaffinity_np_test -lm -lpthread
	gcc pro_1.c -o pro_1 -lm -lpthread
	gcc pro_2.c -o pro_2 -lm -lpthread
	gcc pro_3.c -o pro_3 -lm -lpthread

clean:
	rm -f pthread_setaffinity_np_test
	rm -f pro_1
	rm -f pro_2
	rm -f pro_3

run:
	./pthread
	./pro_1
	./pro_2
	./pro_3
