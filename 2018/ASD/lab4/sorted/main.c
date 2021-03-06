#include <stdlib.h>
#include <stdio.h>
#include "search.h"
#include "sorted_table.h"
int main(){
    table* t1,*t2,*t3;
    srand(rand());

    printf("MAX STEPS\n");
    for(int size=50;size<=450;size+=50){
        t1=table_init(size);
        t2=table_init(size);
        t3=table_init(size);
        fill_table(t1,size);
        fill_table(t2,size);
        fill_table(t3,size);
        switch_search(1);
        search_function(t1,size);
        printf("Fast linear search do in %d operation for %d elements\n",counter,size);
        switch_search(2);
        search_function(t2,size);
        printf("Binary search do in %d operation for %d elements\n",counter,size);
        switch_search(3);
        search_function(t3,size);
        printf("Block search do in %d operation for %d elements\n",counter,size);
        table_done(t1);
        table_done(t2);
        table_done(t3);
    }
    printf("AVERANGE STEPS\n");
    for(int size=50;size<=450;size+=50){
        t1=table_init(size);
        t2=table_init(size);
        t3=table_init(size);
        fill_table(t1,size);
        fill_table(t2,size);
        fill_table(t3,size);
        switch_search(1);
        search_function(t1,size/2);
        printf("Fast linear search do in %d operation for %d elements\n",counter,size);
        switch_search(2);
        search_function(t2,size/2);
        printf("Binary search do in %d operation for %d elements\n",counter,size);
        switch_search(3);
        search_function(t3,size/2);
        printf("Block search do in %d operation for %d elements\n",counter,size);
        table_done(t1);
        table_done(t2);
        table_done(t3);

    }

    return 0;
}
