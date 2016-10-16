all:
		gcc pthread_setaffinity_np_test.c -o pthread_setaffinity_np_test -lm -lpthread
		gcc pro_1.c -o pro_1 -lm -lpthread
		gcc pro_2.c -o pro_2 -lm -lpthread
		gcc pro_3.c -o pro_3 -lm -lpthread

clean:
    find . -name '*.out' -exec rm --force {}

run:
    ./pthread.out
		./proc_1.out
		./proc_2.out
		./proc_3.out
